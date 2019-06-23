# Another test owing to the fact that I'm new at Pygame
# Goal: To make an array of places and get a peg to jump from place to place
# The array is going to be a straight one, because we've already established that getting the peg to
# go around the whole loop is possible

import pygame
import random

pygame.init()

win = pygame.display.set_mode((1000, 1100))

win.fill((255, 255, 255))
font = pygame.font.SysFont("comicsans", 20)
pygame.display.set_caption("Peg jump test")
clock = pygame.time.Clock()

board = []
buttons = []
curr_dice_no = 0
curr_dice_no = 0


class Place:
    def __init__(self, n, c, r):
        self.name = n
        self.cost = c
        self.rent = r
        self.players_on_square = []
        board.append(self)


class Peg:
    def __init__(self, c):
        self.pos = 0
        self.colour = c
        board[0].players_on_square.append(self)

    def move_peg(self, dice_no):
        if self.pos + dice_no < len(board):
            board[self.pos].players_on_square.remove(self)
            board[self.pos+dice_no].players_on_square.append(self)
            self.pos += dice_no
            refresh()


class Button:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = text
        self.show = True
        buttons.append(self)

    def draw(self):
        pygame.draw.rect(win, (139, 136, 120), (self.x, self.y, self.width, self.height))
        text = font.render(self.text, 1, (0, 0, 0))
        win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def delete(self):
        buttons.remove(self)

def print_board():
    pos = 40
    i = 0
    while i <= 7:
        place = board[i]
        pygame.draw.rect(win, (0, 0, 0), (pos, 40, 110, 110))
        pygame.draw.rect(win, (255, 255, 255), (pos+10, 50, 95, 95))
        playerpos = 55

        for peg in place.players_on_square:
            pygame.draw.circle(win, peg.colour, (pos+25, playerpos), 5, 1)
            playerpos += 12
        pos += 110
        i += 1
    pos = 150
    while i < 14:
        pygame.draw.rect(win, (0, 0, 0), (40, pos, 115, 110))
        ppos1 = pos+12
        for peg in board[21 - (i+14)].players_on_square:
            pygame.draw.circle(win, peg.colour, (60, ppos1), 5, 1)
            ppos1 += 12
        pygame.draw.rect(win, (255, 255, 255), (50, pos, 90, 95))
        ppos2 = pos+12
        for peg in board[i].players_on_square:
            pygame.draw.circle(win, peg.colour, (820, ppos2), 5, 1)
            ppos2 += 12
        pygame.draw.rect(win, (0, 0, 0), (800, pos, 115, 110))
        pygame.draw.rect(win, (255, 255, 255), (810, pos+10, 90, 95))
        i += 1
        pos += 110


def print_all_buttons():
    for butt in buttons:
        if butt.show:
            butt.draw()


def refresh():
    win.fill((255, 255, 255))
    print_board()
    print_all_buttons()


def show_options():
    butt3.show = True

def buy_confirm():
    butt4.show = True

def perform_button_operation(b):
    if b.text == "ROLL":
        dno = random.randint(1, 6)
        peg1.move_peg(dno)
        curr_dice_no = dno
        b.delete()
        show_options()

    if b.text == "DICE SHOW":
        b.text = f"DICE SHOW {curr_dice_no}"
        b.delete()

    if b.text == "BUY PLACE":
        butt4.text = f"YOU BOUGHT {board[peg1.pos].name}"
        buy_confirm()


p1 = Place("SQ1", 100, 10)
p2 = Place("SQ2", 200, 15)
p3 = Place("SQ3", 300, 20)
p4 = Place("SQ4", 100, 10)
p5 = Place("SQ5", 100, 10)
p6 = Place("SQ6", 100, 10)
p7 = Place("SQ7", 100, 10)
p8 = Place("SQ8", 100, 10)
p9 = Place("SQ9", 100, 10)
p10 = Place("SQ10", 100, 10)
p11 = Place("SQ11", 100, 10)
p12 = Place("SQ12", 100, 10)
p13 = Place("SQ13", 100, 10)
p14= Place("SQ14", 100, 10)
p15 = Place("SQ15", 100, 10)
p16 = Place("SQ16", 100, 10)
p17 = Place("SQ17", 100, 10)
p18 = Place("SQ18", 100, 10)
p19 = Place("SQ19", 100, 10)
p20 = Place("SQ20", 100, 10)
p21 = Place("SQ21", 100, 10)
p22= Place("SQ22", 100, 10)
p23 = Place("SQ23", 100, 10)
p24 = Place("SQ24", 100, 10)
p25 = Place("SQ25", 100, 10)
p26 = Place("SQ26", 100, 10)
p27 = Place("SQ27", 100, 10)
p28 = Place("SQ28", 100, 10)
p25 = Place("SQ29", 100, 10)
p26 = Place("SQ30", 100, 10)
p27 = Place("SQ31", 100, 10)
p28 = Place("SQ32", 100, 10)
peg1 = Peg((255, 0, 0))
# peg2 = Peg((0, 255, 0))
# peg3 = Peg((0, 0, 255))


butt1 = Button(40, 200, 30, 30, "ROLL")
butt1.show = False
butt2 = Button(40, 260, 70, 30, "DICE SHOWS")
butt3 = Button(40, 200, 70, 30, "BUY PLACE")
butt4 = Button(40, 260, 110, 30, f"YOU BOUGHT {board[peg1.pos].name}")
butt2.show = False
butt3.show = False
butt4.show = False
run = True

while run:
    refresh()
    pygame.display.update()
    #butt1 = Button(40, 200, 30, 30, "ROLL")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            for butt in buttons:
                if butt.isOver(pygame.mouse.get_pos()) and butt.show:
                    perform_button_operation(butt)
                    pygame.time.delay(20)
exit()
