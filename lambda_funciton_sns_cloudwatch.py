import json
import boto3
import datetime

sns_client = boto3.client('sns')
cloudwatch_client = boto3.client('cloudwatch')

def lambda_handler(event, context):
    intent_name = event['sessionState']['intent']['name']
    
    if intent_name == 'ReportIncident':
        return handle_report_incident(event)
    elif intent_name == 'GetIncidentStatus':
        return handle_get_incident_status(event)
    elif intent_name == 'ResolveIncident':
        return handle_resolve_incident(event)
    else:
        return close_response("Sorry, I didn't understand that intent.")

def handle_report_incident(event):
    slots = event['sessionState']['intent']['slots']
    incident_type = slots['IncidentType']['value']['interpretedValue']
    severity = slots['Severity']['value']['interpretedValue']
    description = slots['Description']['value']['interpretedValue']
    
    message = f"New Incident Reported:\nType: {incident_type}\nSeverity: {severity}\nDescription: {description}"
    
    # Publish to SNS
    sns_client.publish(
        TopicArn='arn:aws:sns:us-east-1:123456789012:IncidentAlerts',
        Message=message,
        Subject='New Incident Reported'
    )
    
    return close_response("Incident reported successfully. The team has been notified.")

def handle_get_incident_status(event):
    # Placeholder for fetching incident status
    return close_response("The incident is currently being investigated.")

def handle_resolve_incident(event):
    # Placeholder for resolving incident
    return close_response("The incident has been marked as resolved.")

def close_response(message):
    return {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                "name": "ReportIncident",
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": message
            }
        ]
    }
