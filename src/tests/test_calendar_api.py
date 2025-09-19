from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_main_calendar():
    response = client.get("/calendar.ics")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/calendar; charset=utf-8"

def test_timed_calendar():
    response = client.get("/calendar_timed.ics")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/calendar; charset=utf-8"
