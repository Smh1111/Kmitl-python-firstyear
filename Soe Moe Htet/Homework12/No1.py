class Clock:
    def __init__(self, hh, mm, ss):
        self.hh = int(hh)
        self.mm = int(mm)
        self.ss = int(ss)

    def run(self):
        while(True):
            if (self.ss > 59):
                self.mm += 1
                self.ss = 0

            if (self.mm > 59):
                self.hh += 1
                self.mm = 0

            if (self.hh >= 24):
                self.hh = 0

            self.ss += 1

            print(f"{self.hh:6d}:{self.mm:02d}:{self.ss:02d}")

    def setTime(self, h, m, s):
        self.hh = h
        self.mm = m
        self.ss = s
    
class AlarmClock(Clock):
    def __init__(self, hh, mm, ss, alarm_hh, alarm_mm, alarm_ss):
        super().__init__(hh, mm, ss)

        self.alarm_hh = int(alarm_hh)
        self.alarm_mm = int(alarm_mm)
        self.alarm_ss = int(alarm_ss)

        self.alarm_on_off = False

    def alarm_on(self):
        self.alarm_on_off = True

    def alarm_off(self):
        self.alarm_on_off = False   

    def run(self):
        while(True):
            if (self.ss > 59):
                self.mm += 1
                self.ss = 0

            if (self.mm > 59):
                self.hh += 1
                self.mm = 0

            if (self.hh >= 24):
                self.hh = 0

            print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")
            if (
                self.alarm_on_off == True and 
                self.ss == self.alarm_ss and
                self.mm == self.alarm_mm and
                self.hh == self.alarm_hh
                ):

                print("Stop....")
                break
            
            self.ss += 1

        
def main():
    #            (Actual clock)(Alarm)
    #             ( h,  m,  s,)(h, m , s)
    c = AlarmClock(1, 51, 41, 1, 52, 2)
    c.alarm_on()
    c.run()
    

main()