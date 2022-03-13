'''Libraries'''
import math
import pygame
pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Bouncing Balls")
screen.fill((0,0,0))

class Ball:
    '''Creates a ball'''
    def __init__(self,x_pos,y_pos,):
        self.pos_x = x_pos
        self.pos_y = y_pos
    def __del__(self):
        pass
    def update(self,x_off,y_off):
        '''Updates position of ball'''
        self.pos_x += x_off
        self.pos_y += y_off
    def draw(self):
        '''Draws the ball'''
        pygame.draw.circle(screen, (200, 100, 0), (self.pos_x, self.pos_y), 10)
    def collide(self, x, y):
        '''Checks for collision'''
        if math.sqrt(((self.pos_x-x) * (self.pos_x-x)) + ((self.pos_y-y) * (self.pos_y-y))) <= 10:
            return True
        return False

BALLS = [Ball((90+(i*15))+12, (90+(i*15))+290) for i in range(16)]
EXIT = False
while not EXIT:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            EXIT = True
    #render----------------------------------------------------------------
    screen.fill((0,0,0))
    pygame.draw.line(screen, (255,255,255), (400,700), (50,350), 2)
    pygame.draw.line(screen, (255,255,255), (400,700), (750,350), 2)
    for balls in BALLS:
        balls.draw()
    pygame.display.flip()
pygame.quit()
