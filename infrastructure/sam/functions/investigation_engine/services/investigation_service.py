from shared.logger import log_info
from services.rule_engine import RuleEngine
from services.bedrock_service import BedrockService
from repositories.investigation_repository import InvestigationRepository


class InvestigationService:
    """
    Handles incident investigation logic.
    """

    def __init__(self):
        self.rule_engine = RuleEngine()
        self.bedrock_service = BedrockService()
        self.repository = InvestigationRepository()

    def analyze(self, incident_id: str, logs: list) -> dict:

        log_info(
            "Starting investigation",
            incident_id=incident_id
        )

        # ==========================================================
        # Step 1: Run rule engine with evidence
        # ==========================================================

        evidence = self.rule_engine.analyze_with_evidence(
            logs
        )

        findings = list(
            dict.fromkeys(
                item["issue"]
                for item in evidence
            )
        )

        severity = "LOW"

        if len(findings) >= 2:
            severity = "HIGH"

        elif len(findings) == 1:
            severity = "MEDIUM"

        log_info(
            "Rule engine analysis completed",
            incident_id=incident_id,
            finding_count=len(findings),
            evidence_count=len(evidence)
        )

        # ==========================================================
        # Step 2: Find similar previous investigations
        # ==========================================================

        similar_investigations = (
            self.repository.find_similar_investigations(
                issues=findings,
                current_incident_id=incident_id
            )
        )

        log_info(
            "Similar investigations found",
            incident_id=incident_id,
            count=len(similar_investigations)
        )

        # ==========================================================
        # Step 3: Run AI investigation
        # ==========================================================

        ai_result = self.bedrock_service.analyze_incident(
            incident_id=incident_id,
            issues=findings,
            logs=logs,
            similar_investigations=similar_investigations,
            evidence=evidence
        )

        # ==========================================================
        # Step 4: Build compact historical evidence
        # ==========================================================

        similar_incidents = []

        for investigation in similar_investigations:

            previous_analysis = investigation.get(
                "analysis",
                {}
            )

            similar_incidents.append(
                {
                    "incident_id": investigation.get(
                        "incident_id"
                    ),
                    "similarity_score": round(
                        investigation.get(
                            "similarity_score",
                            0
                        ) * 100
                    ),
                    "matching_issues": investigation.get(
                        "matching_issues",
                        []
                    ),
                    "severity": previous_analysis.get(
                        "severity",
                        "UNKNOWN"
                    ),
                    "summary": previous_analysis.get(
                        "summary",
                        "No summary available."
                    ),
                    "root_cause": previous_analysis.get(
                        "root_cause",
                        []
                    )
                }
            )

        # ==========================================================
        # Step 5: Calculate investigation confidence
        # ==========================================================

        confidence = "LOW"

        if findings and ai_result.get("confidence") == "HIGH":
            confidence = "HIGH"

        elif findings and ai_result.get(
            "confidence"
        ) in ["MEDIUM", "HIGH"]:
            confidence = "MEDIUM"

        # ==========================================================
        # Step 6: Build analysis result
        # ==========================================================

        analysis = {
            "analysis_mode": "rule-engine + historical-context + bedrock",
            "summary": f"{len(findings)} issue(s) detected.",
            "severity": severity,
            "root_cause": findings if findings else ["Unknown"],

            "similar_incidents_found": len(
                similar_investigations
            ),

            "similar_incidents": similar_incidents,

            "recommendation": (
                "AI investigation completed."
                if findings
                else "No known issue detected."
            ),

            "evidence": ai_result.get(
                "evidence",
                []
            ),

            "ai_result": ai_result
        }

        # ==========================================================
        # Step 7: Persist investigation
        # ==========================================================

        self.repository.save_investigation(
            incident_id=incident_id,
            logs=logs,
            analysis=analysis
        )

        log_info(
            "Investigation completed",
            incident_id=incident_id
        )

        return analysis

    def list_investigations(self) -> list:
        """
        Retrieve all stored investigations.
        """

        log_info(
            "Starting investigation history retrieval"
        )

        investigations = (
            self.repository.list_investigations()
        )

        log_info(
            "Investigation history retrieved",
            count=len(investigations)
        )

        return investigations