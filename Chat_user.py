import datetime
class FUNCTIONALITY:
    def __init__(self) -> None:
        pass
    
    def time(self):
        time = datetime.datetime.now()
        datetime.time
        hour = time.hour
        minute = time.minute
        seconds = time.second
        string = f"{hour}:{minute}:{seconds}"
        print(string)
    
    def date(self):
        time = datetime.datetime.now()
        year = time.year
        month = time.month
        days = time.day
        date = time.date
        string = f"Year: {year}\nMonth: {month}\nDay: {days}"
        print(string)

    def weather(self):
        print("Sunny/windy")

class INTERACTION(FUNCTIONALITY):
    def __init__(self) -> None:
        super().__init__()
        print("Hello, user!")
        print("Hope you are doing good!")
        print("What would you like to know?")
        a = input()
        b = a.lower()
        if "time" in b:
            self.time()
        elif "date" in b:
            self.date()
        elif "weather" in b:
            self.weather()
        else:
            print("Sorry, I can't do that for you. Please try again!")

obj = INTERACTION()
















