import json
import boto3

from shared.logger import log_info, log_error


class BedrockService:
    """
    Handles communication with Amazon Bedrock.
    """

    def __init__(self):
        self.client = boto3.client(
            "bedrock-runtime",
            region_name="us-east-1"
        )

        self.model_id = "amazon.nova-lite-v1:0"

    def analyze_incident(
        self,
        incident_id: str,
        issues: list,
        logs: list
    ) -> dict:
        """
        Send incident information to Amazon Bedrock
        and return the AI investigation result.
        """

        prompt = f"""
You are an AWS Cloud Incident Investigation Assistant.

Analyze the following cloud incident.

Incident ID:
{incident_id}

Detected Issues:
{chr(10).join(f"- {issue}" for issue in issues)}

Application Logs:
{chr(10).join(f"{i + 1}. {log}" for i, log in enumerate(logs))}

Tasks:

1. Identify the probable root cause.
2. Explain your reasoning.
3. Suggest remediation steps.
4. Assign a confidence level.
5. Keep the answer concise.
"""

        try:
            log_info(
                "Sending incident to Amazon Bedrock",
                incident_id=incident_id,
                model_id=self.model_id
            )

            response = self.client.converse(
                modelId=self.model_id,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "text": prompt
                            }
                        ]
                    }
                ],
                inferenceConfig={
                    "maxTokens": 500,
                    "temperature": 0.2
                }
            )

            ai_text = response["output"]["message"]["content"][0]["text"]

            log_info(
                "Bedrock analysis completed",
                incident_id=incident_id
            )

            return {
                "ai_summary": ai_text,
                "confidence": "AI-generated"
            }

        except Exception as error:
            log_error(
                "Bedrock analysis failed",
                incident_id=incident_id,
                error=str(error)
            )

            return {
                "ai_summary": "AI analysis failed.",
                "confidence": "N/A",
                "error": str(error)
            }