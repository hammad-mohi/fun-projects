import pygame
import random
import time
import math

# Constants
BG_COLOR = "black"
PLAYER_COLOR = "white"
POTTY_COLOR = "brown"
PLAYER_SIZE = 20
POTTY_SIZE = 20
BORDER_PADDING = 25

DIR_UP = "UP"
DIR_DOWN = "DOWN"
DIR_RIGHT = "RIGHT"
DIR_LEFT = "LEFT"

TIMEOUT = 0.04
GRID_SIZE = 20

# Initial setup
pygame.init()
pygame.display.set_caption('Snake Potty Chutharr')
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
font = pygame.font.Font('freesansbold.ttf', 18)

player_dir = DIR_RIGHT
player_pos = pygame.Vector2(screen.get_width() // 2, screen.get_height() // 2)
potty_pos = pygame.Vector2(screen.get_width() // 2, screen.get_height() // 2)
score = -1

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BG_COLOR)

    keys = pygame.key.get_pressed()

    # Using elsif to prevent diagonal motion
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_dir = DIR_UP
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_dir = DIR_DOWN
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_dir = DIR_LEFT
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_dir = DIR_RIGHT

    # Move the player
    if player_dir == DIR_UP and player_pos.y > BORDER_PADDING:
        player_pos.y -= GRID_SIZE
    elif player_dir == DIR_DOWN and player_pos.y < screen.get_height() - BORDER_PADDING:
        player_pos.y += GRID_SIZE
    elif player_dir == DIR_LEFT and  player_pos.x > BORDER_PADDING:
        player_pos.x -= GRID_SIZE
    elif player_dir == DIR_RIGHT and player_pos.x < screen.get_width() - BORDER_PADDING:
        player_pos.x += GRID_SIZE

    # TODOs:
    # // 0. Move in direction of last key
    # 1. Potty in random locations on the screen
    # 2. Following circles for snake as it grows
    # 3. Border to kill the snake
    # 4. Suicide detection - detect if snake kills itself
    # 5. Track and print score - on HUD
    # 6. Speed increase
    # 7. Settings for speed, maps
    # 8. Maps with interior walls
    # 9. Interior wall impact detection
    # 10. Highscores

    # Screens:
    # 1. Menu - Play, Settings, Quit
    # 2. Map Selection (Optional) - Select a Map
    # 3. Game Play - Play Game
    # 4. End Game - Die, Restart, Home

    # Draw HUD
    player_text = font.render(f"Player: ({player_pos.x}, {player_pos.y})", True, PLAYER_COLOR, BG_COLOR)
    potty_text = font.render(f"Potty: ({potty_pos.x}, {potty_pos.y})", True, POTTY_COLOR, BG_COLOR)
    score_text = font.render(f"Score: {score}", True, POTTY_COLOR, BG_COLOR)
    screen.blit(player_text, (0,0))
    screen.blit(potty_text, (0,20))
    screen.blit(score_text, (0,40))
    if abs(potty_pos.x - player_pos.x) <= GRID_SIZE and  abs(potty_pos.y - player_pos.y) <= GRID_SIZE:
        # Randomly reposition potty within the screen bounds, avoiding the border
        potty_pos = pygame.Vector2(
            random.random() * (screen.get_width() - BORDER_PADDING),
            random.random() * (screen.get_height() - BORDER_PADDING)
        )

        # Snap potty's x-coordinate to the nearest multiple of GRID_SIZE
        potty_pos.x = math.floor(potty_pos.x / GRID_SIZE) * GRID_SIZE
        # Snap potty's y-coordinate to the nearest multiple of GRID_SIZE
        potty_pos.y = math.floor(potty_pos.y / GRID_SIZE) * GRID_SIZE

        score += 1

    # Draw snake
    pygame.draw.circle(screen, PLAYER_COLOR, player_pos, PLAYER_SIZE)
    pygame.draw.circle(screen, POTTY_COLOR, potty_pos, POTTY_SIZE)

    # 1. Potty Generation

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    time.sleep(TIMEOUT)


pygame.quit()