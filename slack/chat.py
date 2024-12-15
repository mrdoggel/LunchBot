import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import env

def send(blocks, text, channel):
    client = WebClient(token=os.environ['slack_token'])
    try:
        response = client.chat_postMessage(channel=f'#{channel}', text=text, blocks=blocks)
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")
        # Also receive a corresponding status_code
        assert isinstance(e.response.status_code, int)
        print(f"Received a response status_code: {e.response.status_code}")