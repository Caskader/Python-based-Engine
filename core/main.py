
#import needed moduels
from lib.engine import MainEngine,PhysicsEngine
from core import ok
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

# main loop
running = True
while running:
    surface.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ok.run()
    
    pygame.display.update()

#end
MainEngine.quitEN()
        