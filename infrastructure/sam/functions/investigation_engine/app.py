import json
import uuid

from shared.response import success_response, error_response
from shared.validator import validate_request


def lambda_handler(event, context):
    """
    Entry point for the Investigation Engine Lambda.
    """

    try:
        body = json.loads(event.get("body", "{}"))

        # Validation of the request payload
        is_valid, error = validate_request(body)

        if not is_valid:
            return error_response(error, 400)

        incident_id = body.get(
            "incident_id",
            f"INC-{uuid.uuid4().hex[:8].upper()}"
        )

        logs = body.get("logs", [])

        response = {
            "status": "success",
            "incident_id": incident_id,
            "analysis_mode": "mock",
            "received_logs": len(logs),
            "message": "Logs received successfully"
        }

        return success_response(response)

    except Exception as error:
        return error_response(str(error), 500)