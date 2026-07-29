from shared.logger import log_info
from services.rule_engine import RuleEngine

rule_engine = RuleEngine()

class InvestigationService:
    """
    Handles incident investigation logic.
    """

    def analyze(self, incident_id: str, logs: list) -> dict:

        log_info(
            "Starting investigation",
            incident_id=incident_id
        )

        findings = rule_engine.analyze(logs)

        severity = "LOW"

        if len(findings) >= 2:
            severity = "HIGH"

        elif len(findings) == 1:
            severity = "MEDIUM"

        analysis = {
            "analysis_mode": "rule-engine",
            "summary": f"{len(findings)} issue(s) detected.",
            "severity": severity,
            "root_cause": findings if findings else ["Unknown"],
            "recommendation": (
                "Proceed to AI investigation."
                if findings
                else "No known issue detected."
            )
        }

        log_info(
            "Investigation completed",
            incident_id=incident_id
        )

        return analysis
