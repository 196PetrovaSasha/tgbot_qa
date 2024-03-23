from config.conf import CREDS_WAY, TABLE_ID, SHEET_ID

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from question import questions


def get_service():
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    creds_service = ServiceAccountCredentials.from_json_keyfile_name(CREDS_WAY, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


def get_table():
    return get_service().spreadsheets().values().batchGet(spreadsheetId=TABLE_ID, ranges=[SHEET_ID]).execute()


def get_data():
    return get_table()['valueRanges'][0]['values'][1:]


def push_questions():
    body = {
        'valueInputOption': 'RAW',
        'data': [{'range': f'{SHEET_ID}!A{questions[i].line}', 'values': [questions[i].to_table()]} for i in questions]
    }
    get_service().spreadsheets().values().batchUpdate(spreadsheetId=TABLE_ID, body=body).execute()
