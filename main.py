
        #import needed moduels
from engine import MainEngine,PhysicsEngine
import pygame
from pygame import mixer
import time

    #create a surface
a = MainEngine.default_sets(1000,750,2)
surface = a["surface"]

    #create keyset
keys = {
    "x+":97,
    "x-":100,
    "y+":119,
    "y-":115
}

dir={"x":0,"y":0}
pos={"x":10,"y":10}
dir2={"x":1,"y":0}
pos2={"x":490,"y":10}
pos3={"x":980,"y":0}

obj = {
    "name":"bar",
    "shape":"rect",
    "width":10,
    "height":100,
    "color":(250,250,250)
}
obj2 = {
    "name":"bar",
    "shape":"rect",
    "width":15,
    "height":15,
    "color":(10,200,200)
}

d = {"x":0.5,"y":0.5}

player1 = 0
player2 = 0
def bal_Physics(collision_l,collision_r, speed: int):
        if collision_l == True:
            x = mixer.Sound('hit.mp3')
            x.play()
            d["x"] = speed
        elif collision_r == True:
            x = mixer.Sound('hit.mp3')
            x.play()
            d["x"] = -speed 
        return d

prev_time = time.time()
dt = 0
    # main loop
running = True
while running:
        surface.fill((0,0,0))

        # now = time.time()
        # dt = now - prev_time
        # prev_time = now


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                dir = PhysicsEngine.V_move(event,1)
        if pos2["x"] >= 990:
            player1 += 1
            pos2['x'] =  530
            pos2["y"] = 530
        if pos2["x"] <= 0:
            player2 += 1
            pos2["x"] = 530
            pos2['y'] = 530
        if pos2["y"] >= 750:
            dir2['y'] = -0.5
        if pos2["y"] <= 0:
            dir2['y'] = 0.5

        pos3['y'] = pos2['y'] - 30

        o1 = PhysicsEngine.add_object(pos,dir,surface,obj)
        o3 = PhysicsEngine.add_object(pos3,dir,surface,obj)
        o2 = PhysicsEngine.add_object(pos2,dir2,surface,obj2)
        collied_l = PhysicsEngine.collier_square(o1,o2)
        collied_r = PhysicsEngine.collier_square(o2,o3)
        dir2 = bal_Physics(collied_l,collied_r,0.5)
        # print(o1.colliedrect())
        # print(pos2['x'])
        # print((player1,player2))
        # s = pygame.time.Clock()
        # s.tick(10)
        # print(s)

        pygame.display.update()

    #end
MainEngine.quitEN()
        