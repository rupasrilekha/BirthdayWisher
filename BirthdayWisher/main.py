import datetime as dt
import smtplib

import pandas as pd
import random

my_email = "rupasrilekhakandula@gmail.com"
password = "qomy kmge apjw fgkw"

now= dt.datetime.now()
today_month=now.month
today_day=now.weekday()
today=(today_month,today_day)

data=pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person=birthdays_dict[today]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        contents=letter.read()
        contents=contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"

        )

