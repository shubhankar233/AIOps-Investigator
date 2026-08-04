import os
import boto3
from typing import Any, cast

from shared.logger import log_info, log_error


class InvestigationRepository:
    """
    Handles persistence of incident investigations in DynamoDB.
    """

    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb")

        table_name = os.environ["INVESTIGATION_TABLE_NAME"]

        self.table = self.dynamodb.Table(table_name)

    def save_investigation(
        self,
        incident_id: str,
        logs: list,
        analysis: dict
    ) -> None:
        """
        Store an investigation result in DynamoDB.
        """

        item = {
            "incident_id": incident_id,
            "logs": logs,
            "analysis": analysis
        }

        try:
            self.table.put_item(Item=item)

            log_info(
                "Investigation saved",
                incident_id=incident_id
            )

        except Exception as error:
            log_error(
                "Failed to save investigation",
                incident_id=incident_id,
                error=str(error)
            )

            raise

    def get_investigation(
        self,
        incident_id: str
    ) -> dict | None:
        """
        Retrieve a previously stored investigation
        from DynamoDB by incident ID.
        """

        try:
            response = self.table.get_item(
                Key={
                    "incident_id": incident_id
                }
            )

            response_dict = cast(
                dict[str, Any],
                response
            )

            item = response_dict.get("Item")

            if item:
                log_info(
                    "Investigation retrieved",
                    incident_id=incident_id
                )

                return cast(
                    dict,
                    item
                )

            log_info(
                "Investigation not found",
                incident_id=incident_id
            )

            return None

        except Exception as error:
            log_error(
                "Failed to retrieve investigation",
                incident_id=incident_id,
                error=str(error)
            )

            raise

    def list_investigations(self) -> list:
        """
        Retrieve all stored investigations from DynamoDB.
        """

        try:
            response = self.table.scan()

            response_dict = cast(
                dict[str, Any],
                response
            )

            investigations = response_dict.get(
                "Items",
                []
            )

            log_info(
                "Investigations retrieved",
                count=len(investigations)
            )

            return cast(
                list,
                investigations
            )

        except Exception as error:
            log_error(
                "Failed to retrieve investigations",
                error=str(error)
            )

            raise

    def find_similar_investigations(
        self,
        issues: list,
        current_incident_id: str
    ) -> list:
        """
        Find and rank previous investigations based on
        overlapping detected issues.
        """

        try:
            response = self.table.scan()

            response_dict = cast(
                dict[str, Any],
                response
            )

            investigations = response_dict.get(
                "Items",
                []
            )

            ranked_investigations = []

            current_issues = set(issues)

            for investigation_item in investigations:

                investigation = cast(
                    dict[str, Any],
                    investigation_item
                )

                # Don't compare the incident with itself
                if investigation.get(
                    "incident_id"
                ) == current_incident_id:
                    continue

                analysis = cast(
                    dict[str, Any],
                    investigation.get(
                        "analysis",
                        {}
                    )
                )

                previous_root_causes = cast(
                    list,
                    analysis.get(
                        "root_cause",
                        []
                    )
                )

                previous_issues = set(
                    previous_root_causes
                )

                # Calculate overlap
                matching_issues = (
                    current_issues &
                    previous_issues
                )

                if not matching_issues:
                    continue

                # Similarity score
                similarity_score = (
                    len(matching_issues)
                    / max(len(current_issues), 1)
                )

                ranked_investigations.append(
                    {
                        "investigation": investigation,
                        "similarity_score": similarity_score,
                        "matching_issues": list(
                            matching_issues
                        )
                    }
                )

            # Highest similarity first
            ranked_investigations.sort(
                key=lambda item: item[
                    "similarity_score"
                ],
                reverse=True
            )

            # Return only the top 5
            top_matches = ranked_investigations[:5]

            similar_investigations = []

            for match in top_matches:

                investigation = match[
                    "investigation"
                ]

                # Add retrieval metadata
                investigation[
                    "similarity_score"
                ] = match[
                    "similarity_score"
                ]

                investigation[
                    "matching_issues"
                ] = match[
                    "matching_issues"
                ]

                similar_investigations.append(
                    investigation
                )

            log_info(
                "Similar investigations ranked",
                count=len(similar_investigations)
            )

            return similar_investigations

        except Exception as error:

            log_error(
                "Failed to find similar investigations",
                error=str(error)
            )

            raise