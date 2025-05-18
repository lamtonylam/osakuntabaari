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
        event.name = food
        event.begin = datetime_object.date()  # Set as all-day event
        event.make_all_day()
        event.description = f"{date} \n{food}"
        
        # Add the event to the calendar
        calendar.events.add(event)
        
        print(f"Added event: {date} - {food}")
    
    return calendar