#!/usr/bin/python3

from flask import Flask, jsonify, request #create data and app
import requests #send request to google for get weather
import bs4 #get weather in html page

app = Flask(__name__) #create app

#create get weather function
def get_weather(city):
    try:
        url = f"https://www.google.com/search?q=weather+{city.replace(' ', '')}"
        session = requests.session()
        session.headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        page = session.get(url)
        soup = bs4.BeautifulSoup(page.text, 'html.parser')
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

@app.route('/', methods = ['POST', 'GET'])
def get_data():
    city = request.args.get('city')
    if city != None:
        data = get_weather(city)
    else:
        data = {
            'error':'please send your city name'
        }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=8000)