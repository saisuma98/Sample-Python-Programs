
class TIME:
    startTime = 0
    endTime = 0

    def __init__(self):
        self.startTime = 0
        self.endTime = 0

    def duration(self,start,end):
        time = start-end

        day = time // (24 * 3600)
        time = time % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        print("Days:{}\nHours:{}\nMonths:{}\nSeconds:{}\n".format(day,hour,minutes,seconds))


t = TIME()

start = int(input("Enter the start time in seconds"))
end = int(input("Enter the end time in seconds"))

#t.duration(1234565,2234565)

t.duration(start,end)



