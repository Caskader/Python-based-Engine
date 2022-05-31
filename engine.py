import pygame
import json

pygame.init()
direction = {"x": 0, "y": 0, 3: False}
direction2 = {"x": 0, "y": 0, 3: False}


class docker():
    def __init__(self) -> None:
        # don't remove this code
        print("welcome to the Pygame Engine ,made by Sidhh Vasa(Caskader)")
        self.version = "0.5.8"

    def new_project():
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
        with open("dock.py", "w+") as f:
            s = """
from engine import docker
            """
            f.write(s)
        print("done")

    def new_animation(name: str):
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
        with open(name, "w+") as f:
            f.write(boiler_plate2)
        print("done")

        print("writing file (dock.py)")
        with open("dock.py", "w+") as f:
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
        with open(name + ".py", "w+") as f:
            f.write(x)

    def extract_obj(simple_file, extraction):
        data = ""
        with open(simple_file, "r") as f:
            print("reading file ...")
            a = f.read()
            f.close()
        data = json.loads(a)

        print("compilling file ...")

        for i in data['layers']:
            print("creating objects ...")
            with open(extraction+"/"+i + ".py", "w+") as f:
                try:
                    temp = """
class """+"obj" +"""():
    def __init__(self) -> None:
        self.pos = """ + str("{'x':" + str(data["x"]) + ",'y':" + str(data['y']) + "}") + """
        self.dir = {'x':0,'y':0}
        self.width = """ + str(data['width'])+"""
        self.height = """+str(data['height'])+"""
        self.shape = None
        self.image = '"""+ i+"""'
    """
                    f.write(temp)
                    f.close()
                    print("done ...")
                except:
                    print("ERROR:not able to compile the file, see that the file was compiled in simple format")
            print("done compliling")
        with open("dock.py", "w+") as f:
            s = """
from engine import docker
            """
            f.write(s)
            
    def new_shaders(name):
        with open(name + ".py","w+") as f:
            t = """

from engine import *
import PIL

color = (10,10,10)


            """
            f.write(t)

    def startEn(w,h,c,running):
        MainEngine.default_sets(w,h,c)
        while running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    MainEngine.quitEN()
            LiveEngine.reload()

class LiveEngine():
    def run(file,running):
        MainEngine.default_sets(100,100,10)
        code = ""
        # MainEngine.default_sets()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        with open(file,"r")as f:
                            code = f.readlines()
                            f.close()
            i = 0
            for line in code:
                exec(code[i])
                i += 1

            pygame.display.update()
        MainEngine.quitEN()
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

    def add_child(obj1, obj2, a):
        pos = obj1 + a
        return pos
    
    def add_object(surface, obj) -> None:
        obj.pos["x"] += obj.dir["x"]
        obj.pos["y"] += obj.dir["y"]
        width = obj.width
        height = obj.height

        a = None
        # try:
        if obj.shape == "rect":
            color = obj.color
            a = pygame.draw.rect( surface, color, (obj.pos["x"], obj.pos["y"], width, height))
        if obj.shape == None:
            img = pygame.image.load(obj.image)
            surface.blit(img,(obj.pos['x'],obj.pos['y']))
        # except:
        #     print("an error occured")
        return a

class PhysicsEngine():
    def collier_square(obj1, obj2):
        return obj1.colliderect(obj2)

    def moving_body(keyset: dict, event, speed: int) -> dict[3]:
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


class ProceduralRenderEngine():
    def add_animation(name: str):
        with open(name + ".py", "w+") as f:
            template = """
from engine import ProceduralRenderEngine
            
pos = {"x":0,"y":0}
dir = {"x":0,"y":0}
# main animation loop


            """
            f.write(template)
