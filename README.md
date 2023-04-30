![Python versions](https://img.shields.io/pypi/pyversions/danger-python)
# Weather-API
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
The Weather-API is an API powered by Flask and FastAPI, we can send requests to them and send our city as a POST request and receieve the current weather.

### Installation
#### Flask Requirements
`Flask` :
```sh
# git clone 
git clone https://github.com/nothyphen/Weather-API.git
# open flask directory
cd flask
# virtualenv
source ven/bin/active
# install package
pip -r requirements.txt
# run app
python3 app.py
# url
http://127.0.0.1:8000/
# send city with POST method like this:
http://127.0.0.1:8000/?city=Tehran
```
`Fastapi` :
```sh
# git clone 
git clone https://github.com/nothyphen/Weather-API.git
# open fastapi directory
cd fast_api
# virtualenv
source ven/bin/active
# install package
pip -r requirements.txt
# open src directory
cd src
# run app
uvicorn app:app --reload
# url
http://127.0.0.1:8000/
# send city with POST method like this:
http://127.0.0.1:8000/?city=Tehran
```
