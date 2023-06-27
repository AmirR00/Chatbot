class files():
    path = "/Users/svetlanaroman/Desktop/coding/PyProg/Practice/TODOLISTFILE.txt"

    def __init__(self) -> None:
        pass
    
    def writemethod(self, data):
        with open(self.path, "a" ) as file:
            file.write(data + "\n")
    
    def readmethod(self):
        with open(self.path, "r") as file:
            info = file.read()
        return info.strip()

class user(files):
    def __init__(self) -> None:
        super().__init__()
        print("WELCOME TO A TO-DO LIST!")
        print("1 - ADD SOMETHING TO A LIST \n2 - VIEW YOUR LIST")
        self.Inp = input()
        if self.Inp == "1":
            self.ADD()
        elif self.Inp.strip() == "2":
            self.ViewTask()
        else:
            print("Enter 1 or 2")
    
    def ADD(self):
        print("Enter your task: ")
        self.task = input("")
        self.task = self.task.strip()
        self.writemethod(self.task)
        print("-Task was added-")

    def ViewTask(self):
        print("List of your tasks:")
        print(self.readmethod())
 