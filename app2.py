import pyxel
import time

pyxel.init(30,30,fps = 10)

fruit = [pyxel.rndi(0,29), pyxel.rndi(0,29)]

arrow_keys = [pyxel.KEY_UP, pyxel.KEY_DOWN, pyxel.KEY_LEFT, pyxel.KEY_RIGHT]

snake_geometry = [[10, 15],[11, 15],[12, 15]]

snake_direction = [1,0]

def update():   #il faut toujours avoir un update mais on peut mettre "pass" si on veut qu'elle ne fasse rien
    global snake_geometry, snake_direction, fruit
    if pyxel.btnp(pyxel.KEY_Q): # btnp = button press
        pyxel.quit()    # si on appuie sur Q le programme s'arrête
    arrow_keys_pressed = []
    for key in arrow_keys :
        if pyxel.btnp(key):
            arrow_keys_pressed.append(key)
    for key in arrow_keys_pressed :
        if key == pyxel.KEY_UP :
            snake_direction = [0,-1]
            print("↑")
        elif key == pyxel.KEY_DOWN:
            snake_direction = [0,1]
            print("↓")
        elif key == pyxel.KEY_LEFT:
            snake_direction = [-1,0]
            print("←")
        elif key == pyxel.KEY_RIGHT:
            snake_direction = [1,0]
            print("→")
    snake_head = snake_geometry[-1]
    new_snake_head = [snake_head[0] + snake_direction[0]
                      , snake_head[-1] + snake_direction[-1]]
    if new_snake_head == fruit :
        snake_geometry = snake_geometry + [new_snake_head]
        fruit = [pyxel.rndi(0,29), pyxel.rndi(0,29)]
    else :
        snake_geometry = snake_geometry[1:] + [new_snake_head]    

    # for k in range (len(snake_geometry)-1) :
    #     snake_geometry[k] = snake_geometry[k+1]
    #     snake_geometry[-1] = new_snake_head

    # if snake_head == fruit :
    #     snake_geometry = [fruit] + snake_geometry
    #     fruit = [pyxel.rndi(0,29), pyxel.rndi(0,29)]


# # t = 0.0

# # # def draw():
# # #     global t
# # #     t_new = time.time()
# # #     dt = t_new - t
# # #     t = t_new
# # #     fps = 1.0 / dt
# # #     fps = int(round(fps))
# # #     pyxel.cls(0)
# # #     color = pyxel.frame_count % 16
# # #     pyxel.text(56, 54, "Hello, Snake!", color)
# # #     pyxel.text(0, 0, f"fps: {fps}", 7)

# # # pyxel.init(160, 120)
# # # pyxel.run(update, draw)


def draw():
    pyxel.cls(13)
    for i in range(30):
        for j in range(30):
            if (i+j) % 2 == 0:
                pyxel.pset(i, j, 7)
    pyxel.pset(fruit[0], fruit[1], 8)
    for i in range (len(snake_geometry)-1):
        pyxel.pset(snake_geometry[i][0],snake_geometry[i][1], 3)
    pyxel.pset(snake_geometry[-1][0],snake_geometry[-1][-1], 11)

pyxel.run(update, draw)
