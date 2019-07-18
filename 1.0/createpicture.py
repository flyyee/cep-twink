import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SOMEKINDOFRED = (255, 0, 102)
ROPECOLOUR = (153, 102, 51)
RAIN = (51, 102, 255)

size = (400, 720)
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

#kite
kite = pygame.Surface((400, 400))
kite.fill(WHITE)
kite.set_colorkey(WHITE)
pygame.draw.polygon(kite, SOMEKINDOFRED, [[50,50], [250,75], [300,275], [100,250]], 0)
kiteorig = kite.convert()
rot = 0

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    rot += 10
    kite = pygame.transform.flip(kiteorig, True, False)
    kite = pygame.transform.rotate(kiteorig, rot)
    screen.blit(kite.convert(), (0, 0))


    #string
    pygame.draw.line(screen, ROPECOLOUR, [295, 270], [400, 700], 5)

    #psuedo random number
    for x in range(15):
        xcoord = random.randrange(350)
        ycoord = random.randrange(670)
        pygame.draw.ellipse(screen, RAIN, [xcoord, ycoord, 7, 20], 0)

    font = pygame.font.SysFont('Calibri', 25, True, False)
    #caption
    text = font.render("this kite is on fire", True, BLACK)
    screen.blit(text, [50, 250])

    pygame.display.flip()

    #give the cpu a break
    clock.tick(2)

pygame.quit()