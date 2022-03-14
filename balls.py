'''Libraries'''
from math import sin, cos, sqrt
import pygame
pygame.init()

screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Bouncing Balls")
screen.fill((0,0,0))
clock = pygame.time.Clock()

ORIGIN_X = 500
ORIGIN_Y = 900

def draw_lines(ball1, ball2):
    '''Connects two balls'''
    pygame.draw.aaline(screen, (150,100,0), (ball1.pos_x, ball1.pos_y), (ball2.pos_x, ball2.pos_y))


class Ball:
    '''Creates a ball'''
    def __init__(self,radius,velocity):
        self.radius = radius
        self.velocity = velocity
        self.angle = 3.76
        self.pos_x = self.radius * (cos(self.angle)) + ORIGIN_X
        self.pos_y = (2 * self.radius) * (sin(self.angle)) + ORIGIN_Y
    def __del__(self):
        pass
    def move(self):
        '''Updates position of ball'''
        self.angle += self.velocity
        self.pos_x = self.radius * (cos(self.angle)) + ORIGIN_X
        self.pos_y = (2 * self.radius) * (sin(self.angle)) + ORIGIN_Y
    def draw(self):
        '''Draws the ball'''
        pygame.draw.circle(screen, (200, 100, 0), (self.pos_x, self.pos_y), 10)
    def collide(self):
        '''Checks for collision'''
        if self.pos_y - ORIGIN_Y >= (-abs(self.pos_x - ORIGIN_X)) - 10:
            self.velocity *= -1
BALLS = [Ball((150-(i*10)) + 200, (29/(1000 + (i * 24)))/100) for i in range(15,-1,-1)]
print(.029 * (6/8))
EXIT = False
TICKER = 0
while not EXIT:
    #clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            EXIT = True
    #render----------------------------------------------------------------
    screen.fill((0,0,0))
    pygame.draw.line(screen, (255,255,255), (ORIGIN_X,ORIGIN_Y), (ORIGIN_X - 400,ORIGIN_Y - 400), 2)
    pygame.draw.line(screen, (255,255,255), (ORIGIN_X,ORIGIN_Y), (ORIGIN_X + 400,ORIGIN_Y- 400), 2)
    # pygame.draw.line(screen, (255,255,255), (ORIGIN_X-400,ORIGIN_Y), (ORIGIN_X+400,ORIGIN_Y), 1)
    # pygame.draw.line(screen, (255,255,255), (ORIGIN_X,ORIGIN_Y-700), (ORIGIN_X,800), 1)
    for i in range(16):
        if i < 15:
            draw_lines(BALLS[i],BALLS[i+1])
    for balls in BALLS:
        balls.draw()
        balls.collide()
        balls.move()
    pygame.display.flip()
    TICKER += 1
pygame.quit()
