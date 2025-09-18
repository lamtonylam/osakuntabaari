from datetime import datetime, timedelta
from time import timezone
from ics import Calendar, Event


def format_date(date_str):
    """
    Convert date from 'Mon 01.01.' to '01.01.2024' format.
    """
    date_stripped = date_str.split()[1] + str(datetime.now().year)
    datetime_object = datetime.strptime(date_stripped, "%d.%m.%Y")
    return datetime_object


def create_menu_calendar(menu):
    calendar = Calendar()

    for date, food in menu.items():
        # Format the date
        datetime_object = format_date(date)

        # Create a new event
        event = Event()
        # Event name is the food of the day
        event.name = food
        # Event date
        event.begin = datetime_object.date()  # Set as all-day event
        event.make_all_day()
        # Event description
        event.description = f"{date} \n{food}"

        # Add the event to the calendar
        calendar.events.add(event)

    return calendar


def create_menu_calendar_timed(menu):
    calendar = Calendar()

    for date, food in menu.items():
        # Format the date
        datetime_object = format_date(date)

        # Create a new event
        event = Event()
        # Event name is the food of the day
        event.name = food
        # Event date and time (11:00 to 14:30)
        event.begin = datetime_object.replace(hour=11, minute=0)
        is_friday = datetime_object.weekday() == 4
        if is_friday:
            event.end = datetime_object.replace(hour=14, minute=30, tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=2)))
        else:
            event.end = datetime_object.replace(hour=15, minute=0, tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=2)))
        # Event description
        event.description = f"{date} \n{food}"

        # Add the event to the calendar
        calendar.events.add(event)

    return calendar
