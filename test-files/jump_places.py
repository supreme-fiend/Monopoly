# Another test owing to the fact that I'm new at Pygame
# Goal: To make an array of places and get 2 pegs to jump from place to place
# Goal2: Implementing circular jumping about.

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
        else:
            board[self.pos].players_on_square.remove(self)
            board[self.pos+dice_no - len(board)].players_on_square.append(self)
            self.pos = self.pos+dice_no - len(board)


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


board_img = pygame.image.load('boardimage.png')


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
    if b.text == "ROLL1" and b.clickable:
        dno = random.randint(1, 6)
        peg1.move_peg(dno)
        b.set_unclickable()
        butt2.set_clickable()
        # curr_dice_no = dno
        # b.delete()
        # show_options()

    if b.text == "ROLL2" and b.clickable:
        dno = random.randint(1, 6)
        peg2.move_peg(dno)
        b.set_unclickable()
        butt1.set_clickable()
        # curr_dice_no = dno

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
p14 = Place("SQ14", 100, 10)
p15 = Place("SQ15", 100, 10)
p16 = Place("SQ16", 100, 10)
p17 = Place("SQ17", 100, 10)
p18 = Place("SQ18", 100, 10)
p19 = Place("SQ19", 100, 10)
p20 = Place("SQ20", 100, 10)
p21 = Place("SQ21", 100, 10)
p22 = Place("SQ22", 100, 10)
p23 = Place("SQ23", 100, 10)
p24 = Place("SQ24", 100, 10)
p25 = Place("SQ25", 100, 10)
p26 = Place("SQ26", 100, 10)
p27 = Place("SQ27", 100, 10)
p28 = Place("SQ28", 100, 10)
peg1 = Peg((255, 0, 0))
peg2 = Peg((0, 0, 255))
# peg3 = Peg((0, 255, 0))


butt1 = Button(700, 90, 30, 30, "ROLL1")
butt2 = Button(700, 260, 30, 30, "ROLL2")
butt3 = Button(40, 200, 70, 30, "BUY PLACE")
butt4 = Button(40, 260, 110, 30, f"YOU BOUGHT {board[peg1.pos].name}")
butt3.show = False
butt4.show = False
run = True

red_turn = True

while run:
    refresh()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            for butt in buttons:
                if butt.isOver(pygame.mouse.get_pos()) and butt.show:
                    perform_button_operation(butt)
                    # pygame.time.delay(20)
exit()
