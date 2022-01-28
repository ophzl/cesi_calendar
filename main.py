import json
import sys

from Classes.Calendar import Calendar
from Classes.Course import Course
from api import calendar

gcalendar_service = calendar.get_service()


def main(filename):
    print("====== 1. TRY TO RETRIEVE CESI CALENDAR OR CREATE IF NOT EXISTS ======")
    calendar_id = try_get_calendar()
    print("====== 2. RETRIEVING DATA FROM RESOURCES FOLDER ======")
    with open(filename, "r") as file:
        try:
            data = json.loads(file.read())
            courses = data['courses']
            for month in courses:
                for key, values in month.items():
                    for elem in values:
                        course = Course(elem)
                        try_add_event(calendar_id, course.__dict__)
        except:
            print("Error while attempting to load json data.")


def try_get_calendar():
    try:
        get_calendars_list = gcalendar_service.calendarList().list().execute()

        for elem in get_calendars_list['items']:
            if elem['summary'] == "CESI":
                print("\tCESI calendar already existing, skipping this step")
                return elem['id']

        print("\tCESI calendar not found, new one created")
        cesi_calendar = Calendar()
        gcalendar_created = gcalendar_service.calendars().insert(body=cesi_calendar.__dict__).execute()

        return gcalendar_created['id']

    except:
        print("\tEXCEPTION: Error while attempting to get/create CESI calendar.")


def try_add_event(calendar_id, event):
    try:
        get_events = gcalendar_service.events().list(calendarId=calendar_id, timeMin=event['start']['dateTime'],
                                                     timeMax=event['end']['dateTime']).execute()
        if len(get_events['items']) == 0:
            gcalendar_service.events().insert(calendarId=calendar_id, body=event).execute()
            print("\tNew event created")
        else:
            print("\tCannot create an event while one is already existing on date " + get_events['items'][0]['start']['dateTime'])
    except:
        print("\tEXCEPTION: Error while attempting to add new event to calendar.")


if __name__ == "__main__":
    main(sys.argv[1])
