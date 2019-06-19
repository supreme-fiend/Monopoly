# Basic monopoly text-based game
# Nothing fancy, just the basic concept of moving around, buying stuff and prison
# There are no Chance cards
# Instead, there are 2 spots where you get money and 2 spots where you lose money.
# No houses and hotels
# Oh, and the theme is Star Wars based.
import random

board = []
players_list = []


class Player:
    def __init__(self, num):
        self.name = "P"
        self.name += str(num+1)
        self.money = 1000
        players_list.append(self)
        self.curr_square = 0
        self.places_owned = []
        self.prison = False
        self.prison_sentence = 0
    def display_places_owned (self):
        print ("[", end = "")
        for place in self.places_owned:
            print(place.name, end = " ")
        print("]")

    def single_turn(self):
        print (f"It's {self.name}'s turn.")
        print (f'You have {self.money} amount of cash.')
        if not self.prison:
            print ("1) VIEW PLACES YOU OWN")
            print ("2) ROLL DICE")
            choice = input ("> ")
            if int(choice) == 1 :
                self.display_places_owned()
                print ("Press 0 to continue turn")
                input("> ")
                self.single_turn()
            elif int(choice) == 2:
                dice_no = random.randint(1, 12)
                print (f'Dice show {dice_no}')
                board[self.curr_square].move_player(self, dice_no)
                if (not board[self.curr_square].special) and not (board[self.curr_square].owned):
                    board[self.curr_square].print_details()
                    print ("1)Buy")
                    print ("2)Pass")
                    ch = int(input(">"))
                    if ch==1 and board[self.curr_square].cost < self.money:
                        self.places_owned.append(board[self.curr_square])
                        self.money -= board[self.curr_square].cost
                        board[self.curr_square].owned = True
                elif board[self.curr_square].owned :
                    for p in players_list:
                        if board[self.curr_square] in p.places_owned:
                            self.money -= board[self.curr_square].rent
                            p.money += board[self.curr_square].rent
                            print(f"You paid rent of {board[self.curr_square].rent} to {p.name}")
                            print ("Enter 0 to continue")
                            rand = input(">")
                elif board[self.curr_square].special:
                    print("This is a special location")
                    n = self.curr_square
                    if n == 3:
                        print ("INCOME TAX. YOU LOSE 100")
                        self.money -= 100
                    elif n == 7:
                        print("VISITING PRISON")
                    elif n == 12:
                        print ("SUPER TAX. YOU LOSE 200")
                        self.money -= 200
                    elif n == 14:
                        print ("FREE PARK.")
                    elif n == 18:
                        print ("YOU WIN THE LOTTERY!!! YOU GAIN 300")
                        self.money += 300
                    elif n == 21:
                        print ("YOU HAVE BEEN FOUND GUILTY FOR AN OFFENSE AGAINST THE GALACTIC EMPIRE.")
                        print ("YOU ARE SENTENCED TO PRISON")
                        board[self.curr_square].move_player(self, 14)
                        self.prison = True
                        self.prison_sentence = 3
                    elif n == 23:
                        print ("STOCK MARKET IS UP. YOU GAIN 100")
                        self.money += 100
        else:
            if self.prison_sentence == 0:
                self.prison = False
                print("You have completed your prison sentence.")
                self.single_turn()
            print ("1)Pay fee and exit prison (200)")
            print ("2)Wait another day")
            prison_choice = int(input("> "))
            if prison_choice == 1:
                self.money -= 200
                self.prison = False
                self.prison_sentence = 0
                self.single_turn()
            else:
                self.prison_sentence -= 1


class Place:
    def __init__(self, name, cost, rent, special):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.special = special
        board.append(self)
        self.players_on_square = []
        self.owned = False

    def display(self):
        print(self.name, end='[')
        i = 0
        for i in range(len(self.players_on_square)):
            print(self.players_on_square[i].name, end=' ')
        print(']', end = ' ')

    def print_details(self):
        print (f"You are on {self.name}")
        print (f"Cost is {self.cost}")

    def add_player(self, player):
        self.players_on_square.append(player)

    def chuck_player(self, player):
        self.players_on_square.remove(player)

    def move_player(self, player, diceno):
        self.chuck_player(player)
        new_pos = player.curr_square + diceno
        if (new_pos > len(board)):
            new_pos -= (len(board)+1)
            player.money += 200
            print ("You passed go and received 200")
        board[new_pos].add_player(player)
        player.curr_square = new_pos




go = Place(name = "GO       ",cost = 0,rent = 0,special = True)
okr= Place(name ="MUSTAFAR ",cost =60,rent =2,special = False)
wr = Place (name = "DAGOBAH  ",cost =60,rent =4,special =False)
fp1 = Place(name = "INC. TAX ",cost = 0,rent = 0, special =True)
ai= Place(name = "TATOOINE ",cost =100,rent =6,special =False)
pr=   Place(name = "TOYDARIA ",cost =120,rent =8,special =False)
pm=   Place(name = "BESPIN   ",cost =140,rent =10,special =False)
prison=  Place(name = "PRISON   ",cost = 0,rent = 0,special = True)
wh=   Place(name = "KASHYYYK ",cost =140,rent =10, special =False)
na=   Place(name = "SALEUCAMI",cost =160,rent =12, special =False)
bs=   Place(name = "ORD MANTL",cost =180,rent =14,special =False)
ms=   Place(name = "DANTOOINE",cost =180,rent =14,special =False)
fp2 =   Place(name = "SUPER TAX",cost = 0,rent = 0,special = True)
vs=   Place(name = "MALASTARE",cost =200,rent =16,special =False)
free =   Place(name = "FREE PARK",cost = 0,rent = 0, special =True)
ts=   Place(name = "YAVIN    ",cost =220,rent =18,special =False)
fs=   Place(name = "UTAPAU   ",cost =220,rent =18,special =False)
tsq=   Place(name = "MONCALAMARI",cost =240,rent =20,special =False)
fp3 =   Place (name = "LOTTERY  ",cost = 0,rent = 0,special = True)
lsq=   Place(name = "GEONOSIS ",cost =260,rent =22,special =False)
cs=   Place(name = "MANDALORE",cost =260,rent =22,special =False)
goToJail =   Place (name = "GOTO JAIL",cost = 0,rent = 0,special =True)
py=   Place(name = "RYLOTH   ",cost =280,rent =24,special =False)
fp4 =   Place (name = "STOCKS   ",cost = 0,rent = 0,special = True)
rs=   Place(name = "NABOO    ",cost =300,rent =26,special =False)
bos=   Place(name = "Cato Nei.",cost =320,rent =28,special =False)
pl=   Place(name = "ALDERAAN ",cost =350,rent =35,special =False)
mf=   Place(name = "CORUSCANT",cost =400,rent =50,special =False)


def print_board():
    i = 0
    while i <= 7:
        board[i].display()
        i += 1
    print()
    while i < 14:
        board[21 - (i + 14)].display()
        print ('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', end = " ")
        board[i].display()
        print()
        i += 1

    i = 21

    while i >= 14:
        board[i].display()
        i -= 1
    print()


game_end = False

print("How many players (2 or more)")

choice = int(input("> "))

for i in range(choice):
    p = Player(i)

board[0].players_on_square = players_list.copy()

while not game_end:
    for p in players_list:
        print_board()
        p.single_turn()
    if (p.money <= 0):
        players_list.remove(p)
        print(f"{p.name} has lost")
    input('Press 0 to continue\n> ')

    if len(players_list) <= 1:
        game_end = True
        break
