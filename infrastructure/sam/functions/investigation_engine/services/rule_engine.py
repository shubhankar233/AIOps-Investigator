class RuleEngine:
    """
    Rule-based incident detector.

    Detects known infrastructure/application issues and
    preserves the log evidence that triggered each finding.
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
        "too many requests": "API Rate Limiting",

        # API errors
        "502": "API Gateway Error",
        "bad gateway": "API Gateway Error",
        "503": "Service Unavailable",
        "service unavailable": "Service Unavailable",
        "504": "Gateway Timeout",
        "gateway timeout": "Gateway Timeout",

        # Authentication
        "authentication failed": "Authentication Failure",
        "invalid credentials": "Authentication Failure",
        "login failed": "Authentication Failure",

        # Network
        "connection reset": "Network Connectivity",
        "network unreachable": "Network Connectivity",
        "host unreachable": "Network Connectivity",
        "dns": "DNS Resolution Issue",
        "name resolution": "DNS Resolution Issue",
    }

    def analyze(self, logs: list) -> list:
        """
        Detect known issues from logs.

        Returns a unique list of detected issue names.
        """

        findings = []

        for log in logs:

            if not isinstance(log, str):
                continue

            text = log.lower()

            for keyword, issue in self.RULES.items():

                if keyword in text and issue not in findings:
                    findings.append(issue)

        return findings

    def analyze_with_evidence(self, logs: list) -> list:
        """
        Detect issues and preserve the log evidence
        that triggered each finding.
        """

        evidence = []

        for log in logs:

            if not isinstance(log, str):
                continue

            text = log.lower()

            for keyword, issue in self.RULES.items():

                if keyword in text:

                    existing = next(
                        (
                            item
                            for item in evidence
                            if item["issue"] == issue
                        ),
                        None
                    )

                    if existing is None:

                        evidence.append(
                            {
                                "issue": issue,
                                "keyword": keyword,
                                "log": log
                            }
                        )

                    elif log not in [
                        item["log"]
                        for item in evidence
                        if item["issue"] == issue
                    ]:

                        # Keep evidence limited.
                        issue_entries = [
                            item
                            for item in evidence
                            if item["issue"] == issue
                        ]

                        if len(issue_entries) < 3:
                            evidence.append(
                                {
                                    "issue": issue,
                                    "keyword": keyword,
                                    "log": log
                                }
                            )

        return evidence