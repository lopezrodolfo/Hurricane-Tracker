"""
Module: hurricane_tracker

Program to visualize the path of a Hurrican in the North Atlantic Basin.

Author:
1) Rodolfo Lopez (rodolfolopez@sandiego.edu)
"""

import turtle


def screen_setup():
    """
    Creates the Turtle and the Screen with the map background
    and coordinate system set to match latitude and longitude.

    Returns:
    A tuple containing the Turtle and the Screen

    DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """

    import tkinter

    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Tracker")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(
        -90, 0, -17.66, 45
    )  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("hurricane.gif")
    t.shape("hurricane.gif")

    return [t, wn, map_bg_img]


def get_category(wind_speed):
    if wind_speed < 74:
        return 0
    elif wind_speed < 96:
        return 1
    elif wind_speed < 111:
        return 2
    elif wind_speed < 130:
        return 3
    elif wind_speed < 157:
        return 4
    else:
        return 5


def get_color(category):
    if category == 0:
        return "white"
    elif category == 1:
        return "blue"
    elif category == 2:
        return "green"
    elif category == 3:
        return "yellow"
    elif category == 4:
        return "orange"
    elif category == 5:
        return "red"


def animate(filename):
    """
    Animates the path of a hurricane.

    Parameters:
    csv_filename (string): Name of file containing hurricane data (CSV format).
    """

    # screen_setup returns a list of three items: the turtle to draw with, the
    # screen object for the window, and the background image of the window.
    # We only care about the turtle though.

    setup_data = screen_setup()
    hurricane_turtle = setup_data[0]

    with open(filename, "r", encoding="utf-8") as data_file:
        hurricane_turtle.up()
        hurricane_turtle.hideturtle()
        hurricane_turtle.goto(0, 0)
        hurricane_turtle.color("red", "red")

        for line in data_file:
            data = line.split(",")
            latitude = float(data[2])
            longitude = float(data[3])
            wind_speed = float(data[4])
            category = get_category(wind_speed)
            color = get_color(category)

            if category > 0:
                hurricane_turtle.write(str(category))

            hurricane_turtle.pensize(1 * (category + 1))
            hurricane_turtle.color(color, color)

            hurricane_turtle.goto(longitude, latitude)
            hurricane_turtle.down()
            hurricane_turtle.showturtle()

        turtle.done()


if __name__ == "__main__":
    filename = input("Enter the name of the hurricane data file: ")
    animate(filename)
