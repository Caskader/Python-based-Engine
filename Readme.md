
### This is a Python-based Engine made by Siddh Vasa (Caskader)

# Get started

Paste the [engine.py](engine.py) file in your project folder and make a `main.py` file .

Then paste and run file :-

`from engine import newFile()`

`newFile()`

This will create a template for the Engine

# Basics

This engine is based on ready-made assembly system 

It simplyfies the process of making Physics, Object, Collision and Displaying it .

It is based on the python moduel [Pygame](https://www.pygame.org/news) .

## Understanding the template

---

### Default Sets
First we set the Clock and some Defaut settings in

`a = MainEngine.default_sets(1000,1000,39)`

`surface = a["surface"]`

### Main Variables

Then the Variables for Things like Keymap, Position, Direction, Camera Control, Object Creation .etc

Here the Numders 97,100,119 and 115 represents the W,A,S,D Keys.This keymap is used for making the Physics of an object.

`keys = {
    "x+":97,
    "x-":100,
    "y+":119,
    "y-":115
}`

Here the Direction and Position is Determined .The Default is x:0 , y:0 .  This would be later used for makeing an Object .  

`dir={"x":0,"y":0}
pos={"x":0,"y":0}`

### Main loop

Everything here is the Main FUntion of Collision, Physics and Object. The main Variables are used here.

`running = True`

`while running:`

`    surface.fill((0,0,0))`

`   for event in pygame.event.get():`

`     if event.type == pygame.QUIT:`

`          running = False`
    
`pygame.display.update()`