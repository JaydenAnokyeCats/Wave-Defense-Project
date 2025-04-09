import pygame 
import sys
from utility import load_image, load_images  # Functions residing in the utility folder


class Game: 
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption('Defenders')  # Creates window title
        
        self.screen = pygame.display.set_mode((900, 700))  # Window size
        self.display = pygame.Surface((450, 350))
        
        # self.top_collision = pygame.Rect(0, 0, 900, 50)  # Top edge
        # self.bottom_collision = pygame.Rect(0, 700 - 50, 900, 50)  # Bottom edge
        # self.left_collision = pygame.Rect(0, 0, 50, 700)  # Left edge
        # self.right_collision = pygame.Rect(900 - 50, 0, 50, 700)  # Right edge

        
        
        self.clock = pygame.time.Clock()  # Helps restrict frame rate
        
        self.movement = [False, False, False, False]
        
        self.assets = {
            'player': load_image('player_sprites/xRXXModel.0012.png'),
            'zombie': load_image('enemy_sprites/xRXXModel.0013.png'),
            'sword': load_image('weapons/sword.png'),
        }
        
        self.player_x = 100
        self.player_y = 200
        self.sword_x = 50
        self.sword_y = 550
        
        self.player_pos = [self.player_x, self.player_y]
        self.enemy_pos = [700, 300]
        self.sword_pos = [self.sword_x, self.sword_y]
        
        self.player_speed = 5
        self.enemy_speed = 2  
        
        # self.testing_collision_area = pygame.Rect(250 , 450, 100, 100)
        self.player_area = pygame.Rect(self.player_x, self.player_y, 1, 1)
        self.sword_area = pygame.Rect(self.sword_x, self.sword_y, 100, 100)
        
        self.sword_connected = False
        
        

    
    def run(self):
        running = True
        
        # Game Loop
        while running:
            offest_x = 25
            
            self.display.fill((14, 111, 222))  # Placeholder method for me setting a background
            
            
            if self.movement[0]:
                self.player_y -= self.player_speed  # Moves Up
            if self.movement[1]:
                self.player_x -= self.player_speed  # Moves Left
            if self.movement[2]:
                self.player_y += self.player_speed  # Moves Down
            if self.movement[3]:
                self.player_x += self.player_speed  # Moves Right
            
            self.player_pos = [self.player_x, self.player_y]
            
            
            # Exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.movement[0] = True
                    if event.key == pygame.K_a:
                        self.movement[1] = True
                    if event.key == pygame.K_s:
                        self.movement[2] = True
                    if event.key == pygame.K_d:
                        self.movement[3] = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.movement[0] = False
                    if event.key == pygame.K_a:
                        self.movement[1] = False
                    if event.key == pygame.K_s:
                        self.movement[2] = False
                    if event.key == pygame.K_d:
                        self.movement[3] = False
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()))
            self.screen.blit(self.assets['player'], self.player_pos) # Blits the image, and sets the image position on the screen
            self.player_area.update(self.player_x, self.player_y, 100, 100)
             
            self.screen.blit(self.assets['zombie'], self.enemy_pos) 
            self.screen.blit(self.assets['sword'], self.sword_pos) 
            
            if self.player_area.colliderect(self.sword_area): 
            # Checks if our player rect is colliding with the swords rect
                self.sword_connected = True
                
            if self.sword_connected == True:
                    self.sword_pos = [self.player_x + offest_x, self.player_y] 
                    # The sword position is now set to the players position with some offset
            
            
            
            ''' if self.player_area.colliderect(self.testing_collision_area):
                pygame.draw.rect(self.screen, (0, 0, 255), self.testing_collision_area)
            else:
                pygame.draw.rect(self.screen, (255, 0, 255), self.testing_collision_area) 
            This code was to test if my rect existed and was colliding properly. It is temporary code so its not needed'''
            
            pygame.display.update()
            self.clock.tick(60)
        
                
Game().run()

