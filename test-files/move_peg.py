# Simple PyGame test to see whether a small token can move around a board
# This program really gave me the hang of pygame.
# Some small issues, but it served the testing purpose.

import pygame
import random

pygame.init()


class Peg:

    def __init__(self):
        self.pos_x = 40
        self.pos_y = 40

    def move_peg(self, dn):
        if self.pos_y == 40:
            if self.pos_x + 20*dn < 610:
                self.pos_x += 20*dn
            elif self.pos_x + 20*dn >= 610:
                rem_dn = int((610 - self.pos_x)/20)
                self.pos_x = 610
                self.pos_y += rem_dn*20
        if self.pos_y == 410:
            if self.pos_x - 20*dn >= 40:
                self.pos_x -= 20*dn
            else:
                rem_dn = int(self.pos_x/20)
                self.pos_x = 40
                self.pos_y -= rem_dn*20
        elif self.pos_y > 40 and self.pos_y < 410:
            if self.pos_x == 610:
                if self.pos_y + 20*dn >= 410:
                    rem_dn = int((410-self.pos_y) / 20)
                    self.pos_y = 410
                    self.pos_x -= rem_dn*20
                else:
                    self.pos_y += 20*dn
            elif self.pos_x == 40:
                if self.pos_y - 20*dn <= 0:
                    rem_dn = int(self.pos_y / 20)
                    self.pos_y = 0
                    self.pos_x += rem_dn*20
                else:
                    self.pos_y -= 20*dn

    def print_peg(self):
        pygame.draw.circle(win, (255, 0, 0), (self.pos_x, self.pos_y), 5, 1)


win = pygame.display.set_mode((700, 700))
win.fill ((255,255,255))
pygame.display.set_caption("MOVE THE PEG AROUND")


def print_plain_board():
    pygame.draw.rect(win, (0, 0, 0), (30, 30, 600, 400))
    pygame.draw.rect(win, (255, 255, 255), (70, 70, 520, 320))


p = Peg()

run = True
print_plain_board()
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render("Press ENTER to Roll Dice", True, (0,0,0), (255,0,0))
textRect = text.get_rect()
textRect.center = (50, 500)
win.blit(text, textRect)
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        dice_no = random.randint(1, 6)
        p.move_peg(dice_no)
    win.fill((255, 255, 255))
    print_plain_board()
    p.print_peg()
    pygame.display.update()
