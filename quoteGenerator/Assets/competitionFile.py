import pygame
import random
import textwrap
import time


#pygame thing initialize
pygame.init()
(width, height) = (640, 480)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.flip()

black = (0,0,0)
white = (255,255,255)

font = pygame.font.Font('raleway/Raleway-BlackItalic.ttf', 16)
text = font.render('Click Me :)', True, white, white)
textRect = text.get_rect()
textRect.center = (10, height // 2)

screen.fill(white)
pygame.display.set_caption('Click me')

#motivation txt thing initialize
with open('motivationSpeeches.txt', 'r') as fn:
    file_name = fn.readlines()

running = True
while running:
  for event in pygame.event.get():
    randNum = random.randint(0, 360)
    
    screen.blit(text, textRect)
    pygame.display.update()
    if event.type == pygame.MOUSEBUTTONDOWN:
        #todo change this yum tgd wrapshaax margaash2
        
        txt = txt.split()
        print(txt)

        pos = pygame.mouse.get_pos()
        if file_name[randNum][0] == '\'' or file_name[randNum][0] == '\"':
            text = font.render(file_name[randNum], True, black, white)
        else:
            text = font.render(file_name[randNum+1], True, black, white)
            
        
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()
        running = False
    
      
      
