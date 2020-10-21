class Time:
    """
    Represents the time of the day.
    Attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        if not isinstance(self.hour, int):
            self.hour=0
        if not isinstance(self.minute,int):
            self.minute=0
        if not isinstance(self.second,int):
            self.second=0
        if self.hour>23 or self.hour<0:
            self.hour=0
        if self.minute>59 or self.minute<0:
            self.minute=0
        if self.second>59 or self.second<0:
            self.second=0
    
    def is_after(self, time2):
        if self.hour>time2.hour:
            return True
        elif self.hour<time2.hour:
            return False
        elif self.minute>time2.minute:
            return True
        elif self.minute<time2.minute:
            return False
        elif self.second>time2.second:
            return True
        else:
            return False

    def __add__ (self,time2):
        m1=0
        h1=0
        s=self.second+time2.second
        if s>59:
            m1=s//60
            s=s%60
        m=self.minute+time2.minute+m1
        if m>59:
            h1=m//60
            m=m%60
        h=self.hour+time2.hour+h1
        if h>23:
            h=h-24
        time=Time(h,m,s)
        return time  

    def __str__(self):
        if self.second<10:
            s_str=f"""0{self.second}"""
        else:
            s_str=f"""{self.second}"""
        if self.minute<10:
            m_str=f"""0{self.minute}"""
        else:
            m_str=f"""{self.minute}"""
        if self.hour<10:
            h_str=f"""0{self.hour}"""
        else:
            h_str=f"""{self.hour}"""
        str_to_print = f"""{h_str}:{m_str}:{s_str}"""
        return str_to_print 

    

              
            