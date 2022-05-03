import pygame, sys

# SETUP
# Game Logic and Data

# LOOP
# Drawing
# Updating


# PS: LOOK UP PYGAME LIST OF LOCALS
# ---------------------
# General setup
pygame.init()
clock = pygame.time.Clock()
# This generally sets up the game

# Setting up the main window
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

background_color = pygame.Color("dim gray")
alice_blue = (240, 248, 255)

ball_speed_x = 7
ball_speed_y = 7

# Always remember to adjust desired window size
# In this case, we will use a width of 800 x 500


while True:
    # Handling input
    # This creates an exit strategy in case user wants to quit game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Animations
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Vertical or X Axis
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    # Horizontal or Y Axis
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    # Visuals
    screen.fill(background_color)
    pygame.draw.rect(screen, alice_blue, player)
    pygame.draw.rect(screen, alice_blue, opponent)
    pygame.draw.ellipse(screen, alice_blue, ball)
    pygame.draw.aaline(
        screen, alice_blue, (screen_width / 2, 0), (screen_width / 2, screen_height)
    )

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
