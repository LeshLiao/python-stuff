import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
import requests

# Define the FCM scope for OAuth 2.0
SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']

def _get_access_token():
    """Retrieve a valid access token that can be used to authorize requests.
    :return: Access token.
    """
    # Load the service account credentials
    credentials = service_account.Credentials.from_service_account_file(
       'palettex-37930-firebase-adminsdk-6hnye-d95f9e7f80.json', scopes=SCOPES)

    # credentials = service_account.Credentials.from_service_account_file(
    #    'google-services.json', scopes=SCOPES)

    # Refresh the credentials to get the access token
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)

    # Return the access token
    return credentials.token


def send_fcm_message(token, payload):
    """Send an FCM message using the OAuth 2.0 token."""
    access_token = _get_access_token()

    # FCM endpoint
    url = 'https://fcm.googleapis.com/v1/projects/palettex-37930/messages:send'

    # Headers for the HTTP request
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # Create the FCM message body
    body = {
        "message": {
            "token": token,  # FCM device token
            "notification": {
                "title": "Test Notification",
                "body": "This is a test message"
            },
            "data": payload  # Add any custom data here
        }
    }

    # Send the POST request to FCM
    response = requests.post(url, headers=headers, json=body)

    # Print response for debugging
    if response.status_code == 200:
        print("Message sent successfully:", response.json())
    else:
        print("Failed to send message:", response.status_code, response.text)


if __name__ == "__main__":
    # Replace with a valid FCM token and message payload
    fcm_token = "cqPsnjZwTG6XqdioRsRMzd:APA91bFM5TgkZEeP1q0CQPrBb08JffGEtk2yNtjI1b44_hyHFDxgAYtDVcTC-G1NR6FjMf7Qa9jaLcseIV-14QumJjOXZrVw3Y1IMH76I64dUFfr7r02GOcZqTOWaILWv3Foj56HKq5K"
    custom_payload = {"key": "value"}

    # Send the message
    send_fcm_message(fcm_token, custom_payload)