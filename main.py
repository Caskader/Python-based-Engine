#import needed moduels
from engine import MainEngine,PhysicsEngine
import pygame

#create a surface
a = MainEngine.default_sets(1000,1000,39)
surface = a["surface"]

#create keyset
keys = {
    "x+":97,
    "x-":100,
    "y+":119,
    "y-":115
}

# values
b = 0
c= 0
dir={"x":0,"y":0}
pos={"x":0,"y":0}
pos2={"x":100,"y":0}
obj = {
    "name":"bar",
    "shape":"rect",
    "width":10,
    "height":100,
    "color":(100,100,100)
}
EN1 = [pos["x"]]
EN2 = [pos2["x"]]
camSpeed = 10
1# main loop
running = True
while running:
    surface.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                for i in EN1:
                    b += camSpeed
                    pos["x"] += b
                for i in EN2:
                    c += 5
                    pos2["x"] += c
            dir  = PhysicsEngine.moving_body(keys,event,1)

    PhysicsEngine.add_object(pos,dir,surface,obj) 
    PhysicsEngine.add_object(pos2,dir,surface,obj) 
    pygame.display.update()

#end
MainEngine.quitEN()
    