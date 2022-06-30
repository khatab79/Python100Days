import time
import requests
import os
import smtplib
from datetime import datetime
from dotenv import load_dotenv

# my position
LATITUDE = 49.2107718
LONGITUDE = -123.0735743


# return ISS position
def iss_current_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json#")
    data = response.json()
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])
    current_position = (latitude, longitude)
    return current_position


def iss_overhead():
    # compare ISS pos with current pos and return either true or false +- 5 rang from current pos
    iss_position = iss_current_position()
    if LATITUDE - 5 <= iss_position[0] <= LATITUDE + 5 and LONGITUDE - 5 <= iss_position[1] <= LONGITUDE + 5:
        return True


def is_dark():
    parameters = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", parameters)
    response.raise_for_status()
    data = response.json()['results']
    sunrise = int(data['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['sunset'].split("T")[1].split(":")[0])

    current_time = datetime.now().hour
    if current_time > 12:
        current_time -= 12

    if sunset <= current_time <= sunrise:
        return True


def send_notification():
    # send notification email
    load_dotenv(dotenv_path=".env")
    gmail_user = os.getenv('gmail_user')
    gmail_password = os.getenv('gmail_password')
    send_to = 'devtestdev2000@gmail.com'
    email_text = "Subject: ISS overhead\n\n Bro ISS near to your location. come up. check it in th sky"
    # print(email_text)

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.ehlo()
        connection.login(gmail_user, gmail_password)

        # to send email uncommitted the line below and change the send_to (use your email)
        # connection.sendmail("gmail_user", send_to, email_text)
        print('Email sent!')


# keep sending every 60S
while True:
    time.sleep(60)
    if iss_overhead() and is_dark():
        send_notification()
    else:
        print("ISS Still far. you will get email soon it near.")

