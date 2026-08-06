class LogClassificationService:
    """
    Classifies logs by importance before AI analysis.
    """

    IMPORTANT_LEVELS = {
        "ERROR",
        "WARN",
        "WARNING",
        "CRITICAL",
        "FATAL"
    }

    def classify_logs(self, logs: list) -> dict:
        """
        Split logs into important and informational logs.
        """

        important_logs = []
        ignored_logs = []

        for log in logs:

            upper_log = log.upper()

            if any(
                level in upper_log
                for level in self.IMPORTANT_LEVELS
            ):
                important_logs.append(log)

            else:
                ignored_logs.append(log)

        return {
            "important_logs": important_logs,
            "ignored_logs": ignored_logs,
            "important_count": len(important_logs),
            "ignored_count": len(ignored_logs),
            "total_logs": len(logs)
        }

    def classify_incident(self, issues: list) -> str:
        """
        Determine the overall incident category.
        """

        issue_text = " ".join(issues).lower()

        if "database" in issue_text:
            return "Database"

        if "lambda" in issue_text:
            return "Lambda"

        if "cpu" in issue_text:
            return "Compute"

        if "memory" in issue_text:
            return "Compute"

        if "network" in issue_text:
            return "Network"

        if "dns" in issue_text:
            return "Network"

        if "permission" in issue_text:
            return "Security"

        if "authentication" in issue_text:
            return "Security"

        if "api gateway" in issue_text:
            return "API"

        return "General"