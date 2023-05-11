import turtle
import pandas as pd


def show_picture(picture_path):
    """
    Diese Funktion zeigt ein beliebiges Bild auf Turtles.
    Parameter ist entsprechend der Pfad dorthin.
    """
    screen.addshape(picture_path)
    turtle.shape(picture_path)


def write_district(dict_entry, answer):
    """
    Aus einer Bezirks oder Ortsliste im CSV-Format wird ein Dictionary gebastelt.
    :param dict_entry:
    :param answer:
    :return:
    """
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
answers = []
district_dict = create_dict('Data/district_names.csv')

while (game_on):
    answer_district = screen.textinput(title="Rate die Bezirke", prompt=f"Bitte gib einen Bezirk ein!"
                                                                        f"\nNoch {23 - len(answers)} übrig.")
    if answer_district == "":
        game_on = False
    elif answer_district in district_dict:
        if answer_district in answers:
            print("Oh nein, das hatten wir ja schon!")
            continue

        # Insert the right guess onto the map
        write_district(district_dict, answer_district)

        # Put the right answer into a separate list for reference
        answers.append(answer_district)
    else:
        print(answer_district.title())

# Show map with solution
show_picture(picture_path="./Maps/vienna_de17.gif")

screen.exitonclick()
