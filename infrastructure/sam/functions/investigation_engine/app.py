import json
import uuid


from shared.response import success_response, error_response
from shared.validator import validate_request
from shared.logger import log_info, log_error
from services.investigation_service import InvestigationService
from repositories.investigation_repository import InvestigationRepository


service = InvestigationService()
repository = InvestigationRepository()


def lambda_handler(event, context):
# def lambda_handler(event: dict[str, Any], context: Any):
    """
    Entry point for the Investigation Engine Lambda.
    """

    try:
        # Get HTTP method and path parameters
        method = event.get("httpMethod")
        path_parameters = event.get("pathParameters") or {}

        # ==========================================
        # GET /api/v1/investigations
        # GET /api/v1/investigations/{incident_id}
        # ==========================================
        if method == "GET":

            incident_id = path_parameters.get("incident_id")

            # ------------------------------------------
            # Get a single investigation
            # GET /api/v1/investigations/{incident_id}
            # ------------------------------------------
            if incident_id:

                investigation = repository.get_investigation(
                    incident_id
                )

                if not investigation:
                    return error_response(
                        "Investigation not found",
                        404
                    )

                return success_response(
                    investigation
                )

            # ------------------------------------------
            # Get investigation history
            # GET /api/v1/investigations
            # ------------------------------------------
            investigations = service.list_investigations()

            return success_response(
                investigations
            )

        # ==========================================
        # POST /api/v1/analyze
        # ==========================================
        body = json.loads(
            event.get("body", "{}")
        )

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

            return error_response(
                error,
                400
            )

        log_info(
            "Request validation successful"
        )

        incident_id = body.get(
            "incident_id",
            f"INC-{uuid.uuid4().hex[:8].upper()}"
        )

        log_info(
            "Incident ID generated",
            incident_id=incident_id
        )

        logs = body.get(
            "logs",
            []
        )

        analysis = service.analyze(
            incident_id=incident_id,
            logs=logs
        )

        response = {
            "status": "success",
            "incident_id": incident_id,
            "received_logs": len(logs),
            **analysis
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

        return error_response(
            str(error),
            500
        )