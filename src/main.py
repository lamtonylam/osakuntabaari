from lib.hamis_data import get_weeks_menu
from lib.menu import create_menu_calendar
from datetime import datetime
from ics import Calendar, Event
import os
import sys
import uvicorn
from fastapi import FastAPI, Response

# Create FastAPI app
app = FastAPI(title="Osakuntabaari Menu Calendar API")

@app.get("/calendar.ics", response_class=Response)
async def get_calendar():
    """
    Endpoint that serves the menu calendar as an ICS file.
    """
    menu = get_weeks_menu()
    calendar = create_menu_calendar(menu)
    
    calendar_content = str(calendar)
    
    print(f"{datetime.now()}: Calendar served")
    
    return Response(
        content=calendar_content,
        media_type="text/calendar",
        headers={
            "Content-Disposition": "attachment; filename=osakuntabaari_menu.ics"
        }
    )

@app.get("/")
async def root():
    """
    API info endpoint
    """
    return {
        "message": "Osakuntabaari Menu Calendar API", 
        "endpoints": {
            "calendar": "/calendar.ics"
        }
    }

if __name__ == "__main__":
    port = 5000
    
    print(f"Server starting at http://localhost:{port}")
    print(f"Calendar available at http://localhost:{port}/calendar.ics")
    print("Press Ctrl+C to stop the server")
    
    uvicorn.run(app, host="0.0.0.0", port=port)
