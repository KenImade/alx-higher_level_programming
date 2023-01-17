#!/usr/bin/python3
"""
This module defines the Base class
"""
import json
import turtle


class Base:
    """Represent the base model

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization of Base class

        Args:
            id (int, optional): object id. Default is None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.

        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(10, 10)
            elif cls.__name__ == "Square":
                new = cls(10)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv file"""
        filename = cls.__name__ + ".csv"
        content = ""
        text = []
        if list_objs is not None:
            content += ','.join(list_objs[0].to_dictionary().keys())
            content += '\n'
            for lst in list_objs:
                content += ','.join(
                        map(str, lst.to_dictionary.values())
                )
                content += '\n'
        with open(filename, mode='w', encoding='utf-8') as f:
            return f.write(content)

    @classmethod
    def load_from_file_csv(cls):
        """load from csv"""
        filename = cls.__name__ + ".csv"
        object_created = []

        with open(filename, 'r') as f:
            header = f.readline().replace('\n', '').split(',')
            for el in f.readlines():
                values = map(int, el.replace('\n', '').split(','))
                data = dict(zip(header, values))
                object_created.append(cls.create(**data))
        return object_created

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """draw the figure"""
        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares

        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
