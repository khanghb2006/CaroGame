import pygame
import sys
import board
import rule
from pygame import mixer

pygame.init()

#Window
Width = 480
Heigh = 550

#Colors
Black = (0 , 0 , 0 , 225)
Gold = (215 , 215 , 0 , 255)

#Sound
mixer.music.load('sound/error.mp3')
mixer.music.set_volume(1000)

#Fonts
font = pygame.font.Font('freesansbold.ttf', 50)

#Start Button
start_text = font.render('START' , True , Black , Gold)
start_rect = start_text.get_rect()
start_rect.center = (Width // 2 , Heigh // 1.45)

#Rule Button
rule_text = font.render("RULE" , True , Black , Gold)
rule_rect = rule_text.get_rect()
rule_rect.center = (Width // 2 , 450)


#Cordinate Start Button
start_lef = start_rect.left
start_rig = start_rect.right
start_top = start_rect.top
start_bot = start_rect.bottom


#Cordinate Rule Button
rule_lef = rule_rect.left
rule_rig = rule_rect.right
rule_top = rule_rect.top
rule_bot = rule_rect.bottom


def check_cursor_in_start(local_x , local_y) : 
    return start_lef <= local_x <= start_rig and start_top <= local_y <= start_bot

def check_cursor_in_rule(local_x , local_y) : 
    return rule_lef <= local_x <= rule_rig and rule_top <= local_y <= rule_bot


def load_background() : 
    screen = pygame.display.set_mode((Width , Heigh))
    pygame.display.set_caption("Tic Tac Toe")
    
    Running = True
    
    while Running : 
        
        #Load BackGround
        background = pygame.image.load('imagine/background.png').convert()
        screen.blit(background , (0 , 0))
        
        #Load Button
        screen.blit(start_text , start_rect)
        screen.blit(rule_text , rule_rect)
        
        pygame.display.flip()
        
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT : 
                Running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN : 
                local_x , local_y = pygame.mouse.get_pos()
                if check_cursor_in_start(local_x , local_y) : 
                    board.start_board()
                elif check_cursor_in_rule(local_x , local_y) : 
                    rule.show_Rule()
                else :
                    mixer.music.play()
                
                    
    pygame.quit()
    
    
    
    


    