class Clock:
    def __init__(self, hour = 0, minute = 0, second = 0, type = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.type = type


    def getHour(self):
        return self.hour
    def getMinute(self):
        return self.minute
    def getSecond(self):
        return self.second
    def getType(self):
        return self.type
    
    def setHour(self, h):
        self.hour = h
    def setMinute(self, m):
        self.minute = m
    def setSecond(self, s):
        self.second = s
    def setType(self, t):
        self.type = t

    def __str__(self):
        if self.type == 0:
            return '{:02}:{:02}:{:02}'.format(self.hour, self.minute, self.second)
        else:
           return '{:02}:{:02}:{:02} {}'.format(self.hour, self.minute, self.second, 'pm' if self.hour > 11 else 'am')

    def tick(self):
        if self.second >= 59:
            self.second = 0
            if self.minute >= 59:
                self.minute = 0
                self.hour += 1
            else:
                self.minute +=1
        else:
            self.second += 1       
        if self.hour == 24:
            self.hour = 0 
       
