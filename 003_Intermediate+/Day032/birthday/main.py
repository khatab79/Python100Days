import pandas
from datetime import datetime
import smtplib
import random
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path="../.env")

USER = os.getenv('gmail_user')
PASSWORD = os.getenv('gmail_password')
PROVIDER = os.getenv('provider')

# read from birthday csv

birthday_dic = {}
# is_birthday = False

# name,email,year,month,day
try:
    data = pandas.read_csv("birthdays.csv")
    # data to dictionary
    birthday_dic = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
    # print(birthday_dic)
except:
    print("something wrong")

# check the date

birthday_day = datetime.today().day
birthday_month = datetime.today().month

# change it to today date and commit the two lines above
# birthday_day = 15
# birthday_month = 6

birthday = (birthday_month, birthday_day)

if birthday in birthday_dic:
    # print(birthday_dic[birthday]['name'])
    letter_file = f"letter_{ random.randint(1,3) }"
    birthday_person_details = birthday_dic[birthday]
    # print(birthday_person_details)

    with open(f"./letter_templates/{letter_file}.txt", 'r') as letter:
    # build the birthday msg
        # change the name
        msg_from = "Khatab"
        msg_body = letter.read().replace("[NAME]", birthday_person_details['name'])
        msg_subject = f"Happy Birthday { birthday_person_details['name'] }"
        msg_to_name = birthday_person_details['name']
        msg_to_email = birthday_person_details['email']
        msg = f"Subject: { msg_subject }\n\nFrom: {msg_from}\n\nTo: {msg_to_name}\n\n{msg_body}"

    # print(msg)
    # connect and send msg
    # print(USER, PASSWORD, PROVIDER, msg_to_email)
    try:
        with smtplib.SMTP_SSL(PROVIDER) as connect:
            connect.ehlo()
            connect.login(USER, PASSWORD)
            connect.sendmail(from_addr=USER, to_addrs=msg_to_email, msg=msg)
            print(f"msg gone to{ msg_to_name}, the contact email is { msg_to_email}")
    except:
        print("letter did not go, something wrong")
else:
    print("You have no birthday coming today")
