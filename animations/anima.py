    
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
        