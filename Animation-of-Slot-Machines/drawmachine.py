import numpy as np
import pygame
import sys


SKY = (70,130,180)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
GOLD = (255,223,0)

class SlotMachine(pygame.sprite.Sprite):
    def __init__(self,surfsize,surfcolor,machineMean = 0):
        pygame.sprite.Sprite.__init__(self)
        self.played = 0
        self.machineMean = 0
        self.size = surfsize
        self.color = surfcolor
        self.width = surfsize[0]
        self.height = surfsize[1]
        self.image = pygame.Surface([self.size[0]+100,self.size[1]+100]).convert()
        self.image.fill(surfcolor)
        self.image.set_colorkey(surfcolor) 
        pygame.draw.rect(self.image,RED,[15,20,self.width-30,self.height*2.0/3],0)
        pygame.draw.rect(self.image,WHITE,[20,27,self.width-40,17.5],0)
        
        
        # head text
        font = pygame.font.SysFont('Calibri', 20, True, False)      
        self.headtext = font.render("PLAY", True, BLACK)
    
        # Put the image of the text on the screen at 250x250
        self.image.blit(self.headtext, [25, 27])
        
        
        #  main screen
        
        pygame.draw.rect(self.image,GOLD,[20,50,self.width-40,30],0)
        pygame.draw.rect(self.image,WHITE,[23,51,self.width-77,28],0)
        pygame.draw.rect(self.image,WHITE,[39,51,self.width-77,28],0)
        pygame.draw.rect(self.image,WHITE,[55,51,self.width-77,28],0)
        
        font = pygame.font.SysFont('Calibri',23,True,False)
        self.money = font.render("$",True,BLUE)
        self.image.blit(self.money,[25.5,57])
        self.image.blit(self.money,[41.5,57])
        self.image.blit(self.money,[57.5,57])
        
        #
        pygame.draw.rect(self.image,GOLD,[20,85,self.width-40,5],0)
        
        pygame.draw.rect(self.image,GOLD,[20,95,self.width-40,5],0)
        
        pygame.draw.rect(self.image,GOLD,[20,105,self.width-40,5],0)


        # BOTTOM
        pygame.draw.rect(self.image,RED,[7,20+self.height*2.0/3,self.width-13,self.height*1.0/6])
        
        pygame.draw.rect(self.image,BLACK,[20,15+self.height*2.0/3,self.width-40,self.height*1.0/5-3])
        
        pygame.draw.rect(self.image,WHITE,[20,30+self.height*2.0/3,self.width-40,11])
        
        # pullrole
        pygame.draw.rect(self.image,BLACK,[self.width-15,15+self.height*2.0/3,8,3],0)
        pygame.draw.rect(self.image,BLACK,[self.width-10,self.height*1.0/3,3,67],0)
        pygame.draw.circle(self.image,GOLD,[self.width-9, self.height-100],5,0)
        
        
        
        
        font = pygame.font.SysFont('Calibri', 20, True, False)      
        summary = font.render("PLAYED "+str(self.played)+" TIMES", True,WHITE )

        self.image.blit(summary, [0, self.height+50]) 
        summarymean = font.render("MEAN IS "+str(float("{0:.3f}".format(self.machineMean))),True, WHITE)
        self.image.blit(summarymean,[0,self.height+80])
        
        
    
    def resume(self,times,mean=0):
        self.machineMean = mean
        self.played = times
        self.image = pygame.Surface([self.size[0]+100,self.size[1]+100]).convert()
        self.image.fill(self.color)
        self.image.set_colorkey(self.color) 
        pygame.draw.rect(self.image,RED,[15,20,self.width-30,self.height*2.0/3],0)
        pygame.draw.rect(self.image,WHITE,[20,27,self.width-40,17.5],0)
        
        
            # head text
        font = pygame.font.SysFont('Calibri', 20, True, False)      
        self.headtext = font.render("PLAY", True, BLACK)
        
            # Put the image of the text on the screen at 250x250
        self.image.blit(self.headtext, [25, 27])
        
        
        #  main screen
        
        pygame.draw.rect(self.image,GOLD,[20,50,self.width-40,30],0)
        pygame.draw.rect(self.image,WHITE,[23,51,self.width-77,28],0)
        pygame.draw.rect(self.image,WHITE,[39,51,self.width-77,28],0)
        pygame.draw.rect(self.image,WHITE,[55,51,self.width-77,28],0)
        
        font = pygame.font.SysFont('Calibri',23,True,False)
        self.money = font.render("$",True,BLUE)
        self.image.blit(self.money,[25.5,57])
        self.image.blit(self.money,[41.5,57])
        self.image.blit(self.money,[57.5,57])
        
        #
        pygame.draw.rect(self.image,GOLD,[20,85,self.width-40,5],0)
    
        pygame.draw.rect(self.image,GOLD,[20,95,self.width-40,5],0)
        
        pygame.draw.rect(self.image,GOLD,[20,105,self.width-40,5],0)
        
        
        # BOTTOM
        pygame.draw.rect(self.image,RED,[7,20+self.height*2.0/3,self.width-13,self.height*1.0/6])
        
        pygame.draw.rect(self.image,BLACK,[20,15+self.height*2.0/3,self.width-40,self.height*1.0/5-3])
        
        pygame.draw.rect(self.image,WHITE,[20,30+self.height*2.0/3,self.width-40,11])
        
            # pull
        pygame.draw.rect(self.image,BLACK,[self.width-15,15+self.height*2.0/3,8,3],0)
        pygame.draw.rect(self.image,BLACK,[self.width-10,self.height*1.0/3,3,67],0)
        pygame.draw.circle(self.image,GOLD,[self.width-9, self.height-100],5,0)        
        
        font = pygame.font.SysFont('Calibri', 20, True, False)      
        self.summary = font.render("PLAYED "+str(self.played)+" TIMES", True, WHITE)
        
                # Put the image of the text on the screen at 250x250
        self.image.blit(self.summary, [0, self.height+50]) 
        self.summarymean = font.render("MEAN IS "+str(float("{0:.3f}".format(self.machineMean))),True, WHITE)
        self.image.blit(self.summarymean,[0,self.height+80])        
        
        
        
        
    def pull(self,times = 0, mean=0,profit=0.178):
        self.played = times
        self.machineMean = mean
        self.profit = profit
        self.image = pygame.Surface([self.size[0]+100,self.size[1]+100]).convert()
        self.image.fill(self.color)
        self.image.set_colorkey(self.color) 
        pygame.draw.rect(self.image,RED,[15,20,self.width-30,self.height*2.0/3],0)
        pygame.draw.rect(self.image,WHITE,[20,27,self.width-40,17.5],0)

        # head text
        font = pygame.font.SysFont('Calibri', 20, True, False)      
        self.headtext = font.render("WIN", True, BLACK)
        # Put the image of the text on the screen at 250x250
        self.image.blit(self.headtext, [30, 27])
        
        
        #  main screen
        
        pygame.draw.rect(self.image,GOLD,[20,50,self.width-40,30],0)
        
        
        font = pygame.font.SysFont('Calibri',23,True,False)
        self.money = font.render(str(float("{0:.3f}".format(self.profit))),True,BLUE)
        self.image.blit(self.money,[25.5,57])
        
        #
        pygame.draw.rect(self.image,GOLD,[20,85,self.width-40,5],0)
        
        pygame.draw.rect(self.image,GOLD,[20,95,self.width-40,5],0)
        
        pygame.draw.rect(self.image,GOLD,[20,105,self.width-40,5],0)
        
        
        # BOTTOM
        pygame.draw.rect(self.image,RED,[7,20+self.height*2.0/3,self.width-13,self.height*1.0/6])
        
        pygame.draw.rect(self.image,BLACK,[20,15+self.height*2.0/3,self.width-40,self.height*1.0/5-3])
        
        pygame.draw.rect(self.image,WHITE,[20,30+self.height*2.0/3,self.width-40,11])
        
        pygame.draw.ellipse(self.image,[248,215,74],[22,20+self.height*2.0/3,10,9],0)
        pygame.draw.ellipse(self.image,[248,215,74],[27,21+self.height*2.0/3,10,9],0)
        pygame.draw.ellipse(self.image,[248,215,74],[35,20+self.height*2.0/3,10,9],0)
        pygame.draw.ellipse(self.image,[248,215,74],[39,25+self.height*2.0/3,10,9],0)
        pygame.draw.ellipse(self.image,[248,215,74],[45,20+self.height*2.0/3,10,9],0)
        pygame.draw.ellipse(self.image,[248,215,74],[48,23+self.height*2.0/3,10,9],0)
        pygame.draw.ellipse(self.image,[248,215,74],[57,20+self.height*2.0/3,10,9],0)
        pygame.draw.ellipse(self.image,[248,215,74],[37,30+self.height*2.0/3,10,9],0)
        pygame.draw.ellipse(self.image,[248,215,74],[56,30+self.height*2.0/3,10,9],0)
        pygame.draw.ellipse(self.image,[248,215,74],[20,30+self.height*2.0/3,10,9],0)
        # pull
        pygame.draw.rect(self.image,BLACK,[self.width-15,15+self.height*2.0/3,8,3],0)
        pygame.draw.rect(self.image,BLACK,[self.width-10,15+self.height*2.0/3,3,67],0)
        pygame.draw.circle(self.image,GOLD,[self.width-9, self.height+27],5,0)  
        
        
        font = pygame.font.SysFont('Calibri', 20, True, False)      
        self.summary = font.render("PLAYED "+str(self.played)+" TIMES", True, WHITE)
        
                # Put the image of the text on the screen at 250x250
        self.image.blit(self.summary, [0, self.height+50]) 
        self.summarymean = font.render("MEAN IS "+str(float("{0:.3f}".format(self.machineMean))),True, WHITE)
        self.image.blit(self.summarymean,[0,self.height+80])
        
    
   