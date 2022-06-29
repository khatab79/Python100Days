import datetime as dt
import os
import random
import smtplib
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

gmail_user = os.getenv('gmail_user')
gmail_password = os.getenv('gmail_password')

date = dt.datetime.now().weekday()

if date == 1:
    with open("quotes.txt") as txt:
        sent_subject = "Hey Friends!"
        sent_body = random.choice(txt.readlines())

        email_text = f"Subject: Motivation\n\n {sent_body}"

        with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
            connection.ehlo()
            connection.login(gmail_user, gmail_password)
            connection.sendmail("gmail_user", 'devtestdev2000@gmail.com', email_text )
            print('Email sent!')

