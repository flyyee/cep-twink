import pygame
import random
pygame.init()

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
ORANGE      = (244, 118, 65)
BLUE     = (   0,   0, 255)
PURPLE   = ( 255,   0, 255)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

size = (SCREEN_WIDTH, SCREEN_HEIGHT)

class Ball:
    def __init__(self, x, y, gravityspeed, throwspeed, rotatespeed):
        self.color = ORANGE
        self.size = 50

        #ball
        self.ball_surface = pygame.Surface((self.size * 2, self.size * 2))
        #pygame.draw.circle(self.ball_surface, self.color, [self.size, self.size], self.size)
        #pygame.draw.line(self.ball_surface, WHITE, (0,0), (50, 0), 3)
        self.ball_surface.fill(BLACK)


        self.image = self.drawImage()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speeddown = gravityspeed
        self.speedright = throwspeed
        self.speedrot = rotatespeed
        self.currot = 0

        self.maxheight = x - 1


        self.orig_ball_surface = self.ball_surface.convert()


    def drawImage(self):
        pygame.draw.circle(self.ball_surface, self.color, [self.size, self.size], self.size)
        return self.ball_surface.convert()


    def draw(self,screen):
        screen.blit(self.ball_surface.convert(), self.rect)

    def update(self):
        if self.rect.x < SCREEN_WIDTH:
            self.rect.x += self.speedright
        else:
            return 69

        if self.rect.centery > self.maxheight:
            self.rect.y += self.speeddown
        else:
            self.speeddown *= -1
            self.rect.y += self.speeddown

        if self.rect.bottom > SCREEN_HEIGHT:
            #ball will change direction when it reaches the bottom
            self.speeddown *= -1
            self.maxheight = (SCREEN_HEIGHT - self.maxheight) * 0.25 + self.maxheight

        self.currot += self.speedrot

        currentcentre = self.rect.center
        self.ball_surface = pygame.transform.rotate(self.orig_ball_surface, self.currot)
        self.rect = self.ball_surface.get_rect(center=currentcentre)
        self.thecenter = self.ball_surface.get_rect().center

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bouncing Ball")

done = False

clock = pygame.time.Clock()

ball = Ball(0, 0, 5, 3, 2)

stop = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    if not stop:
        if ball.update() == 69:
            stop = True
        ball.draw(screen)
    else:
        pass
        # wait for input


    pygame.display.flip()

    clock.tick(60)

pygame.quit()