import turtle
import pandas

screen = turtle.Screen()
screen.title("Vienna District Quiz")
image = "./Maps/vienna_de17.gif"
screen.addshape(image)
turtle.shape(image)

# TODO: Convert the guess to Title-Case
# TODO: Check if guess is among the 23 districts
# TODO: Write correct guesses onto the map
# TODO: Use a loop that allows continuous guessing.
# TODO: Record the correct guesses in a list
# TODO: Keep track of the score


answer_district = screen.textinput(title="Rate die Bezirke", prompt="Welche Bezirke gibt es noch?")
print(answer_district)
screen.mainloop()


