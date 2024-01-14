#!/usr/bin/python3
"""
Unitest for base.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import csv
import os


class TestBase(unittest.TestCase):
    def test_id_none(self):
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        b = Base(7)
        self.assertEqual(7, b.id)

    def test_id_zero(self):
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        b = Base(-7)
        self.assertEqual(-7, b.id)

    def test_id_string(self):
        b = Base("Hamilton")
        self.assertEqual("Hamilton", b.id)

    def test_id_list(self):
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_dict(self):
        b = Base({"id": 101})
        self.assertEqual({"id": 101}, b.id)

    def test_id_tuple(self):
        b = Base((7,))
        self.assertEqual((7,), b.id)

    def test_to_json_string(self):
        rectangle = Rectangle(4, 6, 2, 1, 1)
        json_str = Base.to_json_string([rectangle.to_dictionary()])
        self.assertEqual(
                json_str,
                '[{"id": 1, "width": 4, "height": 6, "x": 2, "y": 1}]'
                )

        square = Square(3, 2, 3, 2)
        json_str_square = Base.to_json_string([square.to_dictionary()])
        self.assertEqual(
                json_str_square,
                '[{"id": 2, "size": 3, "x": 2, "y": 3}]'
                )

    def test_from_json_string(self):
        json_str_rect = '[{"id": 1, "width": 4, "height": 6, "x": 2, "y": 1}]'
        instances_rect = [Rectangle(
            **json_dict)
            for json_dict in Base.from_json_string(json_str_rect)]
        self.assertEqual(len(instances_rect), 1)
        self.assertEqual(instances_rect[0].width, 4)

        json_str_square = '[{"id": 2, "size": 3, "x": 2, "y": 3}]'
        instances_square = [Square(**json_dict)
                            for json_dict
                            in Base.from_json_string(json_str_square)]
        self.assertEqual(len(instances_square), 1)
        self.assertEqual(instances_square[0].size, 3)

        """
        def test_save_to_file_csv(self):

        rectangle = Rectangle(4, 6, 2, 1, 1)
        Base.save_to_file_csv([rectangle])
        file_name_rect = "{}.csv".format(Rectangle.__name__)
        self.assertTrue(os.path.isfile(file_name_rect))

        os.remove(file_name_rect)

        square = Square(3, 2, 3, 2)
        Base.save_to_file_csv([square])
        file_name_square = "{}.csv".format(Square.__name__)
        self.assertTrue(os.path.isfile(file_name_square))

        os.remove(file_name_square)
        """

    def test_load_from_file_csv(self):
        file_name_rect = "{}.csv".format(Rectangle.__name__)
        with open(file_name_rect, 'w') as f:
            f.write("1,4,6,2,1\n")

        instances_rect = Rectangle.load_from_file_csv()
        self.assertEqual(len(instances_rect), 1)
        self.assertEqual(instances_rect[0].width, 4)

        os.remove(file_name_rect)

        file_name_square = "{}.csv".format(Square.__name__)
        with open(file_name_square, 'w') as f:
            f.write("2,3,2,3\n")

        instances_square = Square.load_from_file_csv()
        self.assertEqual(len(instances_square), 1)
        self.assertEqual(instances_square[0].size, 3)

        os.remove(file_name_square)


if __name__ == '__main__':
    unittest.main()
