# import base64
# import json
# import os
#
# info = None
#
# with open('returneddata.json','r') as info:
#     info = json.load(info)
#
# def check_duplicate_value(value,dictionary):
#     if dictionary.get(value) is not None:
#         return True
#     else:
#         return False
# def clean(text,noSpace):
#   # clean text for creating a folder
#   if(noSpace):
#     return "".join(c if c.isalnum() else "" for c in text)
#   else:
#       return "".join(c if c.isalnum() else "_" for c in text)
#
#
# # print(json.dumps(data, indent=4))
#
#
#
# dict = {
#
# }
# # print(json.dumps(info, indent=4))
#
# for data in info:
#     headers = data['headers']
#     parts = data['parts']
#
#     # print(json.dumps(headers,indent=4))
#
#     for header in headers:
#         if header['name'] == 'Return-Path':
#
#             parentPath_email = clean(header['value'],True)
#             cleanEmailAndStore = header['value'].split('<',2)[1].split('>')[0]
#             subject = clean(headers[19]['value'], True)
#
#             if check_duplicate_value(parentPath_email,dict):
#                 dict[parentPath_email][subject] = {}
#                 dict[parentPath_email][subject]['From'] = cleanEmailAndStore
#             else:
#
#                 dict[parentPath_email] = {}
#                 dict[parentPath_email][subject] = {}
#                 dict[parentPath_email][subject]['From'] = cleanEmailAndStore
#         if header['name'] == 'From':
#             dict[parentPath_email][subject]['nameOfSender'] = header['value'].split('<')[0]
#         if header['name'] == 'Date':
#             dict[parentPath_email][subject]['date'] = header['value']
#         if header['name'] == 'To':
#             dict[parentPath_email][subject]['To'] = header['value']
#     for part in parts:
#         if part['mimeType'] == 'text/plain':
#             dict[parentPath_email][subject]['email/text'] = base64.urlsafe_b64decode(part['body']['data']).decode()
#     # print(json.dumps(dict, indent=4))
#
#
