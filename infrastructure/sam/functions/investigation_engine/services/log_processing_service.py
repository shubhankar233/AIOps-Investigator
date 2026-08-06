class LogProcessingService:
    """
    Handles preprocessing of application logs
    before they are sent to the AI engine.
    """

    @staticmethod
    def remove_duplicate_logs(logs):
        """
        Removes duplicate log entries while
        preserving the original order.
        """

        seen = set()
        cleaned_logs = []

        for log in logs:
            if log not in seen:
                cleaned_logs.append(log)
                seen.add(log)

        return cleaned_logs

    @staticmethod
    def remove_noise_logs(logs: list) -> list:
        """
        Remove low-value log entries before AI analysis.
        """

        ignored_prefixes = [
            "INFO",
            "DEBUG",
            "TRACE"
        ]

        filtered_logs = []

        for log in logs:

            upper_log = log.upper()

            if any(
                upper_log.startswith(prefix)
                for prefix in ignored_prefixes
            ):
                continue

            filtered_logs.append(log)

        return filtered_logs