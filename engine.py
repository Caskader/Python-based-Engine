import pygame
import os

pygame.init()
direction = {"x": 0, "y": 0, 3: False}
direction2 = {"x": 0, "y": 0, 3: False}

class docker():
    def newProject():
        print("creating template ...")
        boiler_plate = """
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

# main loop
running = True
while running:
    surface.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

#end
MainEngine.quitEN()
        """
        print("writing file (main.py)...")
        with open("main.py", "w+") as f:
            f.write(boiler_plate)
        print("done")

        print("writing file (dock.py)")
        with open("dock.py","w+") as f:
            s = """
from engine import docker
            """
            f.write(s)
        print("done")

    def new_animation(name:str):
            print("creting template ...")
            boiler_plate2 = """    
from engine import *
run = True
def load():
pos = {"x":0,"y":0}
dir = {"x":0,"y":0}
running = True
maxTime = 10
time = 0 
delt = 0.01
o = {
"name":"bar",
"shape":"rect",
"width":100,
"height":100,
"color":(100,100,100)
}
animation = {
    "pos":pos,
    "dir":dir,
    "obj":o,
    "time": time,
    "maxTime":maxTime,
    "running":running,
    "delt": delt,
    "color":(250,250,250),
    "width":100,
    "height":180,
    "shape":"rect"
}
return animation

def run(animation) -> dict:
time = animation["time"]
maxTime = animation["maxTime"]
while animation["running"]:

    output = {
    "pos":animation["pos"],
    "dir":animation["dir"],
    "obj":animation["obj"],
    "time": time,
    "maxTime":maxTime,
    "running":animation["running"],
    "delt": animation["delt"],
    "color":animation["color"],
    "width":animation['width'],
    "height":animation["height"],
    "shape":"rect"
}
    if time >= maxTime:
        animation["running"] = False
return output
        """
            print("writting file (anima.py) ...")
            with open(name,"w+") as f:
                f.write(boiler_plate2)
            print("done")

            print("writing file (dock.py)")
            with open("dock.py","w+") as f:
                s = """
from engine import docker
            """
                f.write(s)
            print("done")
    
    def new_obj(name):
        x = """
class obj1():
    def __init__(self) -> None:
        self.pos = {'x':0,'y':0}
        self.dir = {'x':0,'y':0}
        self.width = 10
        self.height = 100
        self.color = (250,250,250)
        self.shape = 'rect'
    """
        with open(name + ".py","w+") as f:
            f.write(x)

class MainEngine():

    def quitEN() -> None:
        pygame.quit()
        quit()

    def default_sets(window_w: int, window_h: int, clockt: int) -> dict[2]:
        window = pygame.display.set_mode((window_w, window_h))
        clock = pygame.time.Clock()
        clock.tick(clockt)
        return {"surface": window, "clock": clock}

    def get_event():
        return pygame.event.get()
    
    def add_child(obj1,obj2,a):
        pos = obj1 + a
        return pos


class PhysicsEngine():
    def collier_square(obj1,obj2):
        return obj1.colliderect(obj2)


    def add_object(surface, obj) -> None:
        obj.pos["x"] += obj.dir["x"]
        obj.pos["y"] += obj.dir["y"]
        color = obj.color
        width = obj.width
        height = obj.height

        a = None
        try:
            if obj.shape == "rect":
                a = pygame.draw.rect(surface, color, (obj.pos["x"], obj.pos["y"], width, height))
        except:
            print("an error occured")
        return a

    def moving_body( keyset:dict,event, speed:int) -> dict[3]:
        direction = {"x": 0, "y": 0, 3: False}
        if event.type == pygame.KEYDOWN:
            if event.key == keyset["x+"]:
                direction["x"] = -speed
            elif event.key == keyset["x-"]:
                direction["x"] = speed
            elif event.key == keyset["y+"]:
                direction["y"] = -speed
            elif event.key == keyset["y-"]:
                direction["y"] = speed
        return direction

    def V_move(event, speed: int):
        if event.type == pygame.KEYDOWN:
            if event.key == 119:
                direction["y"] = -speed
            elif event.key == 115:
                direction["y"] = speed
        return direction

    def H_move(event, speed: int):
        if event.type == pygame.KEYDOWN:
            if event.key == 97:
                direction["x"] = -speed
            elif event.key == 100:
                direction["x"] = speed
        return direction

    def bal_Physics(event, speed: int):
        direction2 = {"x": speed, "y": speed}
        return direction2

class  ProceduralRenderEngine():
    def add_animation(name:str):
        with open(name + ".py","w+") as f:
            template = """
from engine import ProceduralRenderEngine
            
pos = {"x":0,"y":0}
dir = {"x":0,"y":0}
# main animation loop


            """
            f.write(template)