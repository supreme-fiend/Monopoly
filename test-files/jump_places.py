# Another test owing to the fact that I'm new at Pygame
# Goal: To make an array of places and get a peg to jump from place to place
# The array is going to be a straight one, because we've already established that getting the peg to
# go around the whole loop is possible

import pygame

pygame.init()

win = pygame.display.set_mode((1000, 500))

win.fill((255,255,255))

pygame.display.set_caption("Peg jump test")

board = []


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
        board[self.pos].players_on_square.remove(self)
        board[self.pos+dice_no].players_on_square.append(self)
        self.pos += dice_no

    def single_turn(self):
        pygame.time.delay(10000)
        if self.pos <= 10:
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render("THIS IS A TURN. PRESS ENTER TO MOVE ONCE FORWARD", True, (0, 0, 0), (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (50, 300)
            win.blit(text, textRect)
            kys = pygame.key.get_pressed()
            if kys[pygame.K_RETURN]:
                self.move_peg(1)
                return
            pygame.display.update()
        else:
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render("CAN'T MOVE ANYMORE. PRESS ENTER TO CONTINUE", True, (0, 0, 0), (255, 0, 0))
            textRect = text.get_rect()
            textRect.center = (50, 300)
            win.blit(text, textRect)
            kys = pygame.key.get_pressed()
            if kys[pygame.K_RETURN]:
                return
            pygame.display.update()


def print_board():
    pos = 40
    for place in board:
        pygame.draw.rect(win, (0, 0, 0), (pos, 40, 80, 110))
        pygame.draw.rect(win, (255, 255, 255), (pos+10, 50, 65, 95))
        playerpos = 55
        for peg in place.players_on_square:
            pygame.draw.circle(win, peg.colour, (pos+25, playerpos), 5, 1)
            playerpos += 12
        pos += 80
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

peg1 = Peg((255, 0, 0))
peg2 = Peg((0, 255, 0))
peg3 = Peg((0, 0, 255))

peg2.move_peg(7)
peg3.move_peg(4)

run = True

turn_count = 1

while run:
    pygame.time.delay(1000)
    print_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN] and turn_count == 1:
        peg1.move_peg(1)
        turn_count = 2
        pygame.display.update()
        continue
    if keys[pygame.K_RETURN] and turn_count == 2:
        peg2.move_peg(1)
        turn_count = 3
        pygame.display.update()
        continue
    if keys[pygame.K_RETURN] and turn_count == 3:
        peg3.move_peg(1)
        turn_count = 1
        pygame.display.update()
        continue
    pygame.display.update()

exit()

