import pygame
import random
import os

pygame.init()

# Color definitions
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# defines the monitor's native resolution
NATIVEWIDTH = pygame.display.Info().current_w
NATIVEHEIGHT = pygame.display.Info().current_h

game_folder = os.path.dirname(__file__)  # gets current directory
asset_folder = os.path.join(game_folder, 'assets')  # gets assets fold from current directory

# Set the width and height of the screen [width, height]
size = (int(NATIVEWIDTH/4), int(NATIVEHEIGHT/1.75))  # this creates a rectangle
# with respect to the native resolution
# function wants int, not float, so conversion is necessary

screen = pygame.display.set_mode(size)  # sets the screen's size
pygame.display.set_caption("Twinkle Twinkle Little Star!")  # Set the window title

# class for the star's eye
class eye:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 45, 15)
        self.surface = pygame.Surface((45, 15))
        pygame.draw.rect(self.surface, BLACK, self.rect)
        self.surface.set_colorkey(WHITE)

    def draw(self, screen):
        screen.blit(self.surface, self.rect)


class star:
    def __init__(self):
        self.color = pygame.Color("yellow")  # uses pygame's inbuilt library of colours
        # loads asset as image
        self.image = pygame.image.load(os.path.join(asset_folder, 'star.jpg')).convert()

        # sets dimensions with respect to screen resolution
        # window's width and height is NATIVEWIDTH/4 and NATIVEHEIGHT/1.75 respectively
        # makes width and height half of the window's
        self.width = int(NATIVEWIDTH/4/2)
        self.height = int(NATIVEHEIGHT/1.75/2)

        # scales the asset to the correct size
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

        self.surface = pygame.Surface((int(NATIVEWIDTH/4), int(NATIVEHEIGHT/1.75)))
        self.image.set_colorkey(WHITE)

        # centres star in the middle of game window
        self.rect.centerx = self.width
        self.rect.centery = self.height
        self.xconst = self.rect.centerx
        self.yconst = self.rect.centery

        # creates star's left eye
        self.lorigeye = eye(100, 100).surface.convert()
        self.lmyeye = self.lorigeye
        self.lrot = 50

        # creates star's right eye
        self.rorigeye = eye(100, 100).surface.convert()
        self.rmyeye = self.rorigeye
        self.rrot = 310

    def draw(self, screen, rot=False, ang=0):
        # method has a default parameter of rot(ation) and ang(le of rotation)
        # these are used if one wants to rotate the star when drawing it
        if rot:
            # gets the original image of the star
            origimg = self.image
            # saves the center of the original image
            origcenter = origimg.convert().get_rect().center
            # gets the rotated image
            newimg = pygame.transform.rotate(origimg, ang)
            # sets the rotated image's center to the saved center
            newimg.convert().get_rect().center = origcenter
            screen.blit(newimg, self.rect)
        else:
            # no rotation
            screen.blit(self.image, self.rect)

        # blits the star's eyes
        screen.blit(self.lmyeye, (self.xconst - 50, self.yconst - 50))
        screen.blit(self.rmyeye, (self.xconst + 15, self.yconst - 50))

    def rageslowly(self):
        # method makes the star appear angrier stage by stage
        # it does this by making the star a deeper and deeper shade of red
        # increasing its size
        # changing the angle of its eyes (intimidation)

        # expands star
        self.width += 50
        self.height += 50
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect.inflate_ip(50, 50)  # increases size of rect while locking the centre

        pixels = pygame.PixelArray(self.image)  # creates a pixel array which you can use to replace
        # pixels of certain colours

        # replaces color of star accordingly
        if (self.color == pygame.Color("yellow")):
            self.color = pygame.Color("gold")
            pixels.replace(pygame.Color("yellow"), pygame.Color("gold"))
        elif (self.color == pygame.Color("gold")):
            self.color = pygame.Color("coral")
            pixels.replace(pygame.Color("gold"), pygame.Color("coral"))
        elif (self.color == pygame.Color("coral")):
            self.color = pygame.Color("tomato")
            pixels.replace(pygame.Color("coral"), pygame.Color("tomato"))
        elif (self.color == pygame.Color("tomato")):
            self.color = pygame.Color("orangered")
            pixels.replace(pygame.Color("tomato"), pygame.Color("orangered"))
        elif (self.color == pygame.Color("orangered")):
            self.color = pygame.Color("indianred")
            pixels.replace(pygame.Color("orangered"), pygame.Color("indianred"))
        elif (self.color == pygame.Color("indianred")):
            self.color = pygame.Color("firebrick")
            pixels.replace(pygame.Color("indianred"), pygame.Color("firebrick"))
        elif (self.color == pygame.Color("firebrick")):
            self.color = pygame.Color("red")
            pixels.replace(pygame.Color("firebrick"), pygame.Color("red"))
        del pixels
        # makes star redder, making it look angrier

        # rotates left eye until a certain angle is reached
        if self.lrot <= 50 or self.lrot >= 295:
            self.lmyeye = pygame.transform.rotate(self.lorigeye, self.lrot)
            self.lmyeye.get_rect().center = self.lorigeye.get_rect().center  # rotates around the center
            self.lrot = (self.lrot - 25) % 360  # keeps the angle under 360 using modulo

        # rotates right eye until a certain angle is reached
        if self.rrot <= 65 or self.rrot >= 310:
            self.rmyeye = pygame.transform.rotate(self.rorigeye, self.rrot)
            self.rmyeye.get_rect().center = self.rorigeye.get_rect().center  # rotates around the center
            self.rrot = (self.rrot + 25) % 360  # keeps the angle under 360 using modulo

    def reset(self, x, y):
        # method resets the star to its orginal state
        # takes a x and y coordinate as inputs

        # resets color
        self.color = pygame.Color("yellow")
        self.image = pygame.image.load(os.path.join(asset_folder, 'star.jpg')).convert()
        # resets dimensions
        self.width = int(NATIVEWIDTH / 4 / 2)
        self.height = int(NATIVEHEIGHT / 1.75 / 2)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

        self.surface = pygame.Surface((int(NATIVEWIDTH / 4), int(NATIVEHEIGHT / 1.75)))
        self.image.set_colorkey(WHITE)

        # centres star at x and y coordinates
        self.rect.centerx = x
        self.rect.centery = y
        self.xconst = self.rect.centerx
        self.yconst = self.rect.centery

        self.lorigeye = eye(100, 100).surface.convert()
        self.lmyeye = self.lorigeye
        self.lrot = 50

        self.rorigeye = eye(100, 100).surface.convert()
        self.rmyeye = self.rorigeye
        self.rrot = 310








# class for options
# creates a box with text as a sprite
class optionbox(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, text, textcolor, alpha):
        # color is the color of the box, textcolor is the color of the text
        # alpha is the transparency of the box, ranging from 0 (transparent) to 255 (opaque)
        pygame.sprite.Sprite.__init__(self)  # initialises sprite
        pygame.font.init()  # initialises fonts
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.center = (x, y)
        self.surface = pygame.Surface((width, height))
        self.surface.fill(color)
        self.surface.set_colorkey(WHITE)
        self.surface.set_alpha(alpha)
        self.caption = text
        self.captioncolor = textcolor
        pygame.draw.rect(self.surface, self.color, self.rect)

        self.image = self.surface.convert()

    def update(self):
        # writes the text onto the box
        self.font = pygame.font.SysFont('Comic Sans MS', 25)
        self.text = self.font.render(self.caption, True, self.captioncolor)
        self.textrect = self.text.get_rect()
        self.textrect.center = self.rect.center  # centers text
        screen.blit(self.text, (self.textrect.x, self.textrect.y))







# class for bomb, representing lives
class bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # sets asset as image
        self.image = pygame.image.load(os.path.join(asset_folder, 'bomb.png')).convert()
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.image.set_colorkey(WHITE)

        # becomes nearly transparent to denote being inactive
        self.image.set_alpha(50)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def draw(self, screen):
        screen.blit(self.image, self.rect)








# class for head, to be used in the body class
class head(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.Surface((80, 80))
        self.surface.fill(WHITE)
        self.surface.set_colorkey(WHITE)
        # draws the circle
        pygame.draw.circle(self.surface, BLACK, [40, 40], 40)

        self.image = self.surface.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # targetx is the target x coordinate for the head to fly to
        self.targetx = x
        while abs(x - self.targetx < 100):  # ensures end result is far enough so that the head visibly moves
            self.targetx = random.randint(0, int(NATIVEWIDTH/4))
            # gets random value on the x axis of the window, which width is NATIVEWIDTH/4
        self.moveamtx = random.randint(1, 10)  # sets movespeed on the x axis
        self.moveamty = random.randint(1, 10)  # sets movespeed on the y axis

# class for limbs (body, hands, legs), to be used in the body class
class limbs(pygame.sprite.Sprite):
    def __init__(self, x, y, x2, y2):
        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.Surface(size)
        self.surface.fill(WHITE)
        self.surface.set_colorkey(WHITE)
        # draws line, representing limb
        pygame.draw.line(self.surface, BLACK, (x, y), (x2, y2), 3)
        self.image = self.surface.convert()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.targetx = x
        # targetx is the target x coordinate for the head to fly to
        while abs(x - self.targetx) < 100:  # ensures end result is far enough
            self.targetx = random.randint(0, int(NATIVEWIDTH / 4))
            # gets random value on the x axis of the window, which width is NATIVEWIDTH/4
        self.moveamtx = random.randint(1, 10)  # sets movespeed on the x axis
        self.moveamty = random.randint(1, 10)  # sets movespeed on the y axis

# class for a person, houses a head and five limbs (body, left hand, right hand, left leg, right leg)
class person():
    def __init__(self, x, y):
        # takes x and y coordinate as input for the position of the head
        self.surface = pygame.Surface((200, 200))
        self.surface.fill(WHITE)
        self.surface.set_colorkey(WHITE)

        # position of head determined by x and y coordinates
        self.myhead = head(x, y)
        # assigns position of limbs relative to position of head
        self.body = limbs(x, y+40, x, y+40+80)
        self.lhand = limbs(x-40, y+100, x, y+60)  # left hand
        self.rhand = limbs(x+40, y+100, x, y+60)  # right hand
        self.lleg = limbs(x, y+40+80, x-40, y+40+80+40)  # left leg
        self.rleg = limbs(x, y + 40 + 80, x + 40, y + 40 + 80 + 40)  # right leg

        self.parts = pygame.sprite.Group()  # creates a sprite group for body parts
        # adds all the body parts (including head and body) into the body parts sprite group
        self.parts.add(self.myhead)
        self.parts.add(self.body)
        self.parts.add(self.lhand)
        self.parts.add(self.rhand)
        self.parts.add(self.lleg)
        self.parts.add(self.rleg)

    def draw(self):
        self.parts.draw(screen)  # draws all the body parts in the sprite group
        for part in self.parts:  # does this for every body part in the sprite group
            if part.rect.x < part.targetx:  # if target x coordinate of part is
                # to the left, part will move to the left
                # part moves down at the same time
                # part moves along each axis at its predetermined, random speed
                part.rect.move_ip(-part.moveamtx, part.moveamty)
            else:
                # to the right, part will move to the right
                # part moves down at the same time
                # part moves along each axis at its predetermined, random speed
                part.rect.move_ip(part.moveamtx, part.moveamty)






done = False  # Loop until the user clicks the close button.
clock = pygame.time.Clock()  # Used to manage how fast the screen updates
mystar = star()  # main star
all_sprites = pygame.sprite.Group()  # sprite group for general sprites (mainly optionboxes)
all_bombs = pygame.sprite.Group()  # sprite group for bombs

# loads soundtrack
pygame.mixer.music.load(os.path.join(asset_folder, 'twink.mp3'))
# plays soundtrack on loop
pygame.mixer.music.play(-1)

scene = 0  # sets the scene number
scenehandled = False  # determines if that scene has been prepared

# main loop of game
while not done:
    # first time scene setup
    if not scenehandled:  # checks if scene is handled,
        # if not handled, means the scene is appearing for the first time and needs to be handled
        # storyboarding
        if scene == 0:
            screen.fill(pygame.Color("royalblue"))
            caption = "You go for a trip, into the clouds."
            text = pygame.font.SysFont('Verdana', 25).render(caption, True, BLACK)
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            screen.blit(text, (textrect.x, textrect.y - 250))
            pygame.display.flip()

            pygame.time.wait(2000)  # pauses for 2 seconds

            caption = "You see what you expect to see."
            text = pygame.font.SysFont('Verdana', 25).render(caption, True, BLACK)
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            screen.blit(text, (textrect.x, textrect.y - 200))
            pygame.display.flip()

            pygame.time.wait(2000)  # pauses for 2 seconds

            caption = "You see a sea of stars."
            text = pygame.font.SysFont('Verdana', 25).render(caption, True, BLACK)
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            screen.blit(text, (textrect.x, textrect.y - 150))
            pygame.display.flip()

            pygame.time.wait(2000)  # pauses for 2 seconds

            caption = "But you also see..."
            text = pygame.font.SysFont('Verdana', 25).render(caption, True, BLACK)
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            screen.blit(text, (textrect.x, textrect.y - 100))
            pygame.display.flip()

            pygame.time.wait(5000)  # pauses for 5 seconds

            screen.fill(pygame.Color("royalblue"))
            caption = "one VERY VERY ANGRY star."
            text = pygame.font.SysFont('Verdana', 25).render(caption, True, BLACK)
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            screen.blit(text, (textrect.x, textrect.y - 250))
            pygame.display.flip()

            pygame.time.wait(3000)  # pauses for 3 seconds

            caption = "You go up and have a closer look..."
            text = pygame.font.SysFont('Verdana', 25).render(caption, True, BLACK)
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            screen.blit(text, (textrect.x, textrect.y - 200))
            pygame.display.flip()

            pygame.time.wait(5000)  # pauses for 5 seconds
            scene = 1
            mystar.reset(int(NATIVEWIDTH / 4 / 2), int(NATIVEHEIGHT / 1.75 / 2))

        elif scene == 1:

            words = ["Twinkle,", "twinkle,", "little", "star"]
            while words == ["Twinkle,", "twinkle,", "little", "star"]:  # ensures words are never in correct order
                random.shuffle(words)  # shuffles order of words

            # each optionbox contains a random, unique word
            # each optionbox is slightly transparent so that it does not block the background
            opt1 = optionbox(NATIVEWIDTH / 4 / 2, 100, 200, 50, pygame.Color("red"), words[0], WHITE, 100)
            opt2 = optionbox(NATIVEWIDTH / 4 / 2, 200, 200, 50, pygame.Color("red"), words[1], WHITE, 100)
            opt3 = optionbox(NATIVEWIDTH / 4 / 2, 300, 200, 50, pygame.Color("red"), words[2], WHITE, 100)
            opt4 = optionbox(NATIVEWIDTH / 4 / 2, 400, 200, 50, pygame.Color("red"), words[3], WHITE, 100)

            opts = [opt1, opt2, opt3, opt4, opt1, opt2, opt3, opt4]  # for use in cycling through options later

            # adds optionboxes to the sprite group for all sprites
            all_sprites.add(opt1)
            all_sprites.add(opt2)
            all_sprites.add(opt3)
            all_sprites.add(opt4)

            scenehandled = True  # sets scenehandled to true, so it does not redundantly re-setup the scene

        elif scene == 2:
            all_sprites.empty()
            # clears the all sprites sprite group first as it still contains the previous optionboxes
            screen.fill(pygame.Color("red"))
            pygame.time.wait(500)  # pauses for half a second
            pygame.display.flip()
            pygame.time.wait(500)  # pauses for half a second

            caption = "It's not very nice to"
            text = pygame.font.SysFont('Comic Sans MS', 25, bold=True).render(caption, True, WHITE)
            # bold for emphasis
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            screen.blit(text, (textrect.x, textrect.y))

            caption = "tap on people's faces!"
            text = pygame.font.SysFont('Comic Sans MS', 25, bold=True).render(caption, True, WHITE)
            # bold for emphasis
            screen.blit(text, (textrect.x, textrect.y + 30))

            pygame.display.flip()
            pygame.time.wait(4000)  # pauses for 4 seconds
            mystar.reset(400, 100)  # resets star from previous scene

            words = ["a MONSTER", "a Nice MONSTER"]
            random.shuffle(words)  # shuffles order of words

            # NATIVEWIDTH / 4 is the width of the window
            # width divided into two is the center of the window
            # each optionbox is equidistant from the center, approximately 120 pixels
            opt1 = optionbox(NATIVEWIDTH / 4 / 2 - 120, 450, 210, 75, pygame.Color("yellow"), words[0], BLACK, 200)
            opt2 = optionbox(NATIVEWIDTH / 4 / 2 + 120, 450, 210, 75, pygame.Color("yellow"), words[1], BLACK, 200)

            # adds the new optionboxes to the sprite group
            all_sprites.add(opt1)
            all_sprites.add(opt2)

            opts = [opt1, opt2, opt1]  # for use in cycling through options later

            counter = 0  # counts number of times player picks an option later
            caption = "How I wonder what you are?"
            text = pygame.font.SysFont('Comic Sans MS', 25, italic=True).render(caption, True, BLACK)
            # italicised to represent the lyrics
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center


            # draw 5 bombs to represent lives
            bomb1 = bomb(75, 550)
            bomb2 = bomb(150, 550)
            bomb3 = bomb(225, 550)
            bomb4 = bomb(300, 550)
            bomb5 = bomb(375, 550)

            # adds the bombs to the bomb sprite group
            all_bombs.add(bomb1)
            all_bombs.add(bomb2)
            all_bombs.add(bomb3)
            all_bombs.add(bomb4)
            all_bombs.add(bomb5)

            bombs = [bomb1, bomb2, bomb3, bomb4, bomb5]

            # rotation angle of the star
            rotang = 10
            rotangplus = False  # determines if the rotation angle should increase or decrease later

            scenehandled = True

        elif scene == 3:
            all_bombs.empty()  # empties bomb sprite group
            all_sprites.empty()  # empties sprite group
            screen.fill(WHITE)
            pygame.time.wait(500)  # pauses for half a second
            pygame.display.flip()
            pygame.time.wait(500)  # pauses for half a second

            caption = "boom"
            text = pygame.font.SysFont('Comic Sans MS', 15).render(caption, True, BLACK)
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            screen.blit(text, (textrect.x, textrect.y))
            pygame.display.flip()
            pygame.time.wait(2000)  # pauses for 2 seconds

            caption = "you've made me MAD >:C"
            text = pygame.font.SysFont('Comic Sans MS', 15).render(caption, True, BLACK)
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            screen.blit(text, (textrect.x, textrect.y + 30))
            pygame.display.flip()
            pygame.time.wait(4000)  # pauses for 4 seconds

            # loads the background image from the assets
            bg = pygame.image.load(os.path.join(asset_folder, 'starrynight.png')).convert()
            bg = pygame.transform.scale(bg, size)  # scales it to the size of the window (size)

            pygame.time.wait(2000)  # pauses for 2 seconds

            textsurface = pygame.Surface(size)  # surface soley for text
            textsurface.set_colorkey(WHITE)
            textsurface.fill(WHITE)

            caption = "Up above the world so high"
            text = pygame.font.SysFont('Comic Sans MS', 25, italic=True).render(caption, True, BLACK)
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            textsurface.blit(text, (textrect.x, textrect.y - 250))  # adds text to the text surface


            caption = "It'd be a pity if..."
            text = pygame.font.SysFont('Comic Sans MS', 25).render(caption, True, BLACK)
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            textsurface.blit(text, (textrect.x, textrect.y + 210))  # adds text to the text surface


            screen.blit(bg, (0, 0))  # blits the background
            screen.blit(textsurface, (0, 0))  # blits the text surface
            pygame.display.flip()
            pygame.time.wait(5000)  # pauses for 5 seconds

            caption = "one of us fell down"
            text = pygame.font.SysFont('Comic Sans MS', 25).render(caption, True, BLACK)
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            textsurface.blit(text, (textrect.x, textrect.y + 250))
            screen.blit(textsurface, (0, 0))
            pygame.display.flip()
            pygame.time.wait(4000)  # pauses for 4 seconds

            # creates a person whose x coordinate is in the center of the screen
            myperson = person(NATIVEWIDTH/4/2, 100)
            myperson.draw()
            pygame.display.flip()
            pygame.time.wait(1500)  # pauses for 1.5 seconds

            scenehandled = True

        elif scene == 4:
            screen.fill(WHITE)  # resets screen
            textsurface.fill(WHITE)  # resets text surface
            pygame.display.flip()
            pygame.time.wait(2000)  # pauses for 2 seconds

            caption = "bye"
            text = pygame.font.SysFont('Comic Sans MS', 15).render(caption, True, BLACK)
            screen.blit(text, (0, 0))  # blits into the top left corner of the screen
            pygame.display.flip()
            pygame.time.wait(2000)  # pauses for 2 seconds

            screen.fill(WHITE)  # resets screen

            caption = "Like a diamond in the sky"
            text = pygame.font.SysFont('Comic Sans MS', 25, italic=True).render(caption, True, BLACK)
            # italicised to represent lyrics
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            textsurface.blit(text, (textrect.x, textrect.y - 200))
            screen.blit(textsurface, (0, 0))

            pygame.display.flip()
            pygame.time.wait(3000)  # pauses for 3 seconds

            caption = "Bet you didn't know diamonds melt at"
            text = pygame.font.SysFont('Comic Sans MS', 25).render(caption, True, BLACK)
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            textsurface.blit(text, (textrect.x, textrect.y - 100))
            screen.blit(textsurface, (0, 0))

            # creates optionboxes
            opt1 = optionbox(int(NATIVEWIDTH/4/2-60), int(NATIVEHEIGHT/1.75-75), 75, 40, WHITE, "3300°c", pygame.Color("red"), 255)
            opt2 = optionbox(int(NATIVEWIDTH/4/2+60), int(NATIVEHEIGHT/1.75-75), 75, 40, WHITE, "Yes", pygame.Color("red"), 255)

            # adds optionboxes to sprite group
            all_sprites.add(opt1)
            all_sprites.add(opt2)

            opts = [opt1, opt2]  # list containing all the options to be used for checks later

            all_sprites.draw(screen)  # draws the optionboxes

            pygame.display.flip()
            pygame.time.wait(3000)  # pauses for 3 seconds

            scenetrigger = False  # determines if player has triggered and event in the scene (happening later)

            scenehandled = True

        elif scene == 5:
            all_sprites.empty()  # clears sprite group
            textsurface.fill(WHITE)  # resets text surface

            caption = "Introducing, Fiar, my furnace."
            text = pygame.font.SysFont('Comic Sans MS', 25).render(caption, True, BLACK)
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            textsurface.blit(text, (textrect.x, textrect.y - 200))
            screen.blit(textsurface, (0, 0))
            pygame.display.flip()

            pygame.time.wait(2000)  # pauses for 2 seconds

            caption = "You've been annoying me long enough,"
            text = pygame.font.SysFont('Comic Sans MS', 25).render(caption, True, BLACK)
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            textsurface.blit(text, (textrect.x, textrect.y - 150))
            screen.blit(textsurface, (0, 0))
            pygame.display.flip()

            pygame.time.wait(2000)  # pauses for 2 seconds

            caption = "it's time to put us all out of our misery."
            text = pygame.font.SysFont('Comic Sans MS', 25).render(caption, True, BLACK)
            textrect = text.get_rect()
            textrect.center = screen.get_rect().center
            textsurface.blit(text, (textrect.x, textrect.y - 100))
            screen.blit(textsurface, (0, 0))
            pygame.display.flip()

            pygame.time.wait(10000)  # pauses for 10 seconds
            scene = 0  # resets game



    # event loop
    for event in pygame.event.get():  # user did something
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q): # If user clicked close
            done = True # changes flag to exit the loop
        # scene specific if-statements
        if scene == 1:
            if event.type == pygame.MOUSEBUTTONUP:  # mouse click detected
                mystar.rageslowly()  # makes star angrier
                pos = pygame.mouse.get_pos()  # gets position of mouse click
                clicked_sprite = [s for s in all_sprites if s.rect.collidepoint(pos)]
                # gets all sprites whose position was clicked on by at that mouse position
                if clicked_sprite:  # checks if there are clicked sprites, returns false if empty
                    if clicked_sprite[0] in opts:  # checks if the clicked sprite is part of the listopts
                        # which contains opt1 to opt4
                        oldcapt = clicked_sprite[0].caption  # sets the previous caption
                        newcapt = opts[opts.index(clicked_sprite[0])+3].caption  # gets the new caption
                        # finds the optionbox in the list of optionboxes, opts, and gets its index
                        # gets the caption of the optionbox 3 indexes after
                        # there are 7 elements in the list to mirror a loop
                        clicked_sprite[0].caption = newcapt  # sets the clicked optionbox's caption to the new caption
                        opts[opts.index(clicked_sprite[0]) + 3].caption = oldcapt  # changes the affected optionbox's caption
                        # this effectively switches the places of captions of the optionbox the player clicks on,
                        # and the one three after it (aka one behind it)
                        correctorder = ["Twinkle,", "twinkle,", "little", "star"]  # correct order of the words
                        if [opt1.caption, opt2.caption, opt3.caption, opt4.caption] == correctorder:
                            # checks if the options are ordered correctly
                            scene = 2  # proceeds to the next scene
                            scenehandled = False  # the new scene needs to be handled, so flag is set to false

        elif scene == 2:
            if event.type == pygame.MOUSEBUTTONUP:  # mouse click
                pos = pygame.mouse.get_pos()  # mouse click position
                clicked_sprite = [s for s in all_sprites if s.rect.collidepoint(pos)]  # gets all clicked sprites
                if clicked_sprite:  # checks if there are clicked sprites
                    if clicked_sprite[0] in opts:
                        if clicked_sprite[0].caption == "a MONSTER":
                            # if player clicked on "a MONSTER", star becomes angrier
                            mystar.rageslowly()
                            # activates (makes opaque) another bomb
                            bombs[counter].image.set_alpha(255)
                            # increases the counter to the number of activated bombs
                            counter += 1
                            if counter == 5:  # scene ends when 5 bombs are activated, denoting 5 lives for the player
                                scene = 3  # new scene
                                scenehandled = False  # resets scene handling

                        # switches places of captions if correct and if wrong
                        oldcapt = clicked_sprite[0].caption
                        newcapt = opts[opts.index(clicked_sprite[0])+1].caption
                        # gets index of clicked sprite in list of sprites
                        # the other element in the list is the other sprite
                        clicked_sprite[0].caption = newcapt
                        opts[opts.index(clicked_sprite[0])+1].caption = oldcapt

        elif scene == 3:
            pass

        elif scene == 4:
            if event.type == pygame.MOUSEBUTTONUP:  # mouse click
                pos = pygame.mouse.get_pos()  # mouse position
                clicked_sprite = [s for s in all_sprites if s.rect.collidepoint(pos)]  # clicked sprites
                if clicked_sprite:  # checks if there are clicked sprites
                    if clicked_sprite[0] in opts:
                        if not scenetrigger:  # loads next part of scene, scenetrigger is false only when
                            # user has picked the right option and has progressed
                            if clicked_sprite[0].caption == "3300°c":  # if the correct option is clicked,
                                # flag is triggered
                                caption = "Human bodies melt at 1500c."
                                text = pygame.font.SysFont('Comic Sans MS', 25).render(caption, True, BLACK)
                                textrect = text.get_rect()
                                textrect.center = screen.get_rect().center
                                textsurface.blit(text, (textrect.x, textrect.y))
                                scenetrigger = True  # triggers flag to signify carrying on to the next part of the scene
                        else:
                            if clicked_sprite[0].caption == "Yes":
                                scene = 5  # next scene
                                scenehandled = False  # resets scene handling



    # scene specific drawing
    # order is as such to prevent wrong overlapping

    # only proceeds with drawing the scene if scene has been handled

    if scene == 1 and scenehandled:
        mystar.draw(screen)  # draws main star

    if scene == 2 and scenehandled:
        # sets rotation angle to bounced between -10 and 10
        if rotang == -10:
            rotangplus = True  # rotation angle should increase
        if rotang == 10:
            rotangplus = False  # rotation angle should decrease
        if rotangplus:
            rotang += 1
        else:
            rotang -= 1
        mystar.draw(screen, True, rotang)  # draws and rotates main star

    if scenehandled:
        all_sprites.update()
        all_sprites.draw(screen)  # draws sprites


    # scene specific draws
    if scene == 2 and scenehandled:
        screen.blit(text, (textrect.x + 20, textrect.y))  # keeps text on screen
        all_bombs.draw(screen)  # draws bombs

    if scene == 3 and scenehandled:
        screen.blit(bg, (0, 0))  # blits the background
        screen.blit(textsurface, (0, 0))  # keeps text surface (containing texts) on screen
        myperson.draw()  # draws the person (and its body parts)


        # waits for all parts to be out of frame
        sceneover = True
        for part in myperson.parts:
            if part.rect.centerx > 0 and part.rect.centerx < int(NATIVEWIDTH/4):
                if part.rect.centery < int(NATIVEHEIGHT/1.75):
                    sceneover = False
                    break  # stops the check as long as there is one body part still in the window

        if sceneover:
            scene = 4  # goes to next scene
            scenehandled = False  # resets scene handling

    if scene == 4 and scenehandled:
        screen.blit(textsurface, (0, 0))  # blits text surface (containing texts) to screen

    pygame.display.flip()

    screen.fill(WHITE)  # resets screen to white

    # limits game to 30 frames per second
    clock.tick(30)

# ends game when main loop is exited (done flag is true)
pygame.quit()