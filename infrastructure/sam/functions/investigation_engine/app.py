import json
import uuid

from shared.response import success_response, error_response
from shared.validator import validate_request
from shared.logger import log_info, log_error


def lambda_handler(event, context):
    """
    Entry point for the Investigation Engine Lambda.
    """

    try:
        body = json.loads(event.get("body", "{}"))

        # Log the incoming request
        log_info(
            "Request received",
            log_count=len(body.get("logs", []))
        )

        # Validate the request payload
        is_valid, error = validate_request(body)

        if not is_valid:
            log_error(
                "Request validation failed",
                reason=error
            )
            return error_response(error, 400)

        log_info("Request validation successful")

        incident_id = body.get(
            "incident_id",
            f"INC-{uuid.uuid4().hex[:8].upper()}"
        )

        log_info(
            "Incident ID generated",
            incident_id=incident_id
        )

        logs = body.get("logs", [])

        response = {
            "status": "success",
            "incident_id": incident_id,
            "analysis_mode": "mock",
            "received_logs": len(logs),
            "message": "Logs received successfully"
        }

        log_info(
            "Returning success response",
            incident_id=incident_id
        )

        return success_response(response)

    except Exception as error:
        log_error(
            "Unhandled exception",
            error=str(error)
        )

        return error_response(str(error), 500)