#!/usr/bin/env python

# Copyright 2021 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Analytics Data API sample quickstart application.

This application demonstrates the usage of the Analytics Data API using
service account credentials from a JSON file downloaded from
the Google Cloud Console.

Before you start the application, please review the comments starting with
"TODO(developer)" and update the code to use correct values.

Usage:
  pip3 install --upgrade google-analytics-data
  python3 quickstart_json_credentials.py
"""
# [START analyticsdata_json_credentials_quickstart]
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)


def sample_run_report(property_id="YOUR-GA4-PROPERTY-ID", credentials_json_path=""):
    """Runs a simple report on a Google Analytics 4 property."""
    # TODO(developer): Uncomment this variable and replace with your
    #  Google Analytics 4 property ID before running the sample.
    # property_id = "YOUR-GA4-PROPERTY-ID"

    # [START analyticsdata_json_credentials_initialize]
    # TODO(developer): Uncomment this variable and replace with a valid path to
    #  the credentials.json file for your service account downloaded from the
    #  Cloud Console.
    # credentials_json_path = "/path/to/credentials.json"

    # Explicitly use service account credentials by specifying
    # the private key file.
    client = BetaAnalyticsDataClient().from_service_account_json(credentials_json_path)
    # [END analyticsdata_json_credentials_initialize]

    # [START analyticsdata_json_credentials_run_report]
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="city")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="2020-03-31", end_date="today")],
    )
    response = client.run_report(request)
    # [END analyticsdata_json_credentials_run_report]

    print("Report result:")
    for row in response.rows:
        print(row.dimension_values[0].value, row.metric_values[0].value)


# [END analyticsdata_json_credentials_quickstart]


if __name__ == "__main__":
    sample_run_report()
