from engine import *

def load():
    pos = {"x":0,"y":0}
    dir = {"x":0,"y":0}
    running = True
    maxTime = 10
    time = 0 
    delt = 0.01
    x_range = [0,100]
    s = 0
    while running:
        time += delt
        o = {
        "name":"bar",
        "shape":"rect",
        "width":100,
        "height":100,
        "color":(100,100,100)
        }
        # s += 0.01
        # pos["x"] = int(s)

        # print(pos)
        animation = {
            "pos":pos,
            "dir":dir,
            "obj":o
        }
        if time >= maxTime:
            running = False
    return animation