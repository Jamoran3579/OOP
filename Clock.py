class Clock(object):
    def __init__(self, hours: int, minutes: int, seconds: int):
        # Private variables to store the clock times
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

        self.alarm_hours = 12
        self.alarm_minutes = 0
        self.alarm_seconds = 0

        self.numbers = "1234567890"
        self.current_time = (str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))
        self.alarm_time = ""

    def check_time(self, time) -> bool:
        if time[0] not in self.numbers and time[1] not in self.numbers and time[3] not in self.numbers and time[4] not \
                in self.numbers and time[5] not in self.numbers and time[6] not in self.numbers:
            checker = False
        else:
            checker = True

        return checker

    def change_time(self, time) -> None:
        checker = self.check_time(time)

        if checker:
            self.hours = int(time[0])*10 + int(time[1])
            self.minutes = int(time[3])*10 + int(time[4])
            self.seconds = int(time[6])*10 + int(time[7])
        else:
            print("Invalid time")

        if self.hours > 24:
            self.hours = self.hours - 24
        if self.minutes > 60:
            self.minutes = self.minutes - 60
        if self.seconds > 60:
            self.seconds = self.seconds - 60

    def __str__(self):
        string1 = ("The time is:\n" + str(self.hours) + "hrs\n" + str(self.minutes) + "mins\n" + str(self.seconds) +
                   "secs")
        return string1

    def add_time(self, time) -> None:
        checker = self.check_time(time)

        if checker:
            self.hours = self.hours + int(time[0])*10 + int(time[1])
            self.minutes = self.minutes + int(time[3])*10 + int(time[4])
            self.seconds = self.seconds + int(time[6])*10 + int(time[7])
        else:
            print("Invalid time")

        if self.hours > 24:
            self.hours = self.hours - 24
        if self.minutes > 60:
            self.minutes = self.minutes - 60
        if self.seconds > 60:
            self.seconds = self.seconds - 60

    def set_alarm(self, time) -> None:
        checker = self.check_time(time)

        if checker:
            self.alarm_hours = int(time[0])*10 + int(time[1])
            self.alarm_minutes = int(time[3])*10 + int(time[4])
            self.alarm_seconds = int(time[6])*10 + int(time[7])
        else:
            print("Invalid time")

        if self.alarm_hours > 24:
            self.alarm_hours = self.alarm_hours - 24
        if self.alarm_minutes > 60:
            self.alarm_minutes = self.alarm_minutes - 60
        if self.alarm_seconds > 60:
            self.alarm_seconds = self.alarm_seconds - 60

    def ring_alarm(self) -> None:
        self.current_time = (str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))
        self.alarm_time = (str(self.alarm_hours) + ":" + str(self.alarm_minutes) + ":" + str(self.alarm_seconds))

        if self.alarm_time == self.current_time:
            print("落♬")
        else:
            print("It is not time for the alarm")


clock1 = Clock(10, 36, 12)
print(clock1)
print("\n")
clock1.change_time("15:12:54")
print(clock1)
print("\n")
clock1.add_time("21:23:47")
print(clock1)
print("\n")
clock1.change_time("17:30:42")
print(clock1)
print("\n")
clock1.set_alarm("17:30:42")
clock1.ring_alarm()
