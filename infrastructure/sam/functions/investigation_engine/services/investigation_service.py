from shared.logger import log_info
from services.rule_engine import RuleEngine
from services.bedrock_service import BedrockService


class InvestigationService:
    """
    Handles incident investigation logic.
    """

    def __init__(self):
        self.rule_engine = RuleEngine()
        self.bedrock_service = BedrockService()

    def analyze(self, incident_id: str, logs: list) -> dict:

        log_info(
            "Starting investigation",
            incident_id=incident_id
        )

        # Step 1: Run rule engine
        findings = self.rule_engine.analyze(logs)

        severity = "LOW"

        if len(findings) >= 2:
            severity = "HIGH"

        elif len(findings) == 1:
            severity = "MEDIUM"

        # Step 2: Run AI investigation
        ai_result = self.bedrock_service.analyze_incident(
            incident_id=incident_id,
            issues=findings,
            logs=logs
        )

        analysis = {
            "analysis_mode": "rule-engine + bedrock",
            "summary": f"{len(findings)} issue(s) detected.",
            "severity": severity,
            "root_cause": findings if findings else ["Unknown"],
            "recommendation": (
                "AI investigation completed."
                if findings
                else "No known issue detected."
            ),
            "ai_result": ai_result
        }

        log_info(
            "Investigation completed",
            incident_id=incident_id
        )

        return analysis