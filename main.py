
    #import needed moduels
from engine import MainEngine,PhysicsEngine
from objects import bar
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

bar1 = bar.bar() 
# main loop
running = True
while running:
    surface.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    PhysicsEngine.add_object(surface,bar1)
    
    pygame.display.update()

#end
MainEngine.quitEN()
        