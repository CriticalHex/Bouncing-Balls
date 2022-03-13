'''Libraries'''
from math import sin, cos, pi
import pygame
pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Bouncing Balls")
screen.fill((0,0,0))
clock = pygame.time.Clock()

def draw_lines(ball1, ball2):
    '''Connects two balls'''
    pygame.draw.aaline(screen, (150,100,0), (ball1.pos_x, ball1.pos_y), (ball2.pos_x, ball2.pos_y))


class Ball:
    '''Creates a ball'''
    def __init__(self,radius):
        self.radius = radius
        self.velocity = .0003
        self.angle = 3*pi/2
        self.pos_x = self.radius * (cos(self.angle)) + 400
        self.pos_y = self.radius * (sin(self.angle)) + 700
    def __del__(self):
        pass
    def move(self):
        '''Updates position of ball'''
        self.angle += self.velocity
        self.pos_x = self.radius * (cos(self.angle)) + 400
        self.pos_y = self.radius * (sin(self.angle)) + 700
        self.collide()
        self.draw()
    def draw(self):
        '''Draws the ball'''
        pygame.draw.circle(screen, (200, 100, 0), (self.pos_x, self.pos_y), 10)
    def collide(self):
        '''Checks for collision'''
        if self.pos_y - 700 >= (-abs(self.pos_x - 400)) - 10:
            self.velocity *= -1
            print(self.pos_x, self.pos_y)
BALLS = [Ball((i*25) + 100) for i in range(16)]
EXIT = False
while not EXIT:
    #clock.tick(6000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            EXIT = True
    #render----------------------------------------------------------------
    screen.fill((0,0,0))
    pygame.draw.line(screen, (255,255,255), (400,700), (50,350), 2)
    pygame.draw.line(screen, (255,255,255), (400,700), (750,350), 2)
    for i in range(len(BALLS)):
        if i < len(BALLS) - 1:
            draw_lines(BALLS[i],BALLS[i+1])
    for balls in BALLS:
        balls.move()
    pygame.display.flip()
pygame.quit()
