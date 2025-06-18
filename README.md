# Flask Login Monitor – Azure Threat Detection Lab

## Overview

This project demonstrates a basic Flask web application deployed to Azure App Service with integrated logging, monitoring, and alerting using Azure Monitor, Log Analytics, and KQL. The purpose is to simulate and detect brute-force login attempts and trigger an alert via email.

## What I Learned

Throughout this lab, I learned how to:

* Deploy a Python Flask application to Azure App Service.
* Enable diagnostic logging and route logs to a Log Analytics Workspace.
* Use Kusto Query Language (KQL) to extract insights from application logs.
* Create and configure alert rules in Azure Monitor based on log events.
* Set up an action group to notify via email when suspicious login activity is detected.

## Challenges Faced

There were several debugging steps and issues I encountered:

* Initially, I did not configure the **startup command** for the Flask app, causing deployment issues. I fixed this using a custom startup command: `gunicorn app:app`.
* When testing login attempts locally, logs weren't printing—this was due to cached processes, and restarting the Flask server fixed the issue.
* On Azure, **AppServiceConsoleLogs** did not appear at first. It took multiple test requests and time delays before logs started showing consistently in Log Analytics.
* Configuring the **alert rule** was tricky due to:

  * No results initially showing in the query preview.
  * The need to select **“Aggregated logs”** instead of **“Single event.”**
  * Logs appearing only after 2–3 repeated failed login attempts.
  * Needing to wait several minutes before alerts were evaluated and triggered.
* I also had to ensure my alert query measured **row count** and correctly used `ResultDescription`.

Despite these hurdles, the alert eventually triggered and sent an email, completing the pipeline from deployment to detection.

## KQL Query Used for Alert Condition

```kql
AppServiceConsoleLogs
| where TimeGenerated > ago(5m)
| where ResultDescription has "Failed login attempt by user:"
```

This query looks at the AppServiceConsoleLogs over the past 5 minutes and filters for any log messages that contain the string indicating a failed login attempt.

## Video Demo

YouTube Link: [https://youtu.be/3yjmmOvlp3w](https://youtu.be/3yjmmOvlp3w)

### Demo Coverage:

* App deployed on Azure
* Log generation via simulated failed login attempts
* Log inspection in Azure Monitor
* KQL query usage in Log Analytics
* Alert rule creation and successful trigger with email notification
