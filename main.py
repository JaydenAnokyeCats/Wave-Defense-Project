import pygame 
import sys
from utility import load_image, load_images # Functions residing in the utility folder

class Game: 
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption('Defenders') # Creates window title
        
        self.screen = pygame.display.set_mode((900,700)) # Creates a window. Parameters are width(px) and height(px)
        self.display = pygame.Surface((450,350))
        
        self.clock = pygame.time.Clock() # Helps restrict frame rate
        
        self.movement = [False, False]
        
        self.assets = {
            'player': load_image('player_sprites/xRXXModel.0012.png')
        }
        
        self.img_pos = [100, 200]
        
        # self.image_surface
        
        
        
    def run(self):
        running = True
        
        # Game Loop
        while running:
            
            self.display.fill((14,111,222)) # Placeholder method for me setting a background
            
            self.img_pos[1] += (self.movement[1] - self.movement[0]) #
            
            # Exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            # Movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
            
            # 
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()))
            self.screen.blit(self.assets['player'], self.img_pos) # Blits the image, and sets the image position on the screen
            
            pygame.display.update()
        
        
Game().run()