def validate_request(body):
    """
    Validate the incoming request payload.

    Returns:
        (is_valid, error_message)
    """

    if not isinstance(body, dict):
        return False, "Request body must be a JSON object."

    if "logs" not in body:
        return False, "'logs' field is required."

    logs = body["logs"]

    if not isinstance(logs, list):
        return False, "'logs' must be a list."

    if len(logs) == 0:
        return False, "'logs' cannot be empty."

    return True, None