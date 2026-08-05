import boto3

from shared.logger import log_info, log_error


class CloudWatchService:
    """
    Handles retrieval of application logs from Amazon CloudWatch Logs.
    """

    def __init__(self):
        self.client = boto3.client(
            "logs",
            region_name="us-east-1"
        )

    def get_logs(
        self,
        log_group_name: str,
        start_time: int,
        end_time: int,
        limit: int = 100
    ) -> list:
        """
        Retrieve log messages from CloudWatch Logs.

        start_time and end_time are Unix timestamps in milliseconds.
        """

        try:

            log_info(
                "Fetching CloudWatch logs",
                log_group=log_group_name,
                start_time=start_time,
                end_time=end_time
            )

            response = self.client.filter_log_events(
                logGroupName=log_group_name,
                startTime=start_time,
                endTime=end_time,
                limit=limit
            )

            events = response.get(
                "events",
                []
            )

            logs = []

            for event in events:

                message = event.get(
                    "message",
                    ""
                ).strip()

                if message:
                    logs.append(message)

            log_info(
                "CloudWatch logs retrieved",
                log_group=log_group_name,
                count=len(logs)
            )

            return logs

        except Exception as error:

            log_error(
                "Failed to retrieve CloudWatch logs",
                log_group=log_group_name,
                error=str(error)
            )

            raise