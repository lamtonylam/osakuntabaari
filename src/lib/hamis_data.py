import requests
from bs4 import BeautifulSoup


def __get_menu():
    url = 'https://hys.net/osakuntabaari/ruokalista/'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    todays_list = soup.find("div", {"class": "lunch"})
    return todays_list

def get_weeks_menu():
    weeks_list = __get_menu().find_all("div", {"class": "row"})
    menu_dict = {}
    for day in weeks_list:
        date = day.find("div", {"class": "col-day"}).p.get_text().capitalize()
        food = day.find("div", {"class": "col-food"}).p.get_text()
        menu_dict[date] = food
    return menu_dict
