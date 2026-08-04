import json
from decimal import Decimal


def decimal_to_int_or_float(value):
    """
    Convert DynamoDB Decimal values into JSON-compatible
    int or float values.
    """

    if value % 1 == 0:
        return int(value)

    return float(value)


def json_serializer(value):
    """
    Custom JSON serializer for DynamoDB Decimal values.
    """

    if isinstance(value, Decimal):
        return decimal_to_int_or_float(value)

    raise TypeError(
        f"Object of type {type(value).__name__} "
        "is not JSON serializable"
    )


def success_response(data, status_code=200):
    """
    Create a standardized success response.
    """

    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(
            data,
            default=json_serializer
        )
    }


def error_response(message, status_code=400):
    """
    Create a standardized error response.
    """

    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "status": "error",
            "message": message
        })
    }