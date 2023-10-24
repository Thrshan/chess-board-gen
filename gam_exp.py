
import pygame
import random

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEMOTION,
    MOUSEBUTTONUP
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

running = True
clock = pygame.time.Clock()

# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("./pieces/chess.com/68747470733a2f2f696d616765732e6368657373636f6d66696c65732e636f6d2f63686573732d7468656d65732f7069656365732f6e656f2f3235362f626b2e706e67.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -2)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 2)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-2, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(2, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def move(self, pos_X, pos_Y, x_off, y_off):
        self.rect.left = pos_X - x_off
        self.rect.top = pos_Y - y_off

    def get_pos(self):
        return self.rect.left, self.rect.top

# Instantiate player. Right now, this is just a rectangle.
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(2, 20)
    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

player = Player()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

pressed = False
x_off, y_off = 0, 0

while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == MOUSEMOTION:
            if pressed:
                player.move(event.__dict__['pos'][0], event.__dict__['pos'][1], x_off, y_off)
                
        elif event.type == MOUSEBUTTONDOWN:
            x, y = player.get_pos()
            x_off = event.__dict__['pos'][0] - x
            y_off = event.__dict__['pos'][1] - y
            print(x,y)
            print(x_off, y_off)
            pressed = True

            print(pygame.mouse.get_pressed()[0])
            print(player.rect.collidepoint(pygame.mouse.get_pos()))

        elif event.type == MOUSEBUTTONUP:
            pressed = False


    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    # Update enemy position
    enemies.update()

    

    screen.fill((0, 0, 0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # if pygame.sprite.spritecollideany(player, enemies):
    #     player.kill()
    #     running = False

    pygame.display.flip()
    clock.tick(60)
