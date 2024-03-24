import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def clean(text):
  # clean text for creating a folder
  return "".join(c if c.isalnum() else "_" for c in text)


def main():
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request(),"url")
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages',[])
    if not messages:
      print('No messages found.')
    else:
      dict = {

      }
      for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()

        payload = msg['payload']
        parts = payload['parts']
        headers = payload['headers']
        container = clean(headers[3]['value'])
        dict[container] = {}


        for header in headers:
          if header['name'] == 'From':
            dict[container]['from'] = container
          if header['name'] == 'Date':
            dict[container]['date'] = header['value']
          if header['name'] == 'Subject':
            dict[container]['Subject'] = header['value']
          if header['name'] == 'To':
            dict[container]['To'] = header['value']
        for part in parts:
          if part['mimeType'] == 'text/plain':
            dict[container]['email'] = base64.urlsafe_b64decode(part['body']['data']).decode()

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()