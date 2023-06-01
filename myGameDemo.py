import pygame, sys, math, random, time             
from Wall import *
from FireBall import *
from MasterChief import *
from MyGameHud import *
from ScreenLoader import *
from Alert import *
pygame.init()
pygame.mixer.pre_init(44100, -16, 1, 512)

if not pygame.mixer: print("Warning, sound disabled")

debug = False
startTime = time.time()

if not pygame.font: print('Warning, fonts disabled')

clock = pygame.time.Clock();

size = [1800, 1000]
screen = pygame.display.set_mode(size)
time = 0
         


mode = "StartGame"

while True:
    bgimage = pygame.image.load("Images/Backgrounds/StartScreen-basic.png")
    bgrect = bgimage.get_rect()
    pygame.mixer.music.load("Sounds/R-Menu-EditedAgain - Copy.ogg")
    pygame.mixer.music.play(loops=-1)
    while mode == "StartGame":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode="Play"
        screen.fill((100, 100, 100))
        screen.blit(bgimage, bgrect)
        pygame.display.flip()
        clock.tick(100)


    counter = 0;
    
    score = MyGameHud("Health: ",[0,0])
    timer = MyGameHud("Time: ",[900-200,0])
    
    scn = 1
    tiles = loadScreen(str(scn)+".scn")
    player = MasterChief(4, tiles[0])
    objects = [player]  
    walls = tiles[1]
    spawners = tiles[3]
    cans = tiles[2]
    
    kills = 1000;
    pygame.mixer.music.load("Sounds/Main.ogg")
    pygame.mixer.music.play(loops=-1)
         
    while mode == "Play":
        if debug: 
            startTime = time.time()
            print("-------------", len(walls))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.goKey("left")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.goKey("right")
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.goKey("jump")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        mode = "Restart"
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.goKey("sleft")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.goKey("sright")
                
                
        
        if debug: print("input done: ", time.time()-startTime)
        for spawner in spawners:
            if spawner.update(size):
                objects += [spawner.spawn()]
                for object in objects:
                    if objects[-1].objectCollide(object):
                        objects.remove(objects[-1])
                        break
        if debug: print("object spawn done: ", time.time()-startTime)
        
          
    
        for object in objects:
            if object.update(size)=="bottom":
                mode = "Game Over"
            
        if debug: print("object update done: ", time.time()-startTime)
        
        time += 1
        timer.update(int(time/100))
        score.update(kills)
        if kills <= 0:
            mode = "Game Over"
        if debug: print("timer update done: ", time.time()-startTime)
            
        for hittingobject in objects:
            for hitobject in objects:
                if hittingobject.objectCollide(hitobject):
                    if hittingobject.kind == "player":
                        objects.remove(hitobject)
                        kills -=50
            for wall in walls:
                hittingobject.wallTileCollide(wall)
        if debug: print("collisions done: ", time.time()-startTime)
                        
        for can in cans:
            if player.objectCollide(can):
                scn += 1
                tiles = loadScreen(str(scn)+".scn")
                player = MasterChief(4, tiles[0])
                objects = [player]  
                walls = tiles[1]
                spawners = tiles[3]
                cans = tiles[2]
        
        screen.fill((100, 100, 100))
        if debug: print("\t fill done: ", time.time()-startTime)
        for spawner in spawners:
            screen.blit(spawner.image, spawner.rect)
        if debug: print("\t spawners done: ", time.time()-startTime)
        for object in objects:
            screen.blit(object.image, object.rect)
        if debug: print("\t objects done: ", time.time()-startTime)
        for wall in walls:
            screen.blit(wall.image, wall.rect)
        if debug: print("\t walls done: ", time.time()-startTime)
        screen.blit(timer.image, timer.rect)
        screen.blit(score.image, score.rect)
        screen.blit(player.image, player.rect)
        for can in cans:
            screen.blit(can.image, can.rect)
        if debug: print("\t cans done: ", time.time()-startTime)
        screen.blit(timer.image, timer.rect)
        screen.blit(score.image, score.rect)
        screen.blit(player.image, player.rect)
        
        pygame.display.flip()
        if debug: print("draw done: ", time.time()-startTime)
        clock.tick(100)
        if (clock.get_fps() < 2):
            print("slow", clock.get_fps())
            #debug = True
        else:
            debug = False
    
    alert = Alert([800,500])
    
    pygame.mixer.music.load("Sounds/Riff.ogg")
    pygame.mixer.music.play(loops=-1) 
    
    while mode == "Game Over":
        if debug: 
            startTime = time.time()
            print("-------------", len(walls))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode = "Play"
        
        screen.fill((100, 100, 100))
        screen.blit(alert.image, alert.rect)

        pygame.display.flip()
        clock.tick(100)
    
    while mode == "Restart":
        time = 0
        timer.update(int(time/100))
        mode="Play"
