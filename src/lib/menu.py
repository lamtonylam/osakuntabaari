from datetime import datetime
from ics import Calendar, Event



def create_menu_calendar(menu):
    calendar = Calendar()
    
    for date, food in menu.items():
        # Format the date
        date_stripped = date.split()[1] + str(datetime.now().year)
        datetime_object = datetime.strptime(date_stripped, '%d.%m.%Y')
        
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