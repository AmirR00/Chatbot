import random

def rpsgame():
    #make computer choose rock(r), paper(p), scizzors(s)

    userinp = input("Choose one of the following [R/P/S]: ").upper()
    if userinp == "S" or userinp == "R" or userinp == "P":
        Compinp = random.choice(["R", "P", "S"])


        # U=C --> D; 
        # U = "R" and C = "S" --> U wins
        # U = "S" and C = "P" --> U wins
        # U = "P" and C = "R" --> U wins
        # U = "S" and C = "R" --> C wins
        # U = "P" and C = "S" --> C wins
        # U = "R" and C = "P" --> C wins


    print(f"Computer choice = {Compinp}")
    if userinp == Compinp:
        print("Draw")
    elif ((userinp == "R" and Compinp == "S") or 
        (userinp == "S" and Compinp == "P") or 
        (userinp == "P" and Compinp == "R")):
        print("User wins")
    else:
        print("Computer wins")

        
            
