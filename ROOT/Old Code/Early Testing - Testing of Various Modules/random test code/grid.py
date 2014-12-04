import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

pygame.init()
 
size = (255, 255)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Grid")

width = 20
height = 20
margin = 5

grid = []
for row in range(10):
       grid.append([])
       for column in range(10):
              grid[row].append(0)
              
done = False
 
clock = pygame.time.Clock()
 
while not done:
       for event in pygame.event.get(): 
              if event.type == pygame.QUIT:
                     done = True
              if event.type == pygame.MOUSEBUTTONDOWN:
                      pos = pygame.mouse.get_pos()
                      column_coords = pos[0] // (width + margin)
                      row_coords = pos[1] // (height + margin)
                      grid[row_coords][column_coords] = 1
                      print('Row:', row_coords, 'Column:', column_coords)
       screen.fill(BLACK)

       for row in range(10):
              for column in range(10):
                     color = WHITE
                     if grid[row][column] == 1:
                            color = GREEN
                     pygame.draw.rect(screen,color,
                                      [(margin+width)*column+margin,
                                       (margin+height)*row+margin,width,height])
       pygame.display.flip()
 
       clock.tick(60)
 
pygame.quit()
