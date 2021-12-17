import datetime

string = "22 November 2021"
tab = string.split(" ")
long_month_name = tab[1]
datetime_object = datetime.datetime.strptime(long_month_name, "%B")
tab[1] = str(datetime_object.month)
print(":".join(tab))