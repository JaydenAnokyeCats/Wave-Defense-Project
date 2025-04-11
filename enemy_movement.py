class Enemy:
    def __init__(self, enemy_pos, enemy_speed):
        self.enemy_pos = enemy_pos
        self.enemy_speed = enemy_speed
        
        
    
    def Follow_Player(self, player_x, player_y):
        if self.enemy_pos[0] > player_x:
            self.enemy_pos[0] -= self.enemy_speed # Move Left
        elif self.enemy_pos[0] < player_x:
            self.enemy_pos[0] += self.enemy_speed # Move Right
            
        if self.enemy_pos[1] > player_y:
            self.enemy_pos[1] -= self.enemy_speed
        elif self.enemy_pos[1] < player_y:
            self.enemy_pos[1] += self.enemy_speed
