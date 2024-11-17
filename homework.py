import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

TITLE = 'cat and mouse game: )'

score = 0 
game_over = False

cat = Actor('cat')
cat.pos = 100,100

mouse = Actor('mouse')
mouse.pos = 200,200

def draw():
    screen.blit('bg',(0,0))
    mouse.draw()
    cat.draw()
    screen.draw.text("Score: " + str(score), color='black', topleft=(10,10))\
    
    if game_over:
        screen.fill('blue')
        screen.draw.text("Time is up! Your score is: " + str(score), midtop=(WIDTH/2,10),
        fontsize=40, color='white')
    


def place_mouse():
    mouse.x = randint(70, (WIDTH-70))
    mouse.y = randint(70, (HEIGHT-70))

def time_up():
    global game_over 
    game_over = True

def update():
    if keyboard.left:
        cat.x = cat.x - 2
    if keyboard.right:
        cat.x = cat.x + 2
    if keyboard.up:
        cat.y = cat.y - 2
    if keyboard.down:
        cat.y = cat.y + 2

    mouse_collected = cat.colliderect(mouse)
    global score

    if mouse_collected:
        score = score + 10
        place_mouse()
        

clock.schedule(time_up, 40.0)
      








pgzrun.go()
