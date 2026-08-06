import os


AWS_REGION = os.getenv(
    "AWS_REGION",
    "us-east-1"
)

BEDROCK_MODEL_ID = os.getenv(
    "BEDROCK_MODEL_ID",
    "amazon.nova-lite-v1:0"
)

INVESTIGATION_TABLE_NAME = os.getenv(
    "INVESTIGATION_TABLE_NAME",
    "AIOpsInvestigations"
)

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)