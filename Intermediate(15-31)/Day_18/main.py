import colorgram
from random import choice
import turtle as t
from typing import Tuple


def init_turtle() -> t.Turtle:
    jimmy = t.Turtle()
    jimmy.shape("classic")
    jimmy.speed("fastest")
    t.colormode(255)
    jimmy.up()
    jimmy.goto(-200, -170)
    return jimmy


def create_spot_painting(colors_rgb, jimmy, size: Tuple[int, int] = (10, 10)):
    rows, columns = size
    for _ in range(rows):
        row_start = jimmy.position()
        for _ in range(columns):
            jimmy.dot(20, (choice(colors_rgb)))
            jimmy.up()
            jimmy.forward(50)
            jimmy.down()
        jimmy.up()
        jimmy.goto(row_start[0], row_start[1] + 50)


def main(colors_rgb, init_turtle, size: Tuple[int, int] = (10, 10)):
    jimmy = init_turtle
    create_spot_painting(colors_rgb, jimmy, size)
    screen = t.Screen()
    screen.exitonclick()


if __name__ == "__main__":
    colors = colorgram.extract("Intermediate(15-31)/Day_18/image.jpg", 255)
    colors_rgb = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors][3:]
    # colors_rgb: List[Tuple[int, int, int]] = [(224, 233, 227),(207, 160, 82),(54, 88, 130),(145, 91, 40),(140, 26, 49),(221, 207, 105),(132, 177, 203),(158, 46, 83),(45, 55, 104),(169, 160, 39),(129, 189, 143),(83, 20, 44),(37, 43, 67),(186, 94, 107),(187, 140, 170),(85, 120, 180),(59, 39, 31),(88, 157, 92),(78, 153, 165),(194, 79, 73),(45, 74, 78),(80, 74, 44),(161, 201, 218),(57, 125, 121),(219, 175, 187),(169, 206, 172),(219, 182, 169),(179, 188, 212),(48, 74, 73),(147, 37, 35),(43, 62, 61),]

    main(colors_rgb, init_turtle(), (15, 15))
