import json
import requests
import os

url  = os.getenv("webhookUrl")


def handler(event, context):
    try:
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        data = event["Records"][0]["Sns"]
        print(data)
        content = {}
        content["subject"] = data["Subject"]
        content["message"] = data["Message"]
        content["timestamp"] = data["Timestamp"]
        print(content)
        data = {
            "username":"server-alerts",
            "content":json.dumps(content)
        }
        requests.post(url, data=data)

        body = {
            "message": "Message send!",
        }
        return response
    except Exception as ex:
        print(f"exception -->>> {ex}")
    
