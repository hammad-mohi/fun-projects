import pygame
import random

# Constants
BG_COLOR = "black"
PLAYER_COLOR = "white"
POTTY_COLOR = "brown"
BORDER_PADDING = 25

# Initial setup
pygame.init()
pygame.display.set_caption('Snake Potty Chutharr')
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
potty_pos = pygame.Vector2(random.random() * (screen.get_width() - BORDER_PADDING), random.random() * (screen.get_height() - BORDER_PADDING))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw snake
    pygame.draw.circle(screen, PLAYER_COLOR, player_pos, 20)
    # pygame.draw.circle(screen, POTTY_COLOR, potty_pos, 20)

    keys = pygame.key.get_pressed()

    # Using elsif to prevent diagonal motion
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if player_pos.y > BORDER_PADDING:
            player_pos.y -= 300 * dt
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if player_pos.y < screen.get_height() - BORDER_PADDING:
            player_pos.y += 300 * dt
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if player_pos.x > BORDER_PADDING:
            player_pos.x -= 300 * dt
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if player_pos.x < screen.get_width() - BORDER_PADDING:
            player_pos.x += 300 * dt

    # TODOs:
    # 0. Move in direction of last key
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


    # 1. Potty Generation

    pygame.draw.circle(screen, PLAYER_COLOR, player_pos, 20)




    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(120) / 1000

pygame.quit()