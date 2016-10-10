import sys
import pygame
import numpy as np
from drawmachine import *
from multiarm import *
from randomarm import *
from exp3 import *




pygame.init()
SKY = (70,130,180)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
GOLD = (255,223,0)


SCREENWIDTH,SCREENHEIGHT = 900,900
        
        # Set the height and width of the screen
        
        
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
sound = pygame.mixer.Sound('coin.wav')

background = pygame.Surface(screen.get_size())
background = background.convert()

# FOR EXP3 STRATEGY

gamma = np.sqrt(5*np.log(5)/(np.exp(1)-1)/400)
if gamma > 1:
    gamma =1
ita = gamma/5


scheme = betaScheme(5)

myMAO = MultiArmOpponent(scheme)

myPIG =PartialInformationGame(ita,gamma,myMAO)

means = myPIG.myMAOmodel.scheme.means()

machines = [SlotMachine([90,150],SKY,means[0]),SlotMachine([90,150],SKY,means[1]),
            SlotMachine([90,150],SKY,means[2]),SlotMachine([90,150],SKY,means[3]),SlotMachine([90,150],SKY,means[4])]


 #FOR RANDOM STRATEGY
randomscheme = betaScheme(5)

randomMAO = MultiArmOpponent(randomscheme)
randomGame = RandomGame(randomMAO)
randommeans = randomGame.myMAOmodel.scheme.means()

randmachines = [SlotMachine([90,150],SKY,randommeans[0]),SlotMachine([90,150],SKY,randommeans[1]),
            SlotMachine([90,150],SKY,randommeans[2]),SlotMachine([90,150],SKY,randommeans[3]),SlotMachine([90,150],SKY,randommeans[4])]




rounds = 0

while True:
    # PROCESSES
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(SKY)
    # EXP3 PLAY
    j,curgain = myPIG.play()
    
    # RANDOM PLAY
    rj,rcurgain = randomGame.play()
    
    rounds += 1
    #if rounds <= 4:
    #    pygame.time.delay(3000)
    if rounds == 400:
        pygame.time.delay(1000000)
    
    print rounds
    
    
    # DISPLAY EXP3 MACHINES
    
    for i in range(5):
        mc = machines[i]
        if i == j:
            mc.pull(myPIG.myMAOmodel.scheme.numPlayed[i],means[i],curgain)
            screen.blit(mc.image,[150*i+100,100])
        else:
            mc.resume(myPIG.myMAOmodel.scheme.numPlayed[i],means[i])
            screen.blit(mc.image,[150*i+100,100])    
            
    font = pygame.font.SysFont('Calibri', 35, True, False)      
    score = font.render("SCORE:  "+str(float("{0:.6f}".format(myPIG.acturalGain))), True, WHITE)
    ma = font.render("MAXIMUM:  "+str(float("{0:.6f}".format(myPIG.maxiSum))), True, WHITE)
    screen.blit(score, [310, 40]) 
    screen.blit(ma,[290,70])        
    name = font.render("EXP3 STRATEGY",True,WHITE)
    screen.blit(name,[310,10])
    
    
    for ri in range(5):
        rmc = randmachines[ri]
        if ri == rj:
            rmc.pull(randomGame.myMAOmodel.scheme.numPlayed[ri],randommeans[ri],rcurgain)
            screen.blit(rmc.image,[150*ri+100,500])
        else:
            rmc.resume(randomGame.myMAOmodel.scheme.numPlayed[ri],randommeans[ri])
            screen.blit(rmc.image,[150*ri+100,500])   
    rfont = pygame.font.SysFont('Calibri', 35, True, False)  
    rscore = rfont.render("SCORE:  "+str(float("{0:.6f}".format(randomGame.acturalGain))), True, WHITE)
    rma = rfont.render("MAXIMUM:  "+str(float("{0:.6f}".format(randomGame.maxiSum))), True, WHITE)
    screen.blit(rscore, [310, 400]) 
    screen.blit(rma,[290,430])    
    rname = font.render("RANDOM STRATEGY",True,WHITE)
    screen.blit(rname,[290,370])
    if rounds <=399:
        sound.play() 
    
    
    pygame.display.flip()  
    means = myPIG.myMAOmodel.scheme.means()
    randommeans = randomGame.myMAOmodel.scheme.means()
    
           