from datetime import datetime
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import os
from django.conf import settings

def get_calendar_service():
    creds = Credentials.from_service_account_file(settings.GOOGLE_CALENDAR_CREDENTIALS, scopes=['https://www.googleapis.com/auth/calendar'])
    service = build('calendar', 'v3', credentials=creds)
    return service

def fetch_holidays(start_date, end_date):
    # Converte start_date e end_date para datetime.date se forem strings
    if isinstance(start_date, str):
        start_date = datetime.fromisoformat(start_date).date()
    if isinstance(end_date, str):
        end_date = datetime.fromisoformat(end_date).date()

    # Formata as datas para o padrão RFC3339
    start_date_rfc3339 = start_date.isoformat() + 'T00:00:00Z'
    end_date_rfc3339 = end_date.isoformat() + 'T00:00:00Z'

    # Obtém o serviço do Google Calendar
    service = get_calendar_service()

    # Faz a requisição para a API do Google Calendar
    events_result = service.events().list(
        calendarId='primary',
        timeMin=start_date_rfc3339,
        timeMax=end_date_rfc3339,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    # Extrai os feriados dos eventos retornados
    events = events_result.get('items', [])
    holidays = [event['start'].get('date') for event in events if 'date' in event['start']]

    return holidays
