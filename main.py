
#import needed moduels
from engine import MainEngine,PhysicsEngine
from player import obj1
import pygame

#create a surface
a = MainEngine.default_sets(1000,1000,39)
surface = a["surface"]

#create keyset
keys = {
    "x+":97,
    "x-":100,
    "y+":119,
    "y-":115}
o  = obj1()
# main loop
running = True
while running:
    surface.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    MainEngine.add_object(surface,o)
    pygame.display.update()

#end
MainEngine.quitEN()
        