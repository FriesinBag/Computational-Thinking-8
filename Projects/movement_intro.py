# Section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass()


t = codesters.Sprite("fox")
stage.set_background("fall")


def move_up(sprite):
	sprite.move_up(1)
t.event_key("up", move_up)

def move_down(sprite):
	sprite.move_down(1)
t.event_key("down", move_down)
    
def move_left(sprite):
	sprite.move_left(1)
t.event_key("left", move_left)
    
def move_right(sprite):    
	sprite.move_right(1)
t.event_key("right", move_right)

def draw(sprite):
	sprite.pen_down()
t.event_key("q", draw)

def stop_drawing(sprite):
	sprite.pen_up()
t.event_key("w", stop_drawing)

def erase(sprite):
	sprite.pen_clear()
t.event_key("e", erase)

def red_pen(sprite):
	sprite.set_color("red")
t.event_key("r", red_pen)

