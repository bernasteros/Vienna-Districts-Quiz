import turtle
import pandas


def show_picture(picture_path):
    screen.addshape(picture_path)
    turtle.shape(picture_path)


# Screen Configuration
screen = turtle.Screen()
screen.title("Vienna District Quiz")

# Show blank map
show_picture(picture_path="./Maps/vienna_de15.gif")

# CONSTANTS and initial variables
game_on = True

# TODO: Check if guess is among the 23 districts (pandas?)
# TODO: Write correct guesses onto the map (Turtle position on right guess)
# TODO: Use a loop that allows continuous guessing. (While gameOn)
# TODO: Record the correct guesses in a list (create entry, no doubles allowed)
# TODO: Keep track of the score (count the correct entries)

while (game_on):
    answer_district = screen.textinput(title="Rate die Bezirke", prompt="Welche Bezirke gibt es noch?")
    if answer_district is None:
        game_on = False
    else:
        print(answer_district.title())

# Show map with solution
show_picture(picture_path="./Maps/vienna_de17.gif")

screen.exitonclick()
