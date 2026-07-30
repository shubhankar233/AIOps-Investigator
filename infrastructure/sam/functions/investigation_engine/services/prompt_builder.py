class PromptBuilder:
    """
    Builds prompts for AI-powered incident investigation.
    """

    def build(
        self,
        incident_id: str,
        logs: list,
        findings: list
    ) -> str:

        findings_text = (
            "\n".join(f"- {item}" for item in findings)
            if findings
            else "- No known issues detected"
        )

        logs_text = "\n".join(
            f"{index + 1}. {log}"
            for index, log in enumerate(logs)
        )

        prompt = f"""
You are an AWS Cloud Incident Investigation Assistant.

Analyze the following cloud incident.

Incident ID:
{incident_id}

Detected Issues:
{findings_text}

Application Logs:
{logs_text}

Tasks:

1. Identify the probable root cause.
2. Explain your reasoning.
3. Suggest remediation steps.
4. Assign a confidence level.
5. Keep the answer concise.
"""

        return prompt.strip()