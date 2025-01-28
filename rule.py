import pygame
import sys
import background

pygame.init()

#Window
Width = 800
Heigh = 600
pygame.display.set_caption("Tic Tac Toe")
game_icon = pygame.image.load('imagine/icon.webp')
pygame.display.set_icon(game_icon)

#Color
White = (255 , 255 , 255 , 255)
Black = (0 , 0 , 0 , 225)
Blue = (30 , 144 , 225)
Gold = (215 , 215 , 0 , 255)
Red = (255 , 0 , 0 , 255)

#Font
font_text = pygame.font.Font('freesansbold.ttf' , 45)
font_button = pygame.font.Font('freesansbold.ttf' , 80)

#Back Button
back_button_text = font_button.render('BACK' , True , Black , Gold)
back_button_rect = back_button_text.get_rect()
back_button_mid = int((back_button_rect.bottom - back_button_rect.top) // 2)
back_button_rect.center = (back_button_rect.right // 2 , Heigh - back_button_mid)

#Rule 
diff = 40
diff_rule = 80
rule_text = font_button.render('RULE' , True , Red)
line1_text = font_text.render(' - First play is X' , True , Black)
line2_text = font_text.render(' - Second player is O' , True , Black)
line3_text = font_text.render(' - Who have five X or five O is win' , True , Black)
#Rule : RuleText
rule_rect = rule_text.get_rect()
rule_lef = rule_rect.left
rule_rig = rule_rect.right
rule_top = rule_rect.top
rule_bot = rule_rect.bottom
rule_size = 2 * diff_rule + int(rule_bot - rule_top)
rule_mid = diff_rule + int((rule_bot - rule_top) // 2)
rule_rect.center = (Width // 2 , rule_mid)
#Rule  : Line1
line1_rect = line1_text.get_rect()
line1_lef = line1_rect.left
line1_rig = line1_rect.right
line1_top = line1_rect.top
line1_bot = line1_rect.bottom
line1_size = rule_size + int(line1_bot - line1_top) + diff
line1_mid = rule_size + int ((line1_bot - line1_top) // 2) 
line1_rect.center = (line1_rig // 2 , line1_mid)
#Rule : Line2 
line2_rect = line2_text.get_rect()
line2_lef = line2_rect.left
line2_rig = line2_rect.right
line2_top = line2_rect.top
line2_bot = line2_rect.bottom
line2_size = line1_size + int(line2_bot - line2_top) + diff
line2_mid = line1_size + int((line2_bot - line2_top) // 2)
line2_rect.center = (line2_rig // 2 , line2_mid)
#Rule : Line3 
line3_rect = line3_text.get_rect()
line3_lef = line3_rect.left
line3_rig = line3_rect.right
line3_top = line3_rect.top
line3_bot = line3_rect.bottom
line3_size = line2_size + int(line3_bot - line3_top) + diff
line3_mid = line2_size + int((line3_bot - line3_top) // 2)
line3_rect.center = (line3_rig // 2, line3_mid)


def check_cursor_in_back_button(local_x , local_y) : 
    back_lef = back_button_rect.left
    back_rig = back_button_rect.right
    back_top = back_button_rect.top
    back_bot = back_button_rect.bottom
    
    return back_lef <= local_x <= back_rig and back_top <= local_y <= back_bot


def show_Rule() : 
    
    # Window setting
    pygame.display.set_caption("Tic Tac Toe")
    game_icon = pygame.image.load('imagine/icon.webp')
    pygame.display.set_icon(game_icon)
    screen = pygame.display.set_mode((Width , Heigh))
    screen.fill(White)
    screen.blit(rule_text , rule_rect)
    screen.blit(back_button_text , back_button_rect)
    screen.blit(line1_text , line1_rect)
    screen.blit(line2_text , line2_rect)
    screen.blit(line3_text , line3_rect)
    pygame.display.flip()
    
    Running = True
    
    while Running : 
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT : 
                Running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN : 
                local_x , local_y = pygame.mouse.get_pos()
                if check_cursor_in_back_button(local_x , local_y) : 
                    background.load_background()
    pygame.quit()
    
