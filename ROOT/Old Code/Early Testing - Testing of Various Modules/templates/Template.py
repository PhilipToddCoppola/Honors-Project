import pygame
 
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
 
def main():
    """ Main function for the game. """
    pygame.init()
      
    size = [700, 500]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("My Game")
 
    done = False
 
    clock = pygame.time.Clock()

def draw_snowman(screen, x, y):
    pygame.draw.ellipse(screen, WHITE, [35+x,0+y,25,25])
    pygame.draw.ellipse(screen, WHITE, [23+x,20+y,50,50])
    pygame.draw.ellipse(screen, WHITE, [0+x,65+y,100,100])

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
      
      
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
         
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
         

        screen.fill(BLACK)

        pygame.display.flip()
 
        clock.tick(20)

         
    pygame.quit()
 
if __name__ == "__main__":
    main()
