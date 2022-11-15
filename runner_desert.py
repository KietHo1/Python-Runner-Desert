from posixpath import supports_unicode_filenames
import pgzrun
from pygame import Color
from pgzhelper import *
import random

WIDTH=800
HEIGHT=600

background=Actor('background')
#Build menu
print("*******************************************************")
print("*                 Menu game Runner-Desert             *")
print("*-----------------------------------------------------*")
print("* 1. You can choose your character                    *")
print("* 2. Random character                                 *")
print("*******************************************************")

while True:
    chooseNumber = input("Enter your choose number: ")
    chooseNumber = int (chooseNumber)
    if(chooseNumber > 0 and chooseNumber < 3):
        break
if(chooseNumber == 1):
    #Choose playership in your way
    while True:
        listCharacterNumber = input("Enter your character number: ")
        listCharacterNumber = int (listCharacterNumber)
        if(listCharacterNumber > 0 and listCharacterNumber < 6):
            break
    if(listCharacterNumber == 1):
        runner=Actor('dinosaur')
        run_images=['dinosaur_run1','dinosaur_run2','dinosaur_run3','dinosaur_run4',
        'dinosaur_run5','dinosaur_run6','dinosaur_run7','dinosaur_run8']
    elif(listCharacterNumber == 2):
        runner=Actor('knight')
        run_images=['knight_run1','knight_run2','knight_run3','knight_run4',
        'knight_run5','knight_run6','knight_run7','knight_run8', 'knight_run9', 'knight_run10']
    elif(listCharacterNumber == 3):
        runner=Actor('ninja')
        run_images=['ninja_run1','ninja_run2','ninja_run3','ninja_run4',
        'ninja_run5','ninja_run6','ninja_run7','ninja_run8', 'ninja_run9', 'ninja_run10']
    elif(listCharacterNumber == 4):
        runner=Actor('alien1_stand')
        run_images=['alien1_walk01', 'alien1_walk02', 'alien1_walk03', 'alien1_walk04', 'alien1_walk05',
        'alien1_walk06', 'alien1_walk07', 'alien1_walk08', 'alien1_walk09', 'alien1_walk10']
    else:
        runner=Actor('alien2_stand')
        run_images=['alien2_stand', 'alien2_walk1', 'alien2_walk2']
else:
    # Random character
    listCharacterNumber = [1, 2, 3, 4, 5]
    if(random.choice(listCharacterNumber) == 1):
        runner=Actor('dinosaur')
        run_images=['dinosaur_run1','dinosaur_run2','dinosaur_run3','dinosaur_run4',
        'dinosaur_run5','dinosaur_run6','dinosaur_run7','dinosaur_run8']
    elif(random.choice(listCharacterNumber) == 2):
        runner=Actor('knight')
        run_images=['knight_run1','knight_run2','knight_run3','knight_run4',
        'knight_run5','knight_run6','knight_run7','knight_run8', 'knight_run9', 'knight_run10']
    elif(random.choice(listCharacterNumber) == 3):
        runner=Actor('ninja')
        run_images=['ninja_run1','ninja_run2','ninja_run3','ninja_run4',
        'ninja_run5','ninja_run6','ninja_run7','ninja_run8', 'ninja_run9', 'ninja_run10']
    elif(random.choice(listCharacterNumber) == 4):
        runner=Actor('alien1_stand')
        run_images=['alien1_walk01', 'alien1_walk02', 'alien1_walk03', 'alien1_walk04', 'alien1_walk05',
        'alien1_walk06', 'alien1_walk07', 'alien1_walk08', 'alien1_walk09', 'alien1_walk10']
    else:
        runner=Actor('alien2_stand')
        run_images=['alien2_stand', 'alien2_walk1', 'alien2_walk2']

runner.images=run_images
runner.x=100
runner.y=450

velocity_y=0
gravity=1

obstacels_timeout=0
obstacels=[]

score=0
game_over=False



def update():
    global velocity_y , gravity , obstacels_timeout , score, game_over , obstacels 
    runner.next_image()

    obstacels_timeout+=1
    if obstacels_timeout > 50:
        actor=Actor('catus')
        actor.x=800
        actor.y=450
        obstacels.append(actor)
        obstacels_timeout=0
    for actor in obstacels :
        actor.x-=8
        if actor.x<-50:
            score=score+1
            obstacels.remove(actor)
    if runner.collidelist(obstacels)!=-1:
        game_over=True
        obstacels.remove(actor)
        sounds.gameover.play()



    if keyboard.up and runner.y==450 : #up to jump up
        velocity_y=-23
        sounds.impact.play()
    runner.y+=velocity_y
    velocity_y+=gravity
    if runner.y>450:
        velocity_y=0
        runner.y=450
    if keyboard.space: #space to restart
        game_over= False
        score=0
        obstacels=[]



def draw():
    background.draw()
    
    if game_over:
        screen.draw.text('GAME OVER!',(300,300),color=(255,255,255),fontsize=60)
        screen.draw.text('Final score: '+str(score),(305,360),color=(255,0,255),fontsize=80)
        screen.draw.text('Press space to restart',(305,400),color=(100,100,255),fontsize=60)
    else:
        screen.draw.text('Score: '+str(score),(10,15),color=(255,0,255),fontsize=30)
        runner.draw()
        for actor in obstacels:
            actor.draw()
pgzrun.go()