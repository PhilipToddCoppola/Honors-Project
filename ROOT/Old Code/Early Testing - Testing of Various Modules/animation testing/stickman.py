import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

def draw_stickman(screen,x,y):
       pygame.draw.ellipse(screen,BLACK, [1+x,y,10,10],0)
       pygame.draw.line(screen,BLACK,[5+x,17+y],[10+x,27+y],2)
       pygame.draw.line(screen,BLACK,[5+x,17+y],[x,27+y],2)
       pygame.draw.line(screen,RED,[5+x,17+y],[5+x,7+y],2)
       pygame.draw.line(screen,RED,[5+x,7+y],[9+x,17+y],2)
       pygame.draw.line(screen,RED,[5+x,7+y],[1+x,17+y],2)

pygame.init()
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Stickmen")
 
done = False
 
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

x_speed = 0
y_speed = 0

x_coord = 10
y_coord = 10

while not done:
       for event in pygame.event.get(): 
              if event.type == pygame.QUIT:
                     done = True
              if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_LEFT:
                            x_speed = -3
                     if event.key == pygame.K_RIGHT:
                            x_speed = 3
                     if event.key == pygame.K_UP:
                            y_speed = -3
                     if event.key == pygame.K_DOWN:
                            y_speed = 3

              if event.type == pygame.KEYUP:
                     if event.key == pygame.K_LEFT:
                            x_speed = 0
                     if event.key == pygame.K_RIGHT:
                            x_speed = 0
                     if event.key == pygame.K_UP:
                            y_speed = 0
                     if event.key == pygame.K_DOWN:
                            y_speed = 0
       x_coord += x_speed
       y_coord += y_speed

       if x_coord <= 0:
              x_coord = 0
       if x_coord >= 688:
              x_coord = 688

       if y_coord <= 0:
              y_coord = 0
       if y_coord >= 473:
              y_coord = 473
       pos = pygame.mouse.get_pos()
       
       x=pos[0]
       y=pos[1]


       screen.fill(WHITE)

       draw_stickman (screen,x,y)
       draw_stickman (screen,x_coord,y_coord)

       pygame.display.flip()

       
       
       clock.tick(60)
 
pygame.quit()
