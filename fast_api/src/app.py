#!/user/bin/python3

import requests
import bs4
from fastapi import FastAPI

def get_weather(city):
    url = f"https://www.google.com/search?q=weather+{city.replace(' ', '')}"
    session = requests.session()
    session.headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    page = session.get(url)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    try:
        celsios = soup.find('span', attrs={'id':'wob_tm'}).text
        wind = soup.find('span', attrs={'id':'wob_ws'}).text
        humidity = soup.find('span', attrs={'id':'wob_hm'}).text
        time = soup.find('div', attrs={'id':'wob_dts'}).text
        data = {
            'celsion' : celsios,
            'wind' : wind,
            'humidity' : humidity,
            'time' : time,
        }
    except AttributeError:
        data ={
            'error' : 'not found your city'
        }
    return data

app = FastAPI()

@app.post("/")
def get_city(city = None):
    if city == None:
        return {'please send your city'}
    else:
        return get_weather(city)