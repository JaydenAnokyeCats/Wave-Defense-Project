import pygame
import sys

class Game: 
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption('Defenders') # Creates window title
        
        self.screen = pygame.display.set_mode((900,700)) # Creates a window. Parameters are width(px) and height(px)
        
        self.clock = pygame.time.Clock() # Helps restrict frame rate
        
        self.display = pygame.Surface((900,700))
        
        # self.image_surface
        
        

        
    def run(self):
        running = True
        
        # Game Loop
        while running:
            self.display.fill((0,200,0)) # Placeholder method for me setting a background

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size())) #rwrrwwrwrrrwwrwrwrr
            pygame.display.update()
        
        
Game().run()