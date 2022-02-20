import sys
import random
import time

logo = """
   ______                        ________            _   __                __             
  / ____/_  _____  __________   /_  __/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/    / / / __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )    / / / / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/    /_/ /_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                                                                                                                                                          |/                                 
"""

win = """
                                 .''.
       .''.             *''*    :_\/_:     . 
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
lose = """
 ██▓     ▒█████    ██████ ▓█████  ██▀███   ▐██▌ 
▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒ ▐██▌ 
▒██░    ▒██░  ██▒░ ▓██▄   ▒███   ▓██ ░▄█ ▒ ▐██▌ 
▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄   ▓██▒ 
░██████▒░ ████▓▒░▒██████▒▒░▒████▒░██▓ ▒██▒ ▒▄▄  
░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░ ░▀▀▒ 
░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░ ░  ░ 
  ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░     ░░   ░     ░ 
    ░  ░    ░ ░        ░     ░  ░   ░      ░    
                                                

"""

print(logo)
print("Welcome to the Number Guessing Game, Lil Bitch!")
print("I'm thinking of a number between 1 and 100.")
target = random.randrange(101)

while True:
    choice = input("Choose a difficulty. Type 'e' for easy or 'h' for hard: ").strip()
    if choice == 'e':
        att = 10
        break
    elif choice == 'h':
        att = 6
        break
    else:
        print("Stop being a dick!")
print("You have", att, "attempts to guess the number.")

idx = att
while idx > 0:

    print('*****************************************')

    try:
        guess = int(input("\nMake a guess: ").strip())

        if guess < target:
            idx -= 1
            if idx == 0:
                print(lose)
                print("You've run out of guesses, Bitch! You lose like a sorry ass bitch!")
                print("Gaming, Bitch! Boooom!")
                print("The number was", target)
                break
            print("Too low.\nYou have", idx, "attempts remaining to guess the number.")
        elif guess > target:
            idx -= 1
            if idx == 0:
                print(lose)
                print("You've run out of guesses, Bitch! You lose like a sorry ass bitch!")
                print("Gaming, Bitch! Boooom!")
                print("The number was", target)
                break
            print("Too high.\nYou have", idx, "attempts remaining to guess the number.")
        else:
            print(win)
            print("You got it, Hotshot!")
            print("The answer is", target)
            break

    except:
        print("What do we have here? An asshole!")







