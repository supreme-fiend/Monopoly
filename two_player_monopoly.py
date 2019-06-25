# A simple two player Monopoly game in python
# Everything except rent, houses and prison

import pygame
import random

pygame.init()

win = pygame.display.set_mode((1000, 1100))

win.fill((255, 255, 255))
font = pygame.font.SysFont("comicsans", 20)
pygame.display.set_caption("Peg jump test")
clock = pygame.time.Clock()

board_img = pygame.image.load('boardimage.png')

board = []
buttons = []
msgs = []
curr_dice_no = 0


class Place:
    def __init__(self, name, cost, rent, special):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.special = False
        self.owned = False
        self.players_on_square = []
        board.append(self)


class Player:
    def __init__(self, c):
        self.pos = 0
        self.colour = c
        self.money = 1000
        self.places = []
        self.jail = False
        board[0].players_on_square.append(self)

    def move_peg(self, dice_no):
        if self.pos + dice_no < len(board):
            board[self.pos].players_on_square.remove(self)
            board[self.pos+dice_no].players_on_square.append(self)
            self.pos += dice_no
            refresh()
        else:
            board[self.pos].players_on_square.remove(self)
            board[self.pos+dice_no - len(board)].players_on_square.append(self)
            self.pos = self.pos+dice_no - len(board)

    def buy_place(self):
        if not board[self.pos].special and not board[self.pos].special:
            self.money -= board[self.pos].cost
            self.places.append(board[self.pos])
            board[self.pos].owned = True


class Button:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = text
        self.button_bgcolour = (0, 255, 0)
        self.button_textcolour = (0, 0, 0)
        self.show = True
        self.clickable = True
        buttons.append(self)

    def draw(self):
        pygame.draw.rect(win, self.button_bgcolour, (self.x, self.y, self.width, self.height))
        text = font.render(self.text, 1, self.button_textcolour)
        win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def delete(self):
        buttons.remove(self)

    def set_show(self):
        self.show = True
        self.set_clickable()

    def set_clickable(self):
        self.clickable = True
        self.button_bgcolour = (0, 255, 0)

    def set_unclickable(self):
        self.clickable = False
        self.button_bgcolour = (255, 0, 0)


class message:
    def __init__(self, text, position):
        self.text = text
        self.position = position
        self.show = True
        msgs.append(self)
    def print_msg(self):
        t = font.render(self.text, 0, (0, 0, 0))
        win.blit(t, self.position)

def print_board():
    win.blit(board_img, (95, 95))
    pos = 40
    i = 0
    while i <= 7:
        place = board[i]
        pygame.draw.rect(win, (0, 0, 0), (pos, 40, 65, 55))
        pygame.draw.rect(win, (255, 255, 255), (pos+10, 50, 50, 40))
        playerpos = 55

        for peg in place.players_on_square:
            pygame.draw.circle(win, peg.colour, (pos+25, playerpos), 5, 1)
            playerpos += 5
        pos += 55
        i += 1
    pos = 95
    while i < 14:
        pygame.draw.rect(win, (0, 0, 0), (40, pos, 65, 55))
        pygame.draw.rect(win, (255, 255, 255), (50, pos, 50, 45))
        ppos1 = pos+10
        for peg in board[21 - (i+14)].players_on_square:
            pygame.draw.circle(win, peg.colour, (60, ppos1), 5, 1)
            ppos1 += 5

        ppos2 = pos+10
        pygame.draw.rect(win, (0, 0, 0), (425, pos, 65, 55))
        pygame.draw.rect(win, (255, 255, 255), (435, pos+10, 50, 55))
        for peg in board[i].players_on_square:
            pygame.draw.circle(win, peg.colour, (460, ppos2), 5, 1)
            ppos2 += 5
        i += 1
        pos += 55

    i = 21

    pos = 40
    while i >= 14:
        place = board[i]
        pygame.draw.rect(win, (0, 0, 0), (pos, 425, 65, 55))
        pygame.draw.rect(win, (255, 255, 255), (pos+5, 430, 55, 40))
        playerpos = 455
        for peg in place.players_on_square:
            pygame.draw.circle(win, peg.colour, (pos+25, playerpos), 5, 1)
            playerpos += 12
        pos += 55
        i -= 1

def print_all_msgs():
    for msg in msgs:
        if msg.show:
            msg.print_msg()


def print_all_buttons():
    for butt in buttons:
        if butt.show:
            butt.draw()


