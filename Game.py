import pygame
import time
import random
import os
pygame.font.init()


# Window size
WIDTH      = 500
HEIGHT     = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boss Fight")



#import npc images
Enemy = pygame.image.load(os.path.join("assets", "Enemy.png"))
Enemy2 = pygame.image.load(os.path.join("assets", "Helper.png"))

#import player
Player = pygame.image.load(os.path.join("assets", "Man.png"))

#import attack animation
Enemy_attack = pygame.image.load(os.path.join("assets", "Attack.png"))
Player_attack = pygame.image.load(os.path.join("assets", "PlayerAttack.png"))

#Get the background image
bg = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Space.jpg")), (WIDTH, HEIGHT))

class Character:
    global location
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.character_img = Player
        self.attack_img = None
        self.attack = []
        self.cooldown_counter = 0
    def draw(self, window):
        window.blit(self.character_img, (self.x, self.y))
        
    
def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    level = 1
    lives = 10
    main_font = pygame.font.SysFont("Arial", 50)
    player_vel = 5
    character = Character(300, 400)
    def redraw_window():
        WIN.blit(bg, (0,0))
        # Making text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        #Printing the text onto the screen
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10 , 10))

        character.draw(WIN)
        
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and character.x + player_vel > 0: #left
            character.x -= player_vel
        if keys[pygame.K_d] and character.x + player_vel < WIDTH - 50: # rgiht
            character.x += player_vel
        if keys[pygame.K_w] and character.y - player_vel > 0: #up
            character.y -= player_vel
        if keys[pygame.K_s] and character.y + player_vel < HEIGHT - 50: #down
            character.y += player_vel    
            
        




main()
