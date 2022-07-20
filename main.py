import turtle
import pandas

# Screen Configuration
screen = turtle.Screen()
screen.title("Vienna District Quiz")
image = "./Maps/vienna_de15.gif"
screen.addshape(image)
turtle.shape(image)

# CONSTANTS and initial variables
game_on = True

# TODO: Check if guess is among the 23 districts (pandas?)
# TODO: Write correct guesses onto the map (Turtle position on right guess)
# TODO: Use a loop that allows continuous guessing. (While gameOn)
# TODO: Record the correct guesses in a list (create entry, no doubles allowed)
# TODO: Keep track of the score (count the correct entries)

while(game_on):
    answer_district = screen.textinput(title="Rate die Bezirke", prompt="Welche Bezirke gibt es noch?")
    if answer_district is None:
        game_on = False
    else:
        print(answer_district.title())

solution_image = "./Maps/vienna_de17.gif"
screen.addshape(solution_image)
turtle.shape(solution_image)

screen.exitonclick()


