import pygame 
import sys
import time
from utility import load_image, load_images  # Functions residing in the utility folder
from enemy_movement import Enemy




class Swing_Animation:
    def __init__(self, frame):
        self.frame = frame
        self.frames = [load_image('weapons/sword-sprites/sword-swing4.png'),
                       load_image('weapons/sword-sprites/sword-swing1.png'),
                       load_image('weapons/sword-sprites/sword-swing2.png'),
                       load_image('weapons/sword-sprites/sword-swing3.png')]
        self.frames_index_max = len(self.frames) - 1
        self.frames_index = self.frames_index_max
        # self.pos = (0,0)
        
        
    
    def updateFrame(self):
            if self.frames_index < self.frames_index_max:
                self.frames_index += 1
            else:
                self.frames_index = 0


class Game: 
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption('Defenders')  # Creates window title
        
        self.screen = pygame.display.set_mode((900, 700))  # Window size
        self.display = pygame.Surface((900, 700))
        
        
        # self.top_collision = pygame.Rect(0, 0, 900, 50)  # Top edge
        # self.bottom_collision = pygame.Rect(0, 700 - 50, 900, 50)  # Bottom edge
        # self.left_collision = pygame.Rect(0, 0, 50, 700)  # Left edge
        # self.right_collision = pygame.Rect(900 - 50, 0, 50, 700)  # Right edge

        self.clock = pygame.time.Clock()  # Helps restrict frame rate
        
        self.movement = [False, False, False, False]
        
        self.assets = {
            'background': load_image('background/whyjustwhy.png'),
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
        
        self.player_speed = 4
        self.enemy_speed = 2
        
        self.enemy_movement = Enemy(self.enemy_pos, self.enemy_speed)
        self.enemy_hp = 100
        self.enemy_alive = True
        self.damage = False
        
        
        # self.testing_collision_area = pygame.Rect(250 , 450, 100, 100)
        self.player_area = pygame.Rect(self.player_x, self.player_y, 1, 1)
        self.enemy_area = pygame.Rect(700, 300, 50, 50)
        self.sword_area = pygame.Rect(self.sword_x, self.sword_y, 100, 100)
        
        self.sword_connected = False
        self.swing_animation = Swing_Animation(self.assets['sword'])
        self.swinging = False
        self.delay = 0
        

    #def updateEnemy(self):
        #self.enemy_movement.Follow_Player(self.player_x, self.player_y)
        #pass
    
    
    def run(self):
        running = True
        
        # Game Loop
        while running:
            offest_x = 25
            
            
            #self.display.fill((14, 111, 222))  # Placeholder method for me setting a background
            
            
            # Movement Calls
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
            
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.sword_connected == True:
                    self.swinging = True
                    self.swing_animation.frames_index = 0
                    
            # Screen set-up and image loading
            self.display.blit(self.assets['background'])
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            self.screen.blit(self.assets['player'], self.player_pos) # Blits the image, and sets the image position on the screen
            self.player_area.update(self.player_x, self.player_y, 100, 100)
            
            # Enemy Status' 
            if self.enemy_alive:
                self.screen.blit(self.assets['zombie'], self.enemy_pos)
                self.enemy_movement.Follow_Player(self.player_x, self.player_y)
                self.enemy_area.topleft = self.enemy_pos # 
                 
            self.screen.blit(self.assets['sword'], self.sword_pos) 
            
            # Player-Sword Interaction
            if self.player_area.colliderect(self.sword_area): 
            # Checks if our player rect is colliding with the swords rect
                self.sword_connected = True
                
            if self.sword_connected == True:
                    self.sword_pos = [self.player_x + offest_x, self.player_y] 
                    # The sword position is now set to the players position with some offset
            
            # Swing Animation
            self.swing_pos = [self.player_x + 50, self.player_y]
            
            if self.swinging == True:
                self.swing_animation.updateFrame()
                self.screen.blit(self.swing_animation.frames[self.swing_animation.frames_index],self.swing_pos)
            
            if self.swing_animation.frames_index == 0:
                self.swinging = False 
                
                
            # Swing Collision
            self.swing_area = pygame.Rect(self.swing_pos[0] + 10, self.swing_pos[1], 30, 50)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.swing_area.colliderect(self.enemy_area):
                    # pygame.draw.rect(self.screen, (0, 0, 255), self.swing_area) Temporary Code. This was used to visualize the hitbox
                    self.damage = True
            
            # Damage Check     
            if self.damage == True:
                if self.swing_animation.frames_index == 2: # Honestly no clue why list value 2 is where damage registers
                    pygame.time.get_ticks() + 1000
                    self.damage = False
                    self.enemy_hp -= 10
                    
            # Respawn Enemy
            if self.enemy_hp <= 0 and self.enemy_alive:
                print("Enemy has died") # Debugging
                self.enemy_alive = False
                self.delay = pygame.time.get_ticks() + 2500
            
            if self.enemy_alive == False and pygame.time.get_ticks() > self.delay:
                print("Respawning...") # Debugging
                self.enemy_alive = True
                self.enemy_hp = 100
                self.enemy_pos = [700, 300]
                self.enemy_movement = Enemy(self.enemy_pos, self.enemy_speed) # Reenables the follow function

            
                
            
            
            ''' if self.player_area.colliderect(self.testing_collision_area):
                pygame.draw.rect(self.screen, (0, 0, 255), self.testing_collision_area)
            else:
                pygame.draw.rect(self.screen, (255, 0, 255), self.testing_collision_area) 
            This code was to test if my rect existed and was colliding properly. It is temporary code so its not needed'''
            
            pygame.display.update()
            self.clock.tick(60)
        
                
Game().run()

