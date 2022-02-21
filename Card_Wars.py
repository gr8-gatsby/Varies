import random
import sys
import time

logo = """\033[1;33;48m
  ______     ___      .______       _______     ____    __    ____  ___      .______          _______.
 /      |   /   \     |   _  \     |       \    \   \  /  \  /   / /   \     |   _  \        /       |
|  ,----'  /  ^  \    |  |_)  |    |  .--.  |    \   \/    \/   / /  ^  \    |  |_)  |      |   (----`
|  |      /  /_\  \   |      /     |  |  |  |     \            / /  /_\  \   |      /        \   \    
|  `----./  _____  \  |  |\  \----.|  '--'  |      \    /\    / /  _____  \  |  |\  \----.----)   |   
 \______/__/     \__\ | _| `._____||_______/        \__/  \__/ /__/     \__\ | _| `._____|_______/    

"""

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

def print_cards(x):
    if x[0] == 15:
        y = "A"
    elif x[0] == 12:
        y = "J"
    elif x[0] == 13:
        y = "Q"
    elif x[0] == 14:
        y = "K"
    else:
        y = x[0]
    return y, x[1]

print(logo)
print("\033[1;36;48m          <<<(-_-)>>> a.k.a. War, not peace! by Slav Dad (in your face Tolstoi!)<<<(-_-)>>> \n")
print('\n\033[3;33;48mRules:')
print("Highest number wins. The suit (♥ ♦ ♣ ♠) doesn't add value to the card")
n = int(input('\n\033[1;0;48m <<<(-_-)>>> The number of players (max 10) please insert : ').strip())
if n < 2 or n > 10:
    print(
        "\033[1;31;48m Since you already are a joker, you don't need this cards game! Eject! \033[1;33;48m <<<(-_-)>>>")
    exit()
m = int(input('\n\033[1;0;48m <<<(-_-)>>> The number of decks of cards please insert: ').strip())
aa = 0
suit = ['♣', '♥', '♦', '♠']

# Deck generator & shuffle
deck = []
for i in range(2, 11, 1):
    for elem in suit:
        deck.append([i, elem])
for i in range(12, 16, 1):
    for elem in suit:
        deck.append([i, elem])

deck = deck * m
print("\n\033[1;33;48m <<<(-_-)>>> Cards in the deck", len(deck), "there are.")
random.shuffle(deck)
deck = random.sample(deck, len(deck))

ch = input("\n\033[1;0;48m <<<(-_-)>>> The cards for you I have shuffled. To do it again do you want me? Type a number of times or anything else for 'No, thanks': ")
if type(ch) == 'int':
    for i in range(ch):
        random.shuffle(deck)
        deck = random.sample(deck, len(deck))


deck = list(reversed(deck))

# impartirea cartilor
players = [[] for x in range(n)]
while len(deck) > 0:
    for i in range(n):
        try:
            players[i].append(deck.pop())
        except IndexError:
            break

for elem in players:
    print("\n\033[1;33;48m Player", players.index(elem) + 1, "has", len(elem), "cards")
cnt = 0

# Incepe jocul efectiv
# Incepe jocul efectiv
# Incepe jocul efectiv
# Incepe jocul efectiv
elim = []
while len([elem for elem in players if len(elem) > 0]) > 1:
    cnt += 1
# check daca a ramas cineva fara carti

            
#    players = [elem for elem in players if len(elem) > 0]
    pot = []
    hit = input("\n\033[1;0;48m Hit a key to play the next round! ")

    for i in range(n):
        if len(players[i]) == 0:
            if i not in elim:
                print("\n\033[1;31;48m Player", i + 1, "ran out of cards and has been eliminated.", "\n\033[1;0;48m ")
                elim.append(i)

    mac = 0
    idx = -1
    for elem in players:
        idx += 1
        if len(elem) > 0:
            pot.append(elem.pop(0))
            z = print_cards(pot[-1])
            print('Player', idx + 1, z, '--> Remaining cards: ', len(elem))
            if pot[-1][0] > mac:
                mac = pot[-1][0]
                winn = [idx]
            elif pot[-1][0] == mac:
                winn.append(idx)

    if len(winn) == 1:
        players[winn[0]] += pot
        print("\033[1;33;48m The winner of the round is \033[1;32;48m Player", winn[0]+1, "\033[1;0;48m")
    else:
        print("\n\033[2;31;48m <<<(-_-)>>> WAR! WAR! WAR! <<<(-_-)>>>")
# Razboi
        pot_w = []
        winn_w = winn
        while len(winn_w) > 1:
            for elem in winn_w:
                if len(players[elem]) == 0:
                    print("\n\033[1;31;48m Player", elem + 1, "ran out of cards and has been eliminated before the war")
                    winn.remove(elem)
                    break
            if len(winn) > 1:
                mac_w = 0
                for elem in winn_w:
                    pot_w.append(players[elem].pop(0))
                    z = print_cards(pot_w[-1])
                    print('Player', elem + 1, z, '--> Remaining cards: ', len(players[elem]))
                    if pot_w[-1][0] > mac_w:
                        mac_w = pot_w[-1][0]
                        winn_w = [elem]
                    elif pot_w[-1][0] == mac_w:
                        winn_w.append(elem)
            elif len(winn) == 1:
                win_w = winn
            else:
                print("Too weak the force was with all the fighters in the war. All dead they are now")
                print("The cards wil be distributed evenly between all still alive")
                pot = pot + pot_w
                while len(pot) > 0:
                    for i in range(len([elem for elem in players if len(elem) > 0])):
                        try:
                            players[i].append(pot.pop())
                        except IndexError:
                            break
        if len(winn_w) == 1:
            print("\033[1;33;48m <<<(-_-)>>>    <<<(-_-)>>>   <<<(-_-)>>>\033[1;0;48m")
            players[winn_w[0]] = players[winn_w[0]] + pot + pot_w
            aa = winn_w[0]
            print("The war has been won by the \033[1;32;48m Player", aa + 1, "\033[1;0;48m")

    p = []
    for elem in players:
        p.append(len(elem))
    #print([elem for elem in p if elem > 0])
    if cnt in [100, 200, 300, 400]:
        print("\033[1;35;48m Boring ... I have shuffled the cards again! \033[1;0;48m")
        for elem in players:
            random.shuffle(elem)
            elem = random.sample(elem, len(elem))
    elif cnt == 500:
        print("\033[1;32;48m <<<(-_-)>>> Boring it is. We already had", cnt, "rounds <<<(-_-)>>>")
        print("\033[1;32;48m <<<(-_-)>>> Nobody wins! <<<(-_-)>>>")
        exit()
a = [players.index(elem)+1 for elem in players if len(elem) > 0]
print("\033[1;32;48m <<<(-_-)>>> The winner of the game is Player", a[0], "in", cnt, "rounds <<<(-_-)>>>")













