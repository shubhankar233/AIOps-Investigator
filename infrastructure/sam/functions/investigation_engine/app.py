import json
import uuid


from shared.response import success_response, error_response
from shared.validator import (
    validate_request,
    validate_cloudwatch_request
)
from shared.logger import log_info, log_error
from services.investigation_service import InvestigationService
from repositories.investigation_repository import InvestigationRepository
from services.cloudwatch_service import CloudWatchService


service = InvestigationService()
repository = InvestigationRepository()
cloudwatch_service = CloudWatchService()

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
        # POST /api/v1/analyze/cloudwatch
        # ==========================================
        if (
            method == "POST"
            and event.get("resource") == "/api/v1/analyze/cloudwatch"
        ):

            body = json.loads(
                event.get("body", "{}")
            )

            log_info(
                "CloudWatch investigation request received"
            )

            is_valid, error = validate_cloudwatch_request(
                body
            )

            if not is_valid:

                log_error(
                    "CloudWatch request validation failed",
                    reason=error
                )

                return error_response(
                    error,
                    400
                )

            log_group_name = body[
                "log_group_name"
            ]

            minutes = body.get(
                "minutes",
                15
            )

            # Current time in milliseconds
            import time

            end_time = int(
                time.time() * 1000
            )

            start_time = end_time - (
                minutes * 60 * 1000
            )

            logs = cloudwatch_service.get_logs(
                log_group_name=log_group_name,
                start_time=start_time,
                end_time=end_time,
                limit=100
            )

            if not logs:

                return error_response(
                    "No CloudWatch logs found "
                    f"for the last {minutes} minutes.",
                    404
                )

            incident_id = (
                f"INC-{uuid.uuid4().hex[:8].upper()}"
            )

            analysis = service.analyze(
                incident_id=incident_id,
                logs=logs
            )

            response = {
                "status": "success",
                "incident_id": incident_id,
                "source": "cloudwatch",
                "log_group_name": log_group_name,
                "time_window_minutes": minutes,
                "received_logs": len(logs),
                **analysis
            }

            log_info(
                "CloudWatch investigation completed",
                incident_id=incident_id,
                log_count=len(logs)
            )

            return success_response(
                response
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