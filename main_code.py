import random
import pygame
import os


pygame.init()
height = 800
width = 1400
screen = pygame.display.set_mode((width, height))

def write(text, x, y, size_t, color):
    font = pygame.font.SysFont("ebrima", size_t)
    rend = font.render(text, True, color)
    screen.blit(rend, (x, y))


display = "menu"


class Ladybird:
    def __init__(self, wi, he):
        self.x = random.randint(100, 1300)
        self.y = random.randint(100, 700)
        self.wi = wi
        self.he = he
        self.seen = pygame.Rect(self.x, self.y, self.wi, self.he)
        self.picture = pygame.image.load(os.path.join("ladybird.png"))
        self.o1 = random.randint(-1, 1)
        self.o2 = random.randint(-1, 1)
    def born(self):
        screen.blit(self.picture, (self.x, self.y))
    def move(self):
        self.x = self.x + self.o1
        self.y = self.y + self.o2
        self.seen = pygame.Rect(self.x, self.y, self.wi, self.he)
        if self.x <= 0 or self.x >= 1380:
            self.o1 = self.o1 * -1
        if self.y <= 0 or self.y >= 780:
            self.o2 = self.o2 * -1
    def colid(self, player1):
        if self.seen.colliderect(player1):
            return True
        else:
            return False

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wi = 30
        self.he = 30
        self.seen = pygame.Rect(self.x, self.y, self.wi, self.he)
        self.picture = pygame.image.load(os.path.join("player.png"))
    def born(self):
        screen.blit(self.picture, (self.x, self.y))
    def moving_y(self, m1):
        if self.y >= height - 5 or self.y <= 5:
            m1 *= -1
        self.y += m1
        self.seen = pygame.Rect(self.x, self.y, self.wi, self.he)
    def moving_x(self, m2):
        if self.x >= width - 5 or self.x <= 5:
            m2 *= -1
        self.x += m2
        self.seen = pygame.Rect(self.x, self.y, self.wi, self.he)

player = Player(700, 400)
logo = pygame.image.load(os.path.join("logo.png"))
m1 = 0
m2 = 0
points = 0
int(points)
ladybirds = []
for i in range(0, 10):
    ladybirds.append(Ladybird(20, 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if display == "gameplay":
                    m1 += -20
                    player.moving_y(m1)
                    m1 = 0
                    points += 1
            if event.key == pygame.K_DOWN:
                if display == "gameplay":
                    m1 += 20
                    player.moving_y(m1)
                    m1 = 0
                    points += 1
            if event.key == pygame.K_RIGHT:
                if display == "gameplay":
                    m2 += 20
                    player.moving_x(m2)
                    m2 = 0
                    points += 1
            if event.key == pygame.K_LEFT:
                if display == "gameplay":
                    m2 += -20
                    player.moving_x(m2)
                    m2 = 0
                    points += 1
            if event.key == pygame.K_SPACE:
                if display != "gameplay":
                    display = "gameplay"
                    player = Player(700, 400)
                    m1 = 0
                    m2 = 0
                    points = 0
                    ladybirds = []
                    for i in range(0, 10):
                        ladybirds.append(Ladybird(20, 20))
                    pygame.display.update()
    screen.fill((221, 167, 240))
    if display == "gameplay":
        for i in ladybirds:
            i.born()
            i.move()
            if i.colid(player.seen) == True:
                display = "end"
        player.born()
        write(str(points), 50, 50, 40, (44, 189, 102))
        pygame.display.update()
    elif display == "menu":
        write("Press SPACE to start the game", 350, 450, 50, (44, 189, 102))
        screen.blit(logo, (100, 100))
    elif display == "end":
        screen.blit(logo, (100, 100))
        write("YOU LOST! To resume the game press SPACE ", 200, 450, 50, (44, 189, 102))
        write("WOOOW! Your score is : " + str(points) + " points", 300, 600, 50, (44, 189, 102))
    pygame.display.update()
