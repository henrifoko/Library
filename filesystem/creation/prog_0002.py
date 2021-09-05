"""
05/09/2021
FOKO Henri

This program aim to compute the number of days between two dates. Those dates
are provided to program as command line arguments and the should be formated 
like "yyyy-mm-dd".
If the dates format is incorrect, the program will be stopped with an 
error.
"""


import sys
import datetime


def how_to_use():
    print(f"""HOW TO USE

    \rprog_name [-h] date1 [date2]


    -h    \t\t Print this text

    date1 \t\t First date argument
    date2 \t\t Second date argument

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


def days_between(d1: datetime.date, d2: datetime.date):
    return (d2 - d1).days


if __name__ == "__main__":
    args = sys.argv

    if args.index("-h") != -1:
        how_to_use()
        sys.exit(0)

    if len(args) == 2:
        date1 = datetime.date.today()
        date2 = date_from_string(args[1])
        print("{} day(s)".format(days_between(date1, date2)))

    elif len(args) == 3:
        date1 = date_from_string(args[1])
        date2 = date_from_string(args[2])
        print("{} day(s)".format(days_between(date1, date2)))

    else:
        print("Invalid syntax")
        how_to_use()
        raise SyntaxError()
