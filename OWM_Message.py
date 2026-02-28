import requests
import os
from twilio.rest import Client
from datetime import datetime

parametres = {"lat": 24.618538,
              "lon" : 72.766403,
              "appid" : os.getenv("OWM_KEY"),
              "units" : "metric",
              "cnt" : 5,}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parametres)
response.raise_for_status()
data = response.json()

text_message = ""
for i in range(0,5):
    time_stamp = (data['list'][i])
    dt = datetime.fromtimestamp(time_stamp['dt'])
    temp = (time_stamp['main']['temp'])
    feels_like = time_stamp['main']["feels_like"]
    weather = (time_stamp['weather'][0]["description"])
    humidity = (time_stamp['main']['humidity'])

    text_message+=(f"\nGood Morning.🥳🌄\n"
                    f"Today's hourly weather forecast:-⏰\n"
                    f"Date & Time ️📅 = {dt}\n"
                    f"Temperature = {temp}°C\n"
                    f"Feels_Like = {feels_like}°C\n"
                    f"Weather = {weather}\n"
                    f"Humidity💧 = {humidity} g/m³\n"
                    f"_______________________________\n")

account_sid = os.getenv("TWILLIO_ACCOUNT_SID")
auth_token = os.getenv("twilio_auth_token")
client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='whatsapp:+14155238886',
    to='whatsapp:+917849897468',
    body= f"{text_message}\nHave a Good Day,Sir..!!💘"
)
