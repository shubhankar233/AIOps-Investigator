import json


def success_response(data, status_code=200):
    """
    Create a standardized success response.
    """

    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(data)
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