import datetime
import calendar

now = datetime.datetime.now()

print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))



def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])

date = now.strftime("%d %m %Y")

print("Day of the Week :",findDay(date))
