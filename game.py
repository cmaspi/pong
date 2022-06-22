import time 
from typing import Tuple
import pygame
import sys

class game:
    def __init__(self,
                fps : int = 60,
                w : int = 1440,
                h : int = 810,
                caption : str = 'Pong'
                ) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.w = w
        self.h = h
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(caption)

        # Initializing the ball
        d = 30  # diameter
        v = (10,)*2  # speed of the ball

        self.ball = Ball(d, self.w, self.h, *v)
        self.player = Human((10, 140), w-30, h//2, 7)
        self.opponent = AI((10,140), 20, h//2, 12)
    

    def run(self):

        player_speed = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        player_speed = self.player.v
                    if event.key == pygame.K_UP:
                        player_speed = -self.player.v
                if event.type == pygame.KEYUP:
                    # if event.key == pygame.K_DOWN:
                    #     player_speed = 0
                    # if event.key == pygame.K_UP:
                    player_speed = 0

            # Ball animation
            self.ball.animation(self.screen, self.player, self.opponent, self.h, self.w)
            self.player.move(player_speed, self.h)
            self.opponent.move(self.ball.ball, self.h)


            # Updating the window
            pygame.display.flip()
            # fps
            self.clock.tick(self.fps)


class Ball:
    BLACK = (0,)*3
    WHITE = (255,)*3
    GREY = (200,)*3

    def __init__(self, 
                d : int,
                x : int,
                y : int,
                v_x : int = 7,
                v_y : int = 7 
                ) -> None:
        """generates a ball in pygame

        Args:
        -----
            d (int): diameter of the ball
            x (int): initial x coordinate of the ball
            y (int): initial y coordinate of the ball
            v_x (int, optional): horizontal speed of the ball. Defaults to 7.
            x_y (int, optional): vertical speed of the ball. Defaults to 7.
        """
        self.ball = pygame.Rect(x//2 - d//2, y//2 - d//2, d, d)
        self.v_x = v_x
        self.v_y = v_y

    def animation(self, screen, player, opponent, h, w):
        
        # Drawing over the screen
        screen.fill( Ball.BLACK ) 
        # drawing the two players
        pygame.draw.rect(screen, Ball.WHITE , player.player)
        pygame.draw.rect(screen, Ball.WHITE, opponent.player)
        # drawing the ball
        pygame.draw.ellipse(screen, Ball.WHITE, self.ball)
        # drawing a centre line
        pygame.draw.aaline(screen, Ball.GREY, (w//2,0), (w//2,h))

        # moving the ball
        self.ball.x += self.v_x
        self.ball.y += self.v_y

        # checking for boundary
        if self.ball.top <= 0 or self.ball.bottom >= h:
            self.v_y *= -1
        if self.ball.left <= 0:
            self.v_x *= -1
            player.score += 1
            print(f'Player Score : {player.score} | Opponent Score : {opponent.score}')
            self.ball.center = (w//2, h//2)


        elif self.ball.right >= w:
            self.v_x *= -1
            opponent.score += 1
            print(f'Player Score : {player.score} | Opponent Score : {opponent.score}')
            self.ball.center = (w//2, h//2)
        
        # checking for collision with player or opponent
        if self.ball.colliderect(player.player) or self.ball.colliderect(opponent.player):
            self.v_x *= -1



class Player:
    def __init__(self,
                size : Tuple[int, int],
                x : int,
                y : int,
                v : int
                ) -> None:
        """
        generates a player in pygame

        Args:
        -----
            size (Tuple[int, int]): size of the board
            x (int): x coordinates of the player
            y (int): y coordinate of the player
            v (int): speed of the player
        """
        self.player = pygame.Rect(x, y, *size)
        self.v = v
        self.score = 0

class Human(Player):
    def __init__(self, size: Tuple[int, int], x: int, y: int, v: int) -> None:
        super().__init__(size, x, y, v)
    
    def move(self, player_speed : int, h : int):
        """
        moves the player in required direction
        Args:
        -----
            player_speed (int): speed of the player
            h (int): height of the screen
        """
        self.player.y += player_speed
        if self.player.top <= 0:
            self.player.top = 0
        elif self.player.bottom >= h:
            self.player.bottom = h

class AI(Player):
    def __init__(self, size: Tuple[int, int], x: int, y: int, v: int) -> None:
        super().__init__(size, x, y, v)

    def move(self, ball : Ball, h : int):
        if self.player.centery < ball.centery:
            self.player.top += self.v
        elif self.player.centery > ball.centery:
            self.player.top -= self.v
        if self.player.top <= 0:
            self.player.top = 0
        elif self.player.bottom >= h:
            self.player.bottom = h

if __name__ == '__main__':
    pong = game()
    pong.run()



        
    

        