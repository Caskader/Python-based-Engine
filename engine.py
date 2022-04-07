from turtle import color, width
import pygame

pygame.init()
direction = {"x": 0, "y": 0, 3: False}
direction2 = {"x": 0, "y": 0, 3: False}


def newFile():
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


class MainEngine():
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

    def bal_Physics(event, speed: int):
        direction2 = {"x": speed, "y": speed}
        return direction2
