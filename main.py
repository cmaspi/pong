import pygame
import sys

def ball_animation():
    global screen, player, opponent, screen_height, screen_width, ball_speed_x, ball_speed_y

    screen.fill((0,)*3)
    pygame.draw.rect(screen, (200,)*3, player)
    pygame.draw.rect(screen, (200,)*3, opponent)

    pygame.draw.ellipse(screen, (200,)*3, ball)
    pygame.draw.aaline(screen, (200,)*3, (screen_width//2,0), (screen_width//2, screen_height))

    screen.fill((0,)*3)
    pygame.draw.rect(screen, (200,)*3, player)
    pygame.draw.rect(screen, (200,)*3, opponent)

    pygame.draw.ellipse(screen, (200,)*3, ball)
    pygame.draw.aaline(screen, (200,)*3, (screen_width//2,0), (screen_width//2, screen_height))

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

# initializing the game
pygame.init()
clock = pygame.time.Clock()

# window
screen_width = 1080
screen_height = 810

# main screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

ball = pygame.Rect(screen_width//2-15, screen_height//2-15, 30, 30)
player = pygame.Rect(screen_width - 30, screen_height//2 - 70, 10, 140)
opponent = pygame.Rect(20, screen_height//2 - 70, 10, 140)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
        



    # Visuals
    
    ball_animation()
    player.y += player_speed
    opponent_speed = 15
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.top -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

    


    # Updating the window
    pygame.display.flip()
    # 90 fps
    clock.tick(60)

