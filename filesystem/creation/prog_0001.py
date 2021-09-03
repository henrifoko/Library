"""
03/09/2021
FOKO Henri

This program is used to create folders in a directory.
The number of files is the number of days between the two 
dates that have been passed as parameters. For each day 
between these two dates, a folder will be created and the 
name of the folder will be the date corresponding to the 
day in question in the format "yyyy-mm-dd". The directories 
will be created in the same folder as the program is executing from.

The tow dates passed as parameters have to be formatted in 
the same way as the created directories names (yyyy-mm-dd).
An error will be raised if the date format is incorrect.
The second date should be greater than the first one. An error 
will be thrown otherwise.
"""


import os
import sys
import datetime


def how_to_use():
    print(f"""
    \rprog_name date1 [date2]
 
    \rdate1 \t\t First date argument
    \rdate2 \t\t Second date argument

    \rThe first date argument represents the starting date and 
    \rthe second one if provided, the end date.
    \rIf only one argument is provided, this one will be 
    \rconsidered as the second date parameter and the first 
    \rand the current runtime date as the first parameter.

    \rProgram documentation :
    {__doc__}
    """)


def date_from_string(s: str):
    l = s.split("-")
    for i, val in enumerate(l):
        l[i] = int(val)
    return datetime.date(day=l[0], month=l[1], year=l[2])


def date_to_string(d: datetime.date):
    # print("Today's date is {:%Y-%m-%d %H:%M}".format(datetime.date.today()))
    return "{:%Y-%m-%d}".format(d)


def create_folder(name: str):
    try:
        os.mkdir(name)
    except FileExistsError:
        print(f"{name} already exists")


def generate_folder(d1: datetime.date, d2: datetime.date):
    print(f"date 1 : {d1}")
    print(f"date 2 : {d2}")

    date = date1

    while date < date2:
        create_folder(date_to_string(date))
        date = date + datetime.timedelta(days=1)
    create_folder(date_to_string(date))


args = sys.argv

if len(args) == 2:
    date1 = datetime.date.today()
    date2 = date_from_string(args[1])
    generate_folder(date1, date2)

elif len(args) == 3:
    date1 = date_from_string(args[1])
    date2 = date_from_string(args[2])
    generate_folder(date1, date2)

else:
    print("Invalid syntax")
    how_to_use()
    raise SyntaxError()
