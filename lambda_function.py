import boto3
import json

sns = boto3.client('sns')

def lambda_handler(event, context):
    intent = event['sessionState']['intent']['name']

    if intent == 'ReportIncident':
        return report_incident(event)
    elif intent == 'CheckIncidentStatus':
        return check_status(event)
    elif intent == 'ResolveIncident':
        return resolve_incident(event)
    else:
        return close_response("Unrecognized intent")

def report_incident(event):
    message = "New incident reported via chatbot. Please investigate."
    sns.publish(
        TopicArn='arn:aws:sns:us-west-1:123456789012:IncidentAlerts',
        Message=message
    )
    return close_response("Incident has been reported.")

def check_status(event):
    return close_response("Incident is currently being investigated.")

def resolve_incident(event):
    return close_response("Incident has been marked as resolved.")

def close_response(message):
    return {
        "sessionState": {"dialogAction": {"type": "Close"}},
        "messages": [{"contentType": "PlainText", "content": message}]
    }