def refresh():
    win.fill((255, 255, 255))
    print_board()
    print_all_buttons()
    red_msg.text = f"RED'S TURN ({peg1.money})"
    blue_msg.text = f"BLUE'S TURN ({peg2.money})"
    if butt1.clickable:
        red_msg.show = True
        red_msg.show = True
        blue_msg.show = False
    elif butt2.clickable:
        red_msg.show = False
        blue_msg.show = True
    print_all_msgs()


def perform_button_operation(b):
    if b == butt1 and b.clickable:
        dno = random.randint(1, 6)
        peg1.move_peg(dno)
        b.set_unclickable()
        msg1.text = f"YOU LANDED ON {board[peg1.pos].name} ({board[peg1.pos].cost})"
        msg1.show = True
        buy1.set_clickable()
        pass1.set_clickable()

    if b == butt2 and b.clickable:
        dno = random.randint(1, 6)
        peg2.move_peg(dno)
        b.set_unclickable()
        msg1.text = f"YOU LANDED ON {board[peg2.pos].name} ({board[peg2.pos].cost})"
        msg1.show = True
        buy2.set_clickable()
        pass2.set_clickable()

    if b == buy1 and b.clickable:
        peg1.buy_place()
        buy1.set_unclickable()
        pass1.set_unclickable()
        butt2.set_clickable()
        msg1.show = False

    if b == buy2 and b.clickable:
        peg2.buy_place()
        buy2.set_unclickable()
        pass2.set_unclickable()
        butt1.set_clickable()
        msg1.show = False

    if b == pass1 and b.clickable:
        buy1.set_unclickable()
        pass1.set_unclickable()
        butt2.set_clickable()
        msg1.show = False

    if b == pass2 and b.clickable:
        buy2.set_unclickable()
        pass2.set_unclickable()
        butt1.set_clickable()
        msg1.show = False


go = Place(name = "GO       ",cost = 0,rent = 0,special = True)
okr= Place(name ="MUSTAFAR ",cost =60,rent =2,special = False)
wr = Place (name = "DAGOBAH  ",cost =60,rent =4,special =False)
fp1 = Place(name = "INC. TAX ",cost = 0,rent = 0, special =True)
ai= Place(name = "TATOOINE ",cost =100,rent =6,special =False)
pr=   Place(name = "TOYDARIA ",cost =120,rent =8,special =False)
pm=   Place(name = "BESPIN   ",cost =140,rent =10,special =False)
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

peg1 = Player((255, 0, 0))
peg2 = Player((0, 0, 255))
# peg3 = Peg((0, 255, 0))


butt1 = Button(700, 90, 30, 30, "ROLL")
butt2 = Button(700, 260, 30, 30, "ROLL")
buy1 = Button(780, 90, 30, 30, "BUY")
buy2 = Button(780, 260, 30, 30, "BUY")
pass1 = Button(860, 90, 30, 30, "PASS")
pass2 = Button(860, 260, 30, 30, "PASS")
butt2.set_unclickable()
buy1.set_unclickable()
buy2.set_unclickable()
pass1.set_unclickable()
pass2.set_unclickable()


red_msg = message(f"RED'S TURN ({peg1.money})", (70, 500))
red_msg.show = False

blue_msg = message(f"BLUE'S TURN ({peg2.money})", (70, 500))
blue_msg.show = False

msg1 = message("YOU LANDED ON PLACE XYZ", (70, 570))
msg1.show = False

buy_msg = message ("YOU BOUGHT XYZ", (70, 600))
buy_msg.show = False

rent_msg = message("YOU PAID RENT", (70, 600))
rent_msg.show = False

run = True

winner = None

while run:
    refresh()
    pygame.display.update()
    if peg1.money <= 0:
        winner = peg2
        run = False
        break
    if peg2.money <= 0:
        winner = peg1
        run = False
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            for butt in buttons:
                if butt.isOver(pygame.mouse.get_pos()) and butt.show:
                    perform_button_operation(butt)
                    # pygame.time.delay(20)


win2 = pygame.display.set_mode((300, 300))
f = ""
if winner == peg1:
    f = "WINNER IS RED"
else:
    f = "WINNER IN BLUE"

t = font.render(f, 1, (0, 0, 0))
win2.fill((255, 255, 255))
while True:
    pygame.display.update()
    win.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    win2.blit(t, (150, 150))

exit()
