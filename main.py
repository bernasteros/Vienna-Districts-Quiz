import turtle
import pandas as pd

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

# import districts from csv-file and put them into a data list
# in the same time an empty list should be created for guessing.
df = pd.read_csv('Data/district_names.csv')
data = df.values.tolist()

# convert the raw list into a dictionary with districtname + coordinates
district_dict = {}
for district in data:
    name = district[1]
    coords = [district[2], district[3]]
    district_dict[name] = coords

# Todo: Check if guess is among the 23 districts

while (game_on):
    answer_district = screen.textinput(title="Rate die Bezirke", prompt="Bitte gib einen Bezirk ein!")
    if answer_district == "":
        game_on = False
    elif answer_district in district_dict:
        # Create a turtle object
        t = turtle.Turtle()
        # Hide the turtle
        t.ht()
        # Lift the pen up
        t.penup()

        # Move the turtle to the desired position
        x = district_dict[answer_district][0]
        y = district_dict[answer_district][1]
        t.goto(x, y)

        # Put the pen back down
        t.pendown()

        # Write the text at the turtle's position
        text = answer_district
        t.write(text, align="center", font=("Arial", 8, "normal"))

    else:
        print(answer_district.title())

# TODO: Record the correct guesses in a list (create entry, no doubles allowed)
# TODO: Keep track of the score (count the correct entries)


# Show map with solution
show_picture(picture_path="./Maps/vienna_de17.gif")

screen.exitonclick()
