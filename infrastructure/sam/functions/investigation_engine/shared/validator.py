def validate_request(body):
    """
    Validate the incoming manual log investigation request.

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


def validate_cloudwatch_request(body):
    """
    Validate a CloudWatch investigation request.

    Expected payload:

    {
        "log_group_name": "/aws/lambda/example",
        "minutes": 15
    }

    Returns:
        (is_valid, error_message)
    """

    if not isinstance(body, dict):
        return False, "Request body must be a JSON object."

    if "log_group_name" not in body:
        return False, "'log_group_name' field is required."

    log_group_name = body["log_group_name"]

    if not isinstance(log_group_name, str):
        return False, "'log_group_name' must be a string."

    if not log_group_name.strip():
        return False, "'log_group_name' cannot be empty."

    minutes = body.get("minutes", 15)

    if not isinstance(minutes, int):
        return False, "'minutes' must be an integer."

    if minutes < 1 or minutes > 60:
        return False, "'minutes' must be between 1 and 60."

    return True, None