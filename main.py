import turtle
import pandas

def get_mouse_click_coor(x, y):
    print(x, y)

screen = turtle.Screen()
screen.title("Vienna District Quiz")
image = "./Maps/vienna_de17.gif"
screen.addshape(image)

turtle.shape(image)

turtle.onscreenclick(get_mouse_click_coor)

screen.mainloop()


