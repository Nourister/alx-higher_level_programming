#!/usr/bin/python3

"""Defines a base class model"""
import json
import turtle
import csv

class Base:
    """
    Base class.
    """
    # private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Parameters:
        - id (int): Identifier for an instance. Default is None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

# ... other methods and attributes ...

@staticmethod

def to_json_string(list_dictionaries):
    """Return the JSON serialization of a list of dicts or an empty list if input is None or empty."""
    return json.dumps(list_dictionaries) if list_dictionaries else "[]"

@classmethod
def save_to_file(cls, list_objs):
    """Write the JSON serialization of a list of objects to a file."""

    filename = f"{cls.__name__}.json"
    list_dicts = [o.to_dictionary() for o in list_objs] if list_objs else []

    with open(filename, "w") as jsonfile:
        jsonfile.write(Base.to_json_string(list_dicts))


@classmethod
def load_from_file(cls):
    """Return a list of classes instantiated from a file of JSON strings."""

    filename = f"{cls.__name__}.json"
    try:
        with open(filename, "r") as jsonfile:
            list_dicts = Base.from_json_string(jsonfile.read())
        return [cls.create(**d) for d in list_dicts]
    except (IOError, FileNotFoundError):
        return []



@classmethod
def save_to_file_csv(cls, list_objs):
    """Write the CSV serialization of a list of objects to a file."""

    filename = f"{cls.__name__}.csv"
    fieldnames = ["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]

    with open(filename, "w", newline="") as csvfile:
        if not list_objs:
            csvfile.write("[]")
        else:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())


@classmethod
def load_from_file_csv(cls):
    """Return a list of classes instantiated from a CSV file."""

    filename = f"{cls.__name__}.csv"
    fieldnames = ["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]

    try:
        with open(filename, "r", newline="") as csvfile:
            list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
            formatted_dicts = [dict([k, int(v)] for k, v in d.items()) for d in list_dicts]
        return [cls.create(**d) for d in formatted_dicts]
    except (IOError, FileNotFoundError):
        return []


@staticmethod
def draw(list_rectangles, list_squares):
    """Draw Rectangles and Squares using the turtle module."""

    def draw_shape(turt, shape, color):
        """Helper function to draw a single shape."""
        turt.color(color)
        turt.showturtle()
        turt.up()
        turt.goto(shape.x, shape.y)
        turt.down()
        for _ in range(2):
            turt.forward(shape.width)
            turt.left(90)
            turt.forward(shape.height if hasattr(shape, 'height') else shape.width)
            turt.left(90)
        turt.hideturtle()

    turt = turtle.Turtle()
    turt.screen.bgcolor("#b7312c")
    turt.pensize(3)
    turt.shape("turtle")

    for rect in list_rectangles:
        draw_shape(turt, rect, "#ffffff")

    for sq in list_squares:
        draw_shape(turt, sq, "#b5e3d8")

    turtle.exitonclick()
