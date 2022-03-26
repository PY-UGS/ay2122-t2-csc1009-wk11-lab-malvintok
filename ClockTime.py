class ClockTime:
    def __init__(self) -> None:
        pass

    def setHours(self):
        self.hours = input("Hours: ")
    
    def setMinutes(self):
        self.minutes = input("Minutes: ")

    def setSeconds(self):
        self.seconds = input("Seconds: ")

    def setTime(self):
        self.setHours()
        self.setMinutes()
        self.setSeconds()

    def showTime(self):
        print(self.hours + ":" + self.minutes + ":" + self.seconds)

clock = ClockTime()
clock.setHours()
clock.setMinutes()
clock.setSeconds()
clock.showTime()