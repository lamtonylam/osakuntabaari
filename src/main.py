import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lib.hamis_data import get_weeks_menu
from lib.menu import create_menu_calendar, create_menu_calendar_timed
from datetime import datetime
from ics import Calendar, Event
import os
import sys
import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates

# Create FastAPI app
app = FastAPI(title="Osakuntabaari Menu Calendar API")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    """
    API info endpoint
    """
    
    whole_path = str(request.url)
    
    path_for_calendar = whole_path.rstrip("/") + "/calendar.ics"
    path_for_calendar_timed = whole_path.rstrip("/") + "/calendar_timed.ics"
    
    return templates.TemplateResponse( request=request,
        name="index.html", context={"path_for_calendar": path_for_calendar, "path_for_calendar_timed": path_for_calendar_timed}
    )

@app.get("/calendar.ics", response_class=Response)
async def get_calendar():
    """
    Endpoint that serves the menu calendar as an ICS file.
    """
    menu = get_weeks_menu()
    calendar = create_menu_calendar(menu)
    
    calendar_content = calendar.serialize()
    
    print(f"{datetime.now()}: Calendar served")
    
    return Response(
        content=calendar_content,
        media_type="text/calendar",
        headers={
            "Content-Disposition": "attachment; filename=osakuntabaari_menu.ics"
        }
    )

@app.get("/calendar_timed.ics", response_class=Response)
async def get_calendar_timed():
    """
    Endpoint that serves the menu calendar with menus as timed events as an ICS file.
    """
    menu = get_weeks_menu()
    calendar = create_menu_calendar_timed(menu)
    
    calendar_content = calendar.serialize()
    
    print(f"{datetime.now()}: Timed calendar served")
    
    return Response(
        content=calendar_content,
        media_type="text/calendar",
        headers={
            "Content-Disposition": "attachment; filename=osakuntabaari_menu_timed.ics"
        }
    )


if __name__ == "__main__":
    port = 8000
    
    print(f"Server starting at http://localhost:{port}")
    print(f"Calendar available at http://localhost:{port}/calendar.ics")
    print("Press Ctrl+C to stop the server")
    
    uvicorn.run("__main__:app", host="0.0.0.0", port=port, reload=True)
