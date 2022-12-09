

class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def set_hour(self, hour):
        self.hour = hour 
        
    def set_minute(self, minute):
        self.minute = minute
        

    def set_seconds(self, second):
        self.second = second
        
    def set_time(self, hour, minute, second):
        self.set_hour(hour)
        self.set_minute(minute)
        self.set_seconds(second)
    
    def tick(self):
        self._second += 1
        if (self._second == 60):
            self._second = 0
            self._minute += 1

            if (self._minute == 60):

                self._minute = 0
                self._hour += 1

                if (self._hour == 24):
                    self._hour = 0

    def get_time(self):
        if(self.hour > 0 and self.hour <= 12):

            state = "AM"
        elif(self.hour > 12 and self.hour < 24):
            self.hour -= 12
            state = "PM"
        
        elif(self.hour == 12):
            self.hour = 0
            state = "PM"

        elif(self.hour == 24):
            self.hour = 0
            state = "AM"
        
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d} {state}")

    
def main():
    clock = Clock(12, 50, 12)
    clock.set_time(9,30,24)
    clock.set_hour(13)
    clock.set_seconds(30)
    clock.get_time()

main()