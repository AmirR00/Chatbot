import random
def hangame():
    random_word = random.choice(["banana", "book", "mango", "comics", "melon", "pen"])

    def Letter_choice(word, guessed_letters):
        final_word = ""
        for letter in word:
            if letter in guessed_letters:
                final_word += letter
            else:
                final_word += "_"
        return final_word
        

    guessed_letters = []
    attempts = 6
    print("Welcome to the hangman!")
    print("You have to guess the right word.")
    while attempts > 0:
        print(Letter_choice(random_word, guessed_letters))
        print(f"You have {attempts} attempts left.")
        main_input = input("Please enter one letter: ").lower()
        if main_input in random_word:
            guessed_letters.append(main_input)
            print("The letter is correct!")
        
        if "_" not in Letter_choice(random_word, guessed_letters):
            print("Congratulations! \nYou've won!")
            break
            
        if main_input not in random_word:
            attempts -= 1
            print("The letter is not correct.")

        if attempts == 0:
            print("You have no attempts left. Game over.")
            

        



        
