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
        logs: list,
        similar_investigations: list | None = None,
        evidence: list | None = None
    ) -> dict:
        """
        Send incident information and historical investigations
        to Amazon Bedrock and return the AI investigation result.
        """

        if similar_investigations is None:
            similar_investigations = []

        if evidence is None:
            evidence = []

        # ==========================================================
        # Build historical investigation context
        # ==========================================================

        historical_context = ""

        if similar_investigations:

            historical_context = (
                "\n\nPrevious Similar Investigations:\n"
            )

            for investigation in similar_investigations[:5]:

                previous_id = investigation.get(
                    "incident_id",
                    "Unknown"
                )

                similarity_score = investigation.get(
                    "similarity_score",
                    0
                )

                matching_issues = investigation.get(
                    "matching_issues",
                    []
                )

                previous_analysis = investigation.get(
                    "analysis",
                    {}
                )

                historical_context += f"""
Incident ID:
{previous_id}

Similarity Score:
{similarity_score:.0%}

Matching Issues:
{matching_issues}

Root Causes:
{previous_analysis.get("root_cause", [])}

Severity:
{previous_analysis.get("severity", "Unknown")}

AI Result:
{json.dumps(
    previous_analysis.get("ai_result", {}),
    indent=2
)}

---
"""

        else:

            historical_context = """
No previous similar investigations were found.
"""

        # ==========================================================
        # Build Bedrock prompt
        # ==========================================================

        prompt = f"""
You are an AWS Cloud Incident Investigation Assistant.

Your task is to investigate the CURRENT incident using:

1. Current application logs
2. Current rule-engine findings
3. Previous similar investigations as supporting evidence

==================================================
CURRENT INCIDENT
==================================================

Current Incident ID:
{incident_id}

Detected Issues:
{chr(10).join(f"- {issue}" for issue in issues)}

Application Logs:
{chr(10).join(
    f"{i + 1}. {log}"
    for i, log in enumerate(logs[:50])
)}

==================================================
HISTORICAL INVESTIGATION CONTEXT
==================================================

{historical_context}

==================================================
INVESTIGATION RULES
==================================================

The current incident is the primary source of truth.

Use historical investigations only as supporting evidence.

Do not blindly copy conclusions from previous incidents.

Consider the similarity score and matching issues when
evaluating historical investigations.

Determine the most likely technical root cause of the
CURRENT incident based primarily on the current logs
and detected issues.

If a previous investigation is relevant, explain how
it supports the current conclusion.

If historical evidence conflicts with the current logs,
prefer the current logs.

Do not assume that similar incidents have the same
root cause.

==================================================
OUTPUT REQUIREMENTS
==================================================

Return ONLY valid JSON.

Do not use Markdown.

Do not use code fences.

Do not add explanations outside the JSON.

Use exactly this structure:

{{
    "probable_root_cause": "string",
    "evidence": [
        "string"
    ],
    "reasoning": "string",
    "remediation_steps": [
        "string"
    ],
    "confidence": "LOW"
}}

Rules:

- probable_root_cause must contain the most likely
  technical root cause.

- evidence must contain the specific log observations
  that support the probable root cause.

- evidence must use information from the CURRENT logs.

- Do not invent evidence that is not present in the logs.

- Include only the most relevant evidence.

- reasoning must briefly explain why the CURRENT logs
  support the conclusion.

- reasoning may mention relevant historical evidence
  when appropriate.

- Historical incidents are supporting evidence only.
  They must not replace evidence from the CURRENT logs.

- remediation_steps must contain practical AWS/application
  remediation actions.

- confidence must be exactly one of:
  LOW, MEDIUM, HIGH.
"""

        # ==========================================================
        # Call Amazon Bedrock
        # ==========================================================

        try:

            log_info(
                "Sending incident to Amazon Bedrock",
                incident_id=incident_id,
                model_id=self.model_id,
                similar_incident_count=len(
                    similar_investigations
                )
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

            # ======================================================
            # Extract model response
            # ======================================================

            ai_text = response[
                "output"
            ][
                "message"
            ][
                "content"
            ][0]["text"]

            log_info(
                "Raw Bedrock response",
                response=ai_text
            )
            # ======================================================
            # Parse JSON response
            # ======================================================

            try:

                cleaned_text = ai_text.strip()

                # Remove accidental Markdown code fences
                if cleaned_text.startswith("```"):

                    cleaned_text = cleaned_text.replace(
                        "```json",
                        "",
                        1
                    ).replace(
                        "```",
                        "",
                        1
                    ).strip()

                ai_result = json.loads(
                    cleaned_text
                )

            except json.JSONDecodeError:

                log_error(
                    "Bedrock returned invalid JSON",
                    incident_id=incident_id,
                    raw_response=ai_text
                )

                return {
                    "probable_root_cause": (
                        "Unable to determine"
                    ),
                    "evidence": [],
                    "reasoning": (
                        "The AI model returned an invalid "
                        "response format."
                    ),
                    "remediation_steps": [],
                    "confidence": "LOW"
                }

            # ======================================================
            # Successful AI investigation
            # ======================================================

            log_info(
                "Bedrock analysis completed",
                incident_id=incident_id
            )

            return ai_result

        except Exception as error:

            log_error(
                "Bedrock analysis failed",
                incident_id=incident_id,
                error=str(error)
            )

            return {
                "probable_root_cause": "AI analysis failed",
                "evidence": [],
                "reasoning": (
                    "The investigation engine could not complete "
                    "the Amazon Bedrock analysis."
                ),
                "remediation_steps": [],
                "confidence": "LOW",
                "error": str(error)
            }