import pgzrun
from random import randint

WIDTH = 400     
HEIGHT = 400

dots = []
lines = []

next_dot = 0
timer = 0
time_out = 30

for dot in range(10):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)


def draw():
    global timer
    global next_dot

    screen.fill("black")

    number = 1

    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()

        number += 1

    for line in lines:
        screen.draw.line(line[0], line[1], (255, 255, 255))


    if(next_dot == 10):
        screen.draw.text("Win", center=(200,130), color=(255,0,0), fontsize=200)
        screen.draw.text(str(round(timer, 2)), center=(200,230), color=(255,0,0), fontsize=80)
    else:
        screen.draw.text(str(round(timer, 2)), topleft=(10,10), color=(255,0,0), fontsize=30)


    if(timer >= time_out):
        screen.fill("black")
        screen.draw.text("Game Over", center=(200,200), color=(255,0,0), fontsize=100)
        

def on_mouse_down(pos):
    global next_dot
    global lines

    if(next_dot < 10):
        if(dots[next_dot].collidepoint(pos)):
            if(next_dot):
                lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
            next_dot += 1
        else:
            lines = []
            next_dot = 0

def update():
    global timer
    global next_dot
    
    if(next_dot != 10):
        timer += 1 / 60

pgzrun.go()