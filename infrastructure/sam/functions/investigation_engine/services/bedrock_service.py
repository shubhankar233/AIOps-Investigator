import json
import boto3

from shared.logger import log_info, log_error
from shared.config import (
    AWS_REGION,
    BEDROCK_MODEL_ID,
)

class BedrockService:
    """
    Handles communication with Amazon Bedrock.
    """

    def __init__(self):
        self.client = boto3.client(
            "bedrock-runtime",
            region_name=AWS_REGION
        )

        self.model_id = BEDROCK_MODEL_ID

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

    1. Analyze EVERY issue listed in DETECTED ISSUES.
2. Do NOT ignore, omit, or silently discard any detected issue.
3. Every detected issue must be addressed in the AI analysis.
4. For each detected issue, determine whether it is:
   - the probable primary root cause
   - a contributing issue
   - a downstream symptom
   - or an independent issue.
5. Use the CURRENT LOGS and CURRENT EVIDENCE as the primary source of truth.
6. Historical incidents are supporting context only. They are NOT proof of the current root cause.
7. Do not invent log events, infrastructure conditions, or historical facts.
8. If the current evidence is insufficient to establish causality, explicitly state that the relationship is uncertain.
9. Every issue that has direct log evidence must include that evidence in the analysis.
10. Do not assume that an issue is caused by another issue unless the available evidence supports that relationship.

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

    "issue_analysis": [
        {{
            "issue": "string",
            "role": "primary_root_cause",
            "evidence": [
                "string"
            ]
        }}
    ],

    "evidence": [
        "string"
    ],

    "reasoning": "string",

    "remediation_steps": [
        "string"
    ],

    "confidence": "LOW"
}}

==================================================
ISSUE ANALYSIS REQUIREMENTS
==================================================

The "issue_analysis" array is REQUIRED.

For EVERY issue listed under DETECTED ISSUES,
create exactly ONE entry in "issue_analysis".

Do NOT omit any detected issue.

Each issue_analysis entry MUST contain:

- issue
- role
- evidence

The "issue" field must exactly match one of the
issues listed under DETECTED ISSUES.

The "role" field must be exactly one of:

- "primary_root_cause"
- "contributing_issue"
- "downstream_symptom"
- "independent_issue"
- "uncertain"

The "evidence" field must contain the CURRENT log
observations that support that issue.

If an issue has no direct current-log evidence,
return an empty evidence array and use
"uncertain" when appropriate.

Do not invent evidence.

Example:

{{
    "issue_analysis": [
        {{
            "issue": "Database Connectivity",
            "role": "primary_root_cause",
            "evidence": [
                "ERROR Database connection timeout"
            ]
        }},
        {{
            "issue": "CPU Pressure",
            "role": "contributing_issue",
            "evidence": [
                "WARN CPU limit exceeded"
            ]
        }},
        {{
            "issue": "Authentication Failure",
            "role": "independent_issue",
            "evidence": [
                "ERROR Authentication failed"
            ]
        }}
    ]
}}

==================================================
GENERAL OUTPUT RULES
==================================================

- probable_root_cause must contain the most likely
  technical root cause.

- evidence must contain the most relevant CURRENT
  log observations supporting the probable root cause.

- Do not invent evidence that is not present in the
  CURRENT logs.

- reasoning must explain why the CURRENT logs support
  the conclusion.

- reasoning may mention historical investigations
  when appropriate.

- Historical incidents are supporting evidence only.
  They must not replace CURRENT log evidence.

- remediation_steps must contain practical
  AWS/application remediation actions.

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