from engine import *
run = True
def load():
    pos = {"x":0,"y":0}
    dir = {"x":0,"y":0}
    running = True
    maxTime = 10
    time = 0 
    delt = 0.01
    x_range = [0,100]
    s = 0
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
        time += 0.01
        new_pos = animation["pos"]
        new_pos["x"] += 0.1

        output = {
        "pos":new_pos,
        "dir":animation["dir"],
        "obj":animation["obj"],
        "time": time,
        "maxTime":maxTime,
        "running":animation["running"],
        "delt": animation["delt"],
        "color":(250,250,250),
        "width":100,
        "height":180,
        "shape":"rect"
    }
        if time >= maxTime:
            animation["running"] = False
    return output