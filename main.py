import turtle
import pandas as pd

def show_picture(picture_path):
    screen.addshape(picture_path)
    turtle.shape(picture_path)
def write_district(dict_entry, answer):
    # Create a turtle object
    t = turtle.Turtle()
    # Hide the turtle
    t.ht()
    # Lift the pen up
    t.penup()

    # Move the turtle to the desired position
    x = dict_entry[answer][0]
    y = dict_entry[answer][1]
    t.goto(x, y)

    # Put the pen back down
    t.pendown()

    # Write the text at the turtle's position
    text = answer
    t.write(text, align="center", font=("Arial", 8, "normal"))
def create_dict(path):
    # import districts from csv-file and put them into a data list
    # in the same time an empty list should be created for guessing.
    df = pd.read_csv(path)
    data = df.values.tolist()

    # convert the raw list into a dictionary with districtname + coordinates
    dict = {}
    for info in data:
        name = info[1]
        coords = [info[2], info[3]]
        dict[name] = coords
    return dict
# Screen Configuration
screen = turtle.Screen()
screen.title("Vienna District Quiz")

# Show blank map
show_picture(picture_path="./Maps/vienna_de15.gif")

# CONSTANTS and initial variables
game_on = True

district_dict = create_dict('Data/district_names.csv')

while (game_on):
    answer_district = screen.textinput(title="Rate die Bezirke", prompt="Bitte gib einen Bezirk ein!")
    if answer_district == "":
        game_on = False
    elif answer_district in district_dict:
        # Todo: Check if guess is among the 23 districts

        # Insert the right guess onto the map
        write_district(district_dict, answer_district)

    else:
        print(answer_district.title())

# TODO: Record the correct guesses in a list (create entry, no doubles allowed)
# TODO: Keep track of the score (count the correct entries)


# Show map with solution
show_picture(picture_path="./Maps/vienna_de17.gif")

screen.exitonclick()
