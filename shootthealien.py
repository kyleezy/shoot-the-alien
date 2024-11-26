import pgzrun 
import random
WIDTH=600
HEIGHT=400
TITLE="alien"
spencer=Actor("alien")
spencer.pos=(50,50)
message=""
def draw():

    screen.clear()
    screen.fill("red") 
    spencer.draw()
    screen.draw.text(message,(200,100))
def on_mouse_down(pos):
    global message
    if spencer.collidepoint(pos): 
        message="good shot"
        x=random.randint(50,550)
        y=random.randint(50,350)
        spencer.pos=(x,y)
    else :
        message="you missed"




pgzrun.go()