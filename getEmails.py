import json

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
import os
import base64
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def clean(text,noSpace):
  # clean text for creating a folder
  if(noSpace):
    return "".join(c if c.isalnum() else "" for c in text)
  else:
      return "".join(c if c.isalnum() else "_" for c in text)

def check_duplicate_value(value,dictionary):
    if dictionary.get(value) is not None:
        return True
    else:
        return False
def getEmail_json():
    try:
        dict = {

        }
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        service = build('gmail', 'v1', credentials=creds)
        result = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
        messages = result.get('messages',[])
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


            for header in headers:
                if header['name'] == 'Return-Path':
                    parentPath_email = clean(header['value'], True)
                    cleanEmailAndStore = header['value'].split('<', 2)[1].split('>')[0]
                    subject = clean(headers[19]['value'], True)

                    if check_duplicate_value(parentPath_email, dict):
                        dict[parentPath_email][subject] = {}
                        dict[parentPath_email][subject]['From'] = cleanEmailAndStore
                    else:

                        dict[parentPath_email] = {}
                        dict[parentPath_email][subject] = {}
                        dict[parentPath_email][subject]['From'] = cleanEmailAndStore

                    dict[parentPath_email][subject]['threadId'] = message['id']
                if header['name'] == 'From':
                    dict[parentPath_email][subject]['nameOfSender'] = header['value'].split('<')[0]
                if header['name'] == 'Date':
                    dict[parentPath_email][subject]['date'] = header['value']
                if header['name'] == 'To':
                    dict[parentPath_email][subject]['To'] = header['value']
            for part in parts:
                if part['mimeType'] == 'text/plain':
                    dict[parentPath_email][subject]['email/text'] = base64.urlsafe_b64decode(
                        part['body']['data']).decode()


        if os.path.isfile('token.json'):
            os.remove('token.json')
        with open('emails.json', 'w') as file:
         file.write(json.dumps(dict,indent=4))
        return
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")

