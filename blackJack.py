import random
import sys
import time

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

logo1 = """
.---.  .---.  .---.
|A  |  |Q  |  |K  |
|  A|  |  Q|  |  K|
`---'  '---'  '---'  
"""
print(logo)

cards = [11, 2, 10, 4, 5, 10, 7, 8, 9, 10, 6, 10, 3]
cards1 = [11, 11, 11, 11, 11, 11, 11, 11]

player = random.choices(cards, k=2)
if sum(player) > 21 and 11 in player:
    player[player.index(11)] = 1
    print("Your cards:", player, sum(player))
pc = random.choices(cards)
print('Your cards:', player, 'current score:', sum(player))
print("Computer's first card:", pc)

while True:
    decis = input("Type 'y' to get another card, type 'n' to pass: ")
    if decis == 'n':
        break
    elif decis == 'y':
        player.append(random.choice(cards))
        print("Your cards:", player, 'current score:', sum(player))
        if sum(player) > 21 and 11 in player:
            player[player.index(11)] = 1
            print("Your cards:", player, 'current score:', sum(player))
        elif sum(player) > 21 and 11 not in player:
            print(logo1)
            print("Your cards:", player, 'current score:', sum(player), "\nComputer's cards:", pc, 'current score:', sum(pc))
            print_slow("\033[4;31;40m Busted! You lose!\n")
            quit()
        print(logo1)

    else:
        print("The input must be 'y' or 'n")

while sum(pc) < 17:
    print(logo1)
    pc.append(random.choice(cards))
    print("Computer's cards:", pc, 'current score:', sum(pc))

    if sum(pc) > 21 and 11 in pc:
        pc[pc.index(11)] = 1
        print("Computer's cards:", pc, 'current score:', sum(pc))
    elif sum(pc) > 21 and 11 not in pc:
        print(logo1)
        print("Your cards:", player,  'current score:', sum(player), "\nComputer's cards:", pc, 'current score:', sum(pc))
        print_slow("\033[4;32;40m You win! Computer busted!\n")
        quit()

if sum(player) > sum(pc):
    print(logo1)
    print("Your cards:", player, 'current score:', sum(player), "\nComputer's cards:", pc, 'current score:', sum(pc))
    print_slow("\033[4;32;40m You win!")
elif sum(player) < sum(pc):
    print(logo1)
    print("Your cards:", player, 'current score:', sum(player), "\nComputer's cards:", pc, 'current score:', sum(pc))
    print_slow("\033[4;31;40m You lose!")
else:
    print(logo1)
    print("Your cards:", player, 'current score:', sum(player), "\nComputer's cards:", pc, 'current score:', sum(pc))
    print_slow("\033[4;33;40m Draw!")
print("\n\033[1;30;43m Python, bitches!")












