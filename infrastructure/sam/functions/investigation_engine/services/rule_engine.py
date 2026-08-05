class RuleEngine:
    """
    Simple rule-based incident detector.
    """

    RULES = {
        # Lambda / execution issues
        "timeout": "Lambda Timeout",
        "timed out": "Lambda Timeout",
        "execution exceeded": "Lambda Timeout",

        # Database connectivity issues
        "connection refused": "Database Connectivity",
        "connection timeout": "Database Connectivity",
        "database connection": "Database Connectivity",
        "database timeout": "Database Connectivity",
        "unable to connect to database": "Database Connectivity",
        "failed to connect to database": "Database Connectivity",

        # IAM issues
        "access denied": "IAM Permission Issue",
        "not authorized": "IAM Permission Issue",
        "unauthorized": "IAM Permission Issue",

        # Memory issues
        "out of memory": "Memory Pressure",
        "memory limit exceeded": "Memory Pressure",
        "memory usage exceeded": "Memory Pressure",

        # API throttling
        "throttling": "API Rate Limiting",
        "rate exceeded": "API Rate Limiting",
        "too many requests": "API Rate Limiting"
    }

    def analyze(self, logs: list) -> list:
        """
        Detect known issues from logs.
        """

        findings = []

        for log in logs:
            text = log.lower()

            for keyword, issue in self.RULES.items():

                if keyword in text and issue not in findings:
                    findings.append(issue)

        return findings