#################################################
################ Name: Houman Ebrahimi
################ Date: 2020/05/07
################ Description : snake game neon edition
#################################################


import pygame

pygame.init()
#####################
## modules used    ##
#####################
from random import randint
from random import randrange
from math import sqrt
from time import perf_counter

# height and width
height=650
width=900

apple_eaten=0

# main windown 
mainW=pygame.display.set_mode((width,height))
##########
## Fonts##
##########
font=pygame.font.SysFont(('Ariel Black'),20)
font2=pygame.font.SysFont(('Snap ITC'),140)
font3=pygame.font.SysFont(('Snap ITC'),20)
font4=pygame.font.SysFont(('Snap ITC'),30)
# main image 
mainP=pygame.image.load('mainP.jpg')
mainP=mainP.convert_alpha()
change=pygame.transform.scale(mainP,(width,height))

# colours 
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
cyan=(0,255,255)
magenta=(255,0,255)
outline=0

# snakes body and speed

body_width=13
body_height=13
hSpeed=10
vSpeed=10

speedX=0
speedY=0

segX=[int(width/2)]*3
segY=[height,height*hSpeed,height*2*vSpeed]
########## Good Apple #################
apple_X=int(width/2)
apple_Y=int(height/2)
apple_R=10



############ KIWI very good !###################
kiwi_X=randint(30,width-30)
kiwi_Y=randint(30,height-30)
kiwi_width=30
kiwi_height=30
# kiwi picture with apple 
kiwi=pygame.image.load('kiwi.png')
kiwi=kiwi.convert_alpha()
kiwi_transform=pygame.transform.scale(kiwi,(kiwi_width,kiwi_height))


apple=pygame.image.load(("apple.png"))
apple=apple.convert_alpha()
transform_apple=pygame.transform.scale(apple,(30,30))


# bad apple (in this case i could say bad banana) with picture 
apple_pX=70
apple_pY=70
apple_pR=10

apple_poison=pygame.image.load('poisonBanana.png')
apple_poison=apple_poison.convert_alpha()
apple_change=pygame.transform.scale(apple_poison,(50,50))

# intro picture 
intro_game=pygame.image.load('intro.jpg')
intro_game=intro_game.convert_alpha()
intro_change=pygame.transform.scale(intro_game,(width,height))

# timer 
time=20
startTime=pygame.time.get_ticks()/1000

## start snake image ##
snake_head=pygame.image.load('snake_headU.png')
snake_head=snake_head.convert_alpha()
snake_head_transform=pygame.transform.scale(snake_head,(body_width+5,body_height+5))
new_face=snake_head_transform

snake_headL=pygame.image.load('snake_headL.png')
snake_headL=snake_headL.convert_alpha()
snake_head_transformL=pygame.transform.scale(snake_headL,(body_width+5,body_height+5))

snake_headR=pygame.image.load('snake_headR.png')
snake_headR=snake_headR.convert_alpha()
snake_head_transformR=pygame.transform.scale(snake_headR,(body_width+5,body_height+5))

snake_headD=pygame.image.load('snake_headD.png')
snake_headD=snake_headD.convert_alpha()
snake_head_transformD=pygame.transform.scale(snake_headD,(body_width+5,body_height+5))

body1=pygame.image.load('body1.png')
body1=body1.convert_alpha()
body1_transform=pygame.transform.scale(body1,(body_width+5,body_height+5))
snake_body=body1_transform

body2=pygame.image.load('body2.png')
body2=body2.convert_alpha()
body2_transform=pygame.transform.scale(body2,(body_width+5,body_height+5))

### end snake image###

#############
## endScreen#
#############
final=pygame.image.load('final.jpg')
final=final.convert_alpha()
whole_final=pygame.transform.scale(final,(width,height))

arrow_keys=pygame.image.load('arrowKeys.png')
arrow_keys=arrow_keys.convert_alpha()
arrow_keys_resize=pygame.transform.scale(arrow_keys,(100,100))



# play button with the instruction button next 
play_x=110
play_y=450
play_w=65
play_h=30

ins_X=110
ins_Y=520
ins_w=150
ins_h=30

#wall 1 coordinates

wall_X=randrange(50,width//2-50)
wall_Y=randrange(0,height-100)
wall_w=200
wall_h=30

# wall  2 coordinates 
wall_X2=randrange(width//2+100,width-100)
wall_Y2=randrange(0,height-100)
wall_w2=30
wall_h2=200

# speed of the walls 
speedX_wall=1

speedY_wall2=1

# wall picture 
wallP=pygame.image.load('wall.png')
wallP=wallP.convert_alpha()
transform_wall=pygame.transform.scale(wallP,(wall_w+10,wall_h+10))

wallP2=pygame.image.load('wall2.png')
wallP2=wallP2.convert_alpha()
transform_wall2=pygame.transform.scale(wallP2,(wall_w2,wall_h2))


###################### music ######################
                                           #
pygame.mixer.music.load('introSong.mp3')   #
pygame.mixer.music.set_volume(0.4)         #
pygame.mixer.music.play(loops=-1)          #
                                           #
eat=pygame.mixer.Sound('eat.wav')          #
eat.set_volume(0.6)                        #
                                           #
                                           #
no_music=pygame.image.load('noMusic.png')  #
no_music=no_music.convert_alpha()          #
no_music_transform=pygame.transform.scale(no_music,(50,50))#
#
#
wall1_hit=pygame.mixer.Sound('wall1_hit.wav')#
wall1_hit.set_volume(0.6)#
#

###########################################
# intro function
def intro_Game():

    mainW.blit(intro_change,(0,0))
    intro_snake=font2.render('Snake',1,white)
    intro_play=font3.render('Play',1,white)
    ins=font3.render('instructions',1,white)
    greetings=font3.render('welcome',1,white)
    mainW.blit(intro_change,(0,0))
    mainW.blit(intro_snake,(190,35))
    pygame.draw.rect(mainW,white,(play_x,play_y,play_w,play_h),2)
    pygame.draw.rect(mainW,white,(ins_X,ins_Y,ins_w,ins_h),2)
    mainW.blit(intro_play,(play_x+10,play_y+3))
    mainW.blit(ins,(ins_X,ins_Y))
    mainW.blit(greetings,(width//2-100,200))
    mainW.blit(no_music_transform,(750,500))
    pygame.display.update()
    
# instruction function 
def instructions():
    mainW.fill(black)
    instruction_1=font3.render('if you eat apples, the snake gets bigger',1,white)
    instruction_2=font3.render('if you eat the kiwi, the snake gets twice as big',1,white)
    instruction_3=font3.render('if you eat the banana, the snake gets smaller',1,white)
    instruction_4=font3.render('beware of the walls',1,white)
    instruction_5=font3.render('press the up arrow key to start the game and the snake to move',1,white)
    instruction_6=font3.render('if you eat an apple, your score goes up by one, if you eat the kiwi',1,white)
    instruction_7=font3.render('your score goes up by two',1,white)
    instruction_8=font3.render('your time restarts to 12 if you eat the apple',1,white)
    instruction_9=font3.render('your time restarts to 22 if you eat the kiwi',1,white)
    instruction_10=font3.render('press escape button to exit from the main game',1,white)
    instruction_11=font3.render('game is over when your timer reaches zero or score is less than 0',1,white)
    instruction_12=font3.render('snake gets smaller when it eats itself,essentially he eats himself!',1,white)
    mainW.blit(transform_apple,(550,30))
    mainW.blit(instruction_1,(30,30))
    mainW.blit(instruction_2,(30,120))
    mainW.blit(kiwi_transform,(600,120))
    mainW.blit(instruction_3,(30,150))
    mainW.blit(instruction_4,(30,180))
    mainW.blit(instruction_5,(30,210))
    mainW.blit(instruction_6,(30,240))
    mainW.blit(instruction_7,(30,270))
    mainW.blit(instruction_8,(30,300))
    mainW.blit(instruction_9,(30,330))
    mainW.blit(instruction_10,(30,360))
    mainW.blit(instruction_11,(30,420))
    mainW.blit(instruction_12,(10,500))
    mainW.blit(apple_change,(560,140))
    mainW.blit(arrow_keys_resize,(800,500))
    intro_play=font3.render('Play',1,white)
    pygame.draw.rect(mainW,magenta,(play_x,play_y,play_w,play_h),2)
    mainW.blit(intro_play,(play_x+10,play_y+3))
    pygame.display.update()

    
def distance(x1,y1,x2,y2): # function for collision 
    dis=sqrt((x2-x1)**2+(y2-y1)**2) # uses pythagorem theorem
    return dis

def redrawScreen(): # main windown function 
    mainW.blit(change,(0,0)) # display the score and the time left 
    score=font4.render('score : '+str(apple_eaten),1,white)
    elapsed=font4.render("time : "+str(time_left),1,white)
    mainW.blit(score,(width-200,10))
    mainW.blit(elapsed,(20,10))
    colourCLR=(randrange(0,255),randrange(0,255),randrange(0,255))
    for i in range(len(segX)): # draw the body of the sbake 
        pygame.draw.ellipse(mainW,colourCLR,(segX[i],segY[i],body_width,body_height),outline)
        #add the images of the snake according to the direction of movement 
        for i in range(len(segX)):
            if  speedX==-hSpeed and speedY==0:
                snake_face=snake_head_transformL
                mainW.blit(snake_face,(segX[0],segY[0]))
                snake_body=body2_transform
                mainW.blit(snake_body,(segX[i],segY[i]))

            elif speedX==hSpeed and speedY==0:
                snake_face=snake_head_transformR
                mainW.blit(snake_face,(segX[0],segY[0]))
                snake_body=body2_transform
                mainW.blit(snake_body,(segX[i],segY[i]))

            elif speedX==0 and speedY==-vSpeed:
                snake_face=snake_head_transform
                mainW.blit(snake_face,(segX[0],segY[0]))
                snake_body=body1_transform
                mainW.blit(snake_body,(segX[i],segY[i]))

            else:
                snake_face=snake_head_transformD
                mainW.blit(snake_face,(segX[0],segY[0]))
                snake_body=body1_transform
                mainW.blit(snake_body,(segX[i],segY[i]))


    for i in range(len(segX)): # checks if the snake leaves the screen
        if segX[i]<0: # if it goes out of the screen, it would come back from the other side 
            segX[i]=width
        if segX[i]>width:
            segX[i]=0
        if segY[i]<0:
            segY[i]=height
        if segY[i]>height:
            segY[i]=0
            # gives new values to the coordinate 
    pygame.display.update()

def kiwi(): # draw the good kiwis and update the screen 
    mainW.blit(kiwi_transform,(kiwi_X,kiwi_Y))
    pygame.display.update()
    

def apples(): # draw the apple 
    #pygame.draw.circle(mainW,red,(apple_X,apple_Y),apple_R,outline)
    mainW.blit(transform_apple,(apple_X-15,apple_Y-15))
    pygame.display.update()

def poisonous_banana(): # generate bad banana 
    mainW.blit(apple_change,(apple_pX-25,apple_pY-25))
    pygame.display.update()

def game_over(): # game over screen
    mainW.blit(whole_final,(0,0))
    over=font3.render('Game Over',1,white)
    final_score=font3.render('Your final score is : '+str(apple_eaten),1,white)
    quit_button=font3.render('Quit',1,white)
    pygame.draw.rect(mainW,magenta,(100,550,90,30),2)
    mainW.blit(final_score,(width//2-100,height//2+200))
    mainW.blit(over,(width//2-45,height//2+100)) # quit button 
    mainW.blit(quit_button,(100,550))
    pygame.display.update()

def wall():# first wall (the dark one)
    pygame.draw.rect(mainW,red,(wall_X,wall_Y,wall_w,wall_h),2)
    mainW.blit(transform_wall,(wall_X,wall_Y))
    pygame.display.update()

def wall2(): # the second wall (the glowing one)
    pygame.draw.rect(mainW,red,(wall_X2,wall_Y2,wall_w2,wall_h2),2)
    mainW.blit(transform_wall2,(wall_X2,wall_Y2))
    pygame.display.update()

    
# boolean variables for each screen in order intro, instructions,main and end 
intro=True
inst=False
play=False
endGame=False

while intro and not play : # while the intro is true 
    for i in pygame.event.get(): # check for events 
        if i.type==pygame.QUIT: # if the close button is pressed quit 
            intro=False
        (cursorX,cursorY)=pygame.mouse.get_pos() # mouse position 
        if i.type==pygame.MOUSEBUTTONDOWN:
            if cursorX>play_x and cursorX<play_x+play_w and cursorY>play_y and cursorY<play_y+play_h: # if the play button is pressed, enter the main game 
                play=True
                intro=False
            if cursorX>ins_X and cursorX<ins_X+ins_w and cursorY>ins_Y and cursorY<ins_Y+ins_h: # if the instruction button is pressed, enter instructions 
                intro=False
                inst=True

            if cursorX>750 and cursorX<800 and cursorY>500 and cursorY<550: # if the mute button is pressed, mute the themesong 
                pygame.mixer.music.pause()

        intro_Game()
                
        
while inst: # instruction window 
    for i in pygame.event.get():
        if i.type==pygame.QUIT: # checks for events 
            inst=False
        (cursorX,cursorY)=pygame.mouse.get_pos()
        if i.type==pygame.MOUSEBUTTONDOWN: # if the play button is pressed, enter the main game 
            if cursorX>play_x and cursorX<play_x+play_w and cursorY>play_y and cursorY<play_y+play_h:
                play=True
                inst=False
    instructions()


            
    
while play==True and not intro: # main game loop 
    for event in pygame.event.get(): # check for events   
        if event.type==pygame.QUIT:
            play=False
    # timer 
    eventTime=pygame.time.get_ticks()/1000
    keys=pygame.key.get_pressed()
    # subtracts the time 
    time_left=round(time-(eventTime-startTime),2)
    
    #count_from=eventTime-startTime
          # movement of the snake 
    if keys[pygame.K_LEFT] and speedX!=hSpeed: # left 
        speedX=-hSpeed
        speedY=0 # restrict the movments so the snake does not go back into itself 
    if keys[pygame.K_RIGHT]  and speedX!=-hSpeed: # right 
        speedX=hSpeed
        speedY=0
    if keys[pygame.K_UP] and speedY!=vSpeed: # up
        speedX=0
        speedY=-vSpeed
    if keys[pygame.K_DOWN]  and speedY!=-vSpeed: # down 
        speedX=0
        speedY=vSpeed

    if keys[pygame.K_ESCAPE]: # if the escape is pressed, exit the game 
        play=False

    
    for i in range(len(segX)-1,0,-1): # each segment takes the position of the previous one 
        segX[i]=segX[i-1]
        segY[i]=segY[i-1]
        
    for i in range(len(segX)): # checks the collision for the apple 
        if kiwi_X!=apple_X or kiwi_Y!=apple_Y or apple_pX!=apple_X or apple_pY!=apple_Y: # the apple should not be on any fruit 
            if distance(segX[i],segY[i],apple_X,apple_Y)<apple_R+15: # if the snake eats the apple 
                eat.play() # eat sound 
                time=perf_counter()-10*-1 # restart time to 10
                segX.append(segX[-1]) # add one segment 
                segY.append(segY[-1])
                apple_X=randrange(70,width-50) # assign new values to the apple 
                apple_Y=randrange(70,height-50)
                apple_pX=randrange(70,width-50) 
                apple_pY=randrange(70,height-50)
                apple_eaten+=1
        # increase the score 

    for i in range(len(segX)): # kiwi collision 
        if distance(segX[i],segY[i],kiwi_X,kiwi_Y)<kiwi_width: # if the snake eats the kiwi 
            if kiwi_X!=apple_X or kiwi_Y!=apple_Y or apple_pX!=kiwi_X or apple_pY!=kiwi_Y: # kiwi not on any other fruit 
                eat.play() # eat sound 
                kiwi_X=randrange(70,width-50) # assign new values to the kiwi
                kiwi_Y=randrange(70,height-50)
                segX.append(segX[-1]) # add two parts to the snake 
                segY.append(segY[-1])
                segX.append(segX[1])
                segY.append(segY[1])
                apple_eaten+=2 # add the score by 2
                time=perf_counter()-20*-1 # restart the time to 2 
            
    
    for i in range(len(segX)-1,-1,-1): # checks the collision of the banana
        if distance(apple_pX,apple_pY,segX[i],segY[i])<apple_pR+20: # if the snake eats the banana 
            if apple_pX!=apple_X or apple_pY!=apple_Y or apple_pX!=kiwi_X or apple_pY!=kiwi_Y: # banana should not be on any fruit 
                eat.play() # eat sound 
                segX.remove(segX[-1])
                segY.remove(segY[-1]) # remove a segment 
                apple_eaten-=1 # decrease the score
                apple_pX=randrange(70,width-30) # assing new values to the banana
                apple_pY=randrange(70,height-30)
    
    for i in range(len(segX)): # checks if the snake hits the second wall 
        if segX[i]>wall_X2 and segX[i]<wall_X2+wall_w2 and segY[i]>wall_Y2 and segY[i]<wall_Y2+wall_h2:
           wall1_hit.play()# if yes, enter the end screen 
           play=False
           endGame=True
           
    for i in range(len(segX)): # if the snake hits the first wall 
        if segX[i]>wall_X and segX[i]<wall_X+wall_w and segY[i]>wall_Y and segY[i]<wall_Y+wall_h:
            wall1_hit.play()
            play=False# exit the main game and enter end screen 
            endGame=True

    for i in segX: # if the length of the snake is 1, the game is over 
        if len(segX)==1 or len(segY)==1:
            play=False
            endGame=True
            # wall 1 moves horizontally 
    wall_X+=speedX_wall # restriction on the movement to make it move backwards 
    if wall_X>width:
        speedX_wall*=-1
    if wall_X<0:
        speedX_wall*=-1
    # wall 2 moves vertically 
    wall_Y2+=speedY_wall2 # restriction on the movmement of the wall so it dosent exit the screen 
    if wall_Y2>height:
        speedY_wall2*=-1
    if wall_Y2<0:
        speedY_wall2*=-1
    # move the head with the body of the snake 
    segX[0]+=speedX
    segY[0]+=speedY
     # main functions 
    redrawScreen()
    wall2()
    wall()
    apples()
    poisonous_banana()
    kiwi()

    for i in range(len(segX)-1,2,-1): # check if the snake hits to itself 
        if segX[0]==segX[i] and segY[0]==segY[i] : 
            del segX[i:-1] # delets the part from which it eat
            apple_eaten-=5 # reduce the score by 5
        
    # if the score is higher than 30,
    if apple_eaten>=30:
    # double the speed of the walls 
        wall_X+=2*speedX_wall

        wall_Y2+=2*speedY_wall2

    # if the score is higher than 60
    if apple_eaten>=60: # triple the speed of the walls 
        wall_X+=3*speedX_wall
        wall_Y2+=3*speedY_wall2

                        
                        
    if apple_eaten>=30: # increase the speed of the game as the score gets higher 
        pygame.time.delay(9)

    elif apple_eaten>=60:
        pygame.time.delay(3)

    elif apple_eaten<30:
        pygame.time.delay(13)
        # if the score is less than 0, game is over 
    if apple_eaten<0:
        play=False
        endGame=True
        # if the time equals zero the game is over 
    if time_left==00.00:
        play=False
        endGame=True

        # if the time equals zero, the game is over 
    if time_left<0.00:
        play=False
        endGame=True

while endGame: # endscreen 
    for i in pygame.event.get():
        (x,y)=pygame.mouse.get_pos()
        if i.type==pygame.MOUSEBUTTONDOWN:
           if  x>100 and x<190 and y>550 and y<580: # quit button 
               endGame=False
    game_over()  # end screen 

   
pygame.quit()
# always quit pygame 
