import datetime
import calc
import passcheck
import ToDoListOOPS
import RPS
import Hangman
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
    
    def guicalculator(self):
        calc.main()
    
    def passwordchecker(self):
        passcheck.Checkermain()
    
    def Todolist(self):
        ToDoListOOPS.user()
    
    def Rockpapergame(self):
        RPS.rpsgame()
    
    def hangmangame(self):
        Hangman.hangame()


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
        elif "date" in b or "year" in b or "month" in b:
            self.date()
        elif "weather" in b or "forecast" in b or "temp" in b:
            self.weather()
        elif "calc" in b or "math" in b:
            self.guicalculator()
        elif "check" in b or "pass" in b:
            self.passwordchecker()
        elif "todo" in b or "task" in b:
            self.Todolist()
        elif "rock" in b or "paper" in b or "scizzors" in b:
            self.Rockpapergame()
        elif "hangman" in b or "hangmangame" in b:
            self.hangmangame()
        else:
            print("Sorry, I can't do that for you. Please try again!")

obj = INTERACTION()
