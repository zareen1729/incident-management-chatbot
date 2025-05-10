# Incident Management Chatbot

This project implements a serverless chatbot for incident management using AWS services.

## Features

- Report new incidents via chat
- Notify incident response team through SNS
- Monitor system metrics with CloudWatch
- Integrate alerts into Slack or Microsoft Teams

## Setup Instructions

1. Deploy the Lambda function using AWS Console or AWS CLI.
2. Create and configure the Amazon Lex bot with the provided configuration.
3. Set up the SNS topic and subscriptions.
4. Configure CloudWatch alarms to trigger SNS notifications.
5. Integrate AWS Chatbot with your preferred chat platform.

## Requirements

- AWS Account
- AWS CLI configured
- Permissions to create and manage AWS Lambda, Lex, SNS, and CloudWatch resources
