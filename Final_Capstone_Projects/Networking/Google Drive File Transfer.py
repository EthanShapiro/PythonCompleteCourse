from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os

SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET = 'client_secret.json'

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
    creds = tools.run_flow(flow, store, flags) \
        if flags else tools.run(flow, store)

DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

FILES = (
    ('hello.txt', None),
    ('hello.txt', 'application/vnd.google-apps.document')
)

for filename, mime_type in FILES:
    meta_data = {'name': filename}
    if mime_type:
        meta_data['mimeType'] = mime_type
    res = DRIVE.files().create(body=meta_data, media_body=filename).execute()
    if res:
        print('Uploaded {0} ({1})'.format(filename, res['mimeType']))

if res:
    MIMETYPE = 'application/pdf'
    res, data = DRIVE.files().export(res['id'], MIMETYPE).execute()