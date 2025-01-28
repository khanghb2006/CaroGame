import pygame
import sys
from pygame import mixer

pygame.init()
mixer.init()
pygame.get_init()

#Display
screen = pygame.display.set_mode((800,600),pygame.RESIZABLE)

pygame.display.set_caption("Tic Tac Toe")

game_icon = pygame.image.load('imagine/icon.webp')
pygame.display.set_icon(game_icon)

#Num Block 10 x 10
Num_Block = 10

#Size of window
Width,Height = screen.get_size()
Col_Width = Width / Num_Block
Row_Width = Height / Num_Block

#Color
White = (255 , 255 , 255 , 255)
Black = (0 , 0 , 0 , 225)
Blue = (30 , 144 , 225)
Gold = (215 , 215 , 0 , 255)
Red = (255 , 0 , 0 , 255)

#Sound 
error_sound = mixer.music.load('sound/error.mp3')
mixer.music.set_volume(1000)

# Font
font = pygame.font.Font('freesansbold.ttf' , 250)
font_noice = pygame.font.Font('freesansbold.ttf' , 50)
X_win = font.render('X WIN' , True , Gold , Black)
O_win = font.render('O WIN' , True , Gold , Black)
noice = font_noice.render("O nay da duoc danh roi" , Gold , Black)

#Board memory
board = [['' for _ in range(Num_Block)] for _ in range(Num_Block)]

#Draw board
def draw_board() : 
    screen.fill(White)
    
    for col in range (0 , Num_Block) : 
        pygame.draw.line(screen , Black , ((col + 1) * Col_Width , 0) , ((col + 1) * Col_Width,Height), 1) 
        
    for row in range (0 , Num_Block) : 
        pygame.draw.line(screen , Black , (0 , (row + 1) * Row_Width) , (Width , (row + 1) * Row_Width) , 1)
    
    pygame.display.flip() 

#Draw X in board
def draw_X (local_x , local_y) : 
    
    # corner_1          corner_2
    #
    #corner_3           corner_4 
    
    lef_col = int(local_x // Col_Width)
    rig_col = int(local_x // Col_Width + 1)
    
    up_row = int(local_y // Row_Width)
    down_row = int(local_y // Row_Width + 1)
        
    board[lef_col][up_row] = 'X'
    
    corner_1 = (lef_col * Col_Width , up_row * Row_Width)
    corner_2 = (rig_col * Col_Width , up_row * Row_Width)
    corner_3 = (lef_col * Col_Width , down_row * Row_Width)
    corner_4 = (rig_col * Col_Width , down_row * Row_Width)
    
    pygame.draw.line(screen , Red , corner_1 , corner_4 , 2)
    pygame.draw.line(screen , Red , corner_2 , corner_3 , 2)
    
    pygame.display.flip()
    

#Draw O in board
def draw_O (local_x , local_y) : 
    lef_col = int(local_x // Col_Width)
    rig_col = int(local_x // Col_Width + 1)
    
    up_row = int(local_y // Row_Width)
    down_row = int(local_y // Row_Width + 1)
    
    # print(lef_col , up_row)
    board[lef_col][up_row] = 'O'
    
    Centre = (Col_Width * (rig_col + lef_col) / 2, Row_Width * (down_row + up_row) / 2)
    Radious = min (Col_Width / 2 , Row_Width / 2)
    
    pygame.draw.circle(screen , Blue , Centre , Radious , 4)
    pygame.display.flip()


def check_row(local_x , local_y , who) : 
    x = int(local_x // Col_Width)
    y = int(local_y // Row_Width)
    
    num_who = 1
    for row in range(x - 1 , -1 , -1) : 
        if board[row][y] == who : 
            num_who += 1
        else :
            break
    for row in range(x + 1 , Num_Block , 1) : 
        if board[row][y] == who : 
            num_who += 1
        else : 
            break

    return num_who >= 5
    
 
def check_col(local_x , local_y , who) : 
    x = int(local_x // Col_Width)
    y = int(local_y // Row_Width)
    
    num_who = 1
    for col in range(y - 1 , -1 , -1) : 
        if board[x][col] == who : 
            num_who += 1
        else :
            break
    for col in range(y + 1 , Num_Block , 1) : 
        if board[x][col] == who : 
            num_who += 1
        else : 
            break
        
    return num_who >= 5


def check_diagonal (local_x , local_y , who) : 
    x = int(local_x // Col_Width)
    y = int(local_y // Row_Width)
    
    num_who = 1
    
    for diff in range(1 , min(x , y) + 1 , 1) : 
        if board[x - diff][y - diff] == who : 
            num_who += 1
        else : 
            break
    for diff in range(1, min(Num_Block - x,Num_Block - y) , 1) : 
        if board[x + diff][y + diff] == who : 
            num_who += 1
        else : 
            break

    return num_who >= 5


def check_antiDiagonal (local_x , local_y , who) : 
    x = int(local_x // Col_Width)
    y = int(local_y // Row_Width)
    
    num_who = 1
    
    for diff in range (1 , min(x + 1 , Num_Block - y) , 1) : 
        if board[x - diff][y + diff] == who : 
            num_who += 1
        else : 
            break
    for diff in range(1 , min(y + 1 , Num_Block - x) , 1) : 
        if board[x + diff][y - diff] == who : 
            num_who += 1
        else : 
            break

    return num_who >= 5 
 
    
def check_win(local_x , local_y , who) : 
    if check_row(local_x , local_y , who) == True : 
        return True
    if check_col(local_x , local_y , who) == True :
        return True
    if check_diagonal(local_x , local_y , who) == True : 
        return True
    if check_antiDiagonal(local_x , local_y , who) == True : 
        return True
    return False

def winner(who) : 
    if who == 'X' : 
        textRect = X_win.get_rect()
        textRect.center = (Width // 2 , Height // 2)
        screen.blit(X_win , textRect)
    else : 
        textRect = O_win.get_rect()
        textRect.center = (Width // 2 , Height // 2)
        screen.blit(O_win , textRect)
    pygame.display.flip()
    
def check_vis (local_x , local_y) : 
    x = int(local_x // Col_Width)
    y = int(local_y // Row_Width)
    
    return board[x][y] != 'X' and board[x][y] != 'O'

# Main

def start_board() : 
    screen = pygame.display.set_mode((800,600),pygame.RESIZABLE)
    
    Running = True
    Turn = True
    Num_turn = 0

    draw_board()

    while Running : 
        
        for event in pygame.event.get() : 
            
            if event.type == pygame.QUIT : 
                Running = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN : 
                
                local_x , local_y = pygame.mouse.get_pos()
                
                # print(local_x , local_y)
                
                if Turn : 
                    if check_vis(local_x , local_y) :
                        draw_X(local_x , local_y)
                        Num_turn += 1
                        Turn = False
                    else : 
                        print('O nay da duoc danh roi!')
                        mixer.music.play()
                    if check_win(local_x , local_y , 'X') == True : 
                        winner('X')
                        Running = False
                else : 
                    if check_vis(local_x , local_y) : 
                        draw_O(local_x , local_y)
                        Num_turn += 1
                        Turn = True       
                    else : 
                        print('O nay da duoc danh roi!')
                        mixer.music.play()
                    if check_win(local_x , local_y , 'O') == True : 
                        winner('O')
                        Running = False
                if Num_turn == Num_Block * Num_Block : 
                    print('Draw')
                    Running = False
                
    pygame.time.wait(2000)
    pygame.quit()
