class RuleEngine:
    """
    Simple rule-based incident detector.
    """

    RULES = {
        "timeout": "Lambda Timeout",
        "connection refused": "Database Connectivity",
        "access denied": "IAM Permission Issue",
        "out of memory": "Memory Pressure",
        "throttling": "API Rate Limiting"
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