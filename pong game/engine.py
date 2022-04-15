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

    dir={"x":0,"y":0}
    pos={"x":0,"y":0}

    obj = {
        "name":"bar",
        "shape":"rect",
        "width":10,
        "height":100,
        "color":(100,100,100)
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
        print(os.popen("mkdir Main").read)
        print("writing file (main.py)...")
        with open("Main/main.py", "w+") as f:
            f.write(boiler_plate)
        print("done")

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
        os.popen("mkdir animations")
        print("writting file (anima.py) ...")
        with open("animations/anima.py","w+") as f:
            f.write(boiler_plate2)
        print("done")

        print("writing file (dock.py)")
        with open("dock.py","w+") as f:
            s = """
from engine import docker
            """
            f.write(s)
        print("done")

class MainEngine():
    direction2 = {"x":0,"y":0}
    def _get_obj(name:str):
        input = {
            1:10
        }
        with open(name + ".obj","w+") as file:
            file.write(str(input))
        with open(name + ".obj","r") as file:
            output = file.readline()
        return output

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


    def add_object(pos: dict[2], dir: dict[2], surface, obj) -> None:
        pos["x"] += dir["x"]
        pos["y"] += dir["y"]
        color = obj["color"]
        width = obj["width"]
        height = obj["height"]

        if obj["shape"] == "rect":
            a = pygame.draw.rect(surface, color, (pos["x"], pos["y"], width, height))
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

    def bal_Physics(keyset,event, speed: int):
        if event.key == keyset["x+"]:
            direction2["x"] = speed
        if event.key == keyset["x-"]:
            direction2["x"] = -speed
        if event.key == keyset["y+"]:
            direction2["y"] = speed
        if event.key == keyset["y-"]:
            direction2["y"] = -speed 
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