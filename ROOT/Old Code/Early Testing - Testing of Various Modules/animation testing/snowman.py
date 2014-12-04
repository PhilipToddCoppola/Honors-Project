import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

def draw_snowman(screen,x,y):
       pygame.draw.ellipse(screen,WHITE, [35+x,0+y,25,25])
       pygame.draw.ellipse(screen,WHITE, [23+x,20+y,50,50])
       pygame.draw.ellipse(screen,WHITE, [0+x,65+y,100,100])

pygame.init()
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False
 
clock = pygame.time.Clock()
 
while not done:
       for event in pygame.event.get(): 
              if event.type == pygame.QUIT:
                     done = True
                     
       pos = pygame.mouse.get_pos()
       print(pos)
       screen.fill(BLACK)

       draw_snowman(screen,100,100)
       draw_snowman(screen, 10,10)
       draw_snowman(screen, 300, 30)

       pygame.display.flip()
 
       clock.tick(60)
 
pygame.quit()
