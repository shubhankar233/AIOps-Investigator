class RuleEngine:
    """
    Rule-based incident detector.

    Detects known infrastructure/application issues and
    preserves the log evidence that triggered each finding.
    """    
    RULES = {
        # Lambda / execution issues
        "lambda timeout": "Lambda Timeout",
        "lambda timed out": "Lambda Timeout",
        "lambda execution timeout": "Lambda Timeout",
        "execution exceeded": "Lambda Timeout",
        "function timed out": "Lambda Timeout",

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

        # CPU issues
        "cpu limit exceeded": "CPU Pressure",
        "cpu usage exceeded": "CPU Pressure",
        "high cpu usage": "CPU Pressure",
        "cpu utilization exceeded": "CPU Pressure",
        "cpu throttling": "CPU Pressure",

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

    HIGH_SEVERITY_ISSUES = {
        "Lambda Timeout",
        "Database Connectivity",
        "IAM Permission Issue",
        "Memory Pressure",
        "API Gateway Error",
        "Service Unavailable",
        "Gateway Timeout",
        "Network Connectivity",
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

        # def determine_severity(self, findings: list) -> str:
        #         """
        #         Determine incident severity based on detected issues.
        #         """
    
        #         if not findings:
        #             return "LOW"
    
        #         if any(
        #             issue in self.HIGH_SEVERITY_ISSUES
        #             for issue in findings
        #         ):
        #             return "HIGH"
    
        #         return "MEDIUM"

        

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

    def determine_severity(self, findings: list) -> str:
            """
            Determine incident severity based on detected issue types.

            The most severe detected issue determines the
            overall incident severity.
            """

            if not findings:
                return "LOW"

            high_severity_issues = {
                "Lambda Timeout",
                "Database Connectivity",
                "IAM Permission Issue",
                "Memory Pressure",
                "CPU Pressure",
                "API Rate Limiting",
                "API Gateway Error",
                "Service Unavailable",
                "Gateway Timeout",
                "Network Connectivity",
                "DNS Resolution Issue",
            }

            medium_severity_issues = {
                "Authentication Failure",
            }

            for finding in findings:
                if finding in high_severity_issues:
                    return "HIGH"

            for finding in findings:
                if finding in medium_severity_issues:
                    return "MEDIUM"

            return "LOW"