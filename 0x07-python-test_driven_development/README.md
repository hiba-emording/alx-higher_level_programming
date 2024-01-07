## STARTED WITH PYTHON
### PROJECT NUMBER 7

# 0x07. Python - Test-driven development

This directory contains various Python functions designed to perform specific tasks or operations.
Each function has been developed with specific functionalities and edge cases in mind.

## Tests :test_tube:
* tests: Folder of test files.
  * [0-add_integer.txt]
  * [2-matrix_divided.txt]
  * [3-say_my_name.txt]
  * [4-print_square.txt]
  * [5-text_indentation.txt]
  * [6-max_integer_test.py]

## Function Prototypes :floppy_disk:
Prototypes for functions written in this project:

| File                     | Prototype                                    |
| ------------------------ | -------------------------------------------- |
| `0-add_integer.py`       | `def add_integer(a, b=98):`                  |
| `2-matrix_divided.py`    | `def matrix_divided(matrix, div):`           |
| `3-say_my_name.py`       | `def say_my_name(first_name, last_name=""):` |
| `4-print_square.py`      | `def print_square(size):`                    |
| `5-text_indentation.py`  | `def text_indentation(text):`                |


## Tasks :dart:

* **0. Integers addition** :heavy_plus_sign:
  * `0-add_integer.py`: Python function that returns the integer addition of two numbers.
  * If either `a` or `b` is not an `int` or `float`, a `TypeError` is raised.
  * If either `a` or `b` is a `float`, it is casted to an `int` before addition.

* **1. Divide a matrix** :1234:
  * `2-matrix_divided.py`: Python function that divides all elements of a matrix by a common divisor.
  * Returns a new matrix representing the division of all elements of `matrix` by `div`.
  * Quotients are rounded to two decimal places.
  * Handles various error scenarios like non-numeric inputs and zero division.

* **2. Say my name** :speaking_head:
  * `3-say_my_name.py`: Python function that prints a name in a specific format.
  * Raises a `TypeError` for non-string inputs.

* **3. Print square** :black_large_square:
  * `4-print_square.py`: Python function that prints a square using the `#` character.
  * Handles errors for non-integer inputs and negative sizes.

* **4. Text indentation** :scroll:
  * `5-text_indentation.py`: Python function that prints text with indentation.
  * Handles errors for non-string inputs and specific punctuation.

* **5. Max integer - Unittest** :chart_with_upwards_trend:
  * `tests/6-max_integer_test.py`: Python class/script that runs unittests for a specific function.

