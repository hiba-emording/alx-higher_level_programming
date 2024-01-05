## STARTED WITH PYTHON
### PROJECT NUMBER 9

# 0x09. Python - Everything is object

This directory contains tasks focused on understanding the concept of objects in Python, exploring memory allocation, object comparison, object mutability, and more.

## Tasks

| Task Number | File Name(s)                                     | Task Description |
|-------------|--------------------------------------------------|------------------|
| 0           | 0-answer.txt                                    | What function would you use to print the type of an object? |
| 1           | 1-answer.txt                                    | How do you get a variable's identifier (which is the memory address in the CPython implementation)? |
| 2           | 2-answer.txt                                    | In the following code, do `a` and `b` point to the same object? <br> ``` >>> a = 89 >>> b = 100 ``` |
| 3           | 3-answer.txt                                    | In the following code, do `a` and `b` point to the same object? <br> ``` >>> a = 89 >>> b = 89 ``` |
| 4           | 4-answer.txt                                    | In the following code, do `a` and `b` point to the same object? <br> ``` >>> a = 89 >>> b = a ``` |
| 5           | 5-answer.txt                                    | In the following code, do `a` and `b` point to the same object? <br> ``` >>> a = 89 >>> b = a + 1 ``` |
| 6           | 6-answer.txt                                    | What do these 3 lines print? <br> ``` >>> s1 = "Best School" >>> s2 = s1 >>> print(s1 == s2) ``` |
| 7           | 7-answer.txt                                    | What do these 3 lines print? <br> ``` >>> s1 = "Best" >>> s2 = s1 >>> print(s1 is s2) ``` |
| 8           | 8-answer.txt                                    | What do these 3 lines print? <br> ``` >>> s1 = "Best School" >>> s2 = "Best School" >>> print(s1 == s2) ``` |
| 9           | 9-answer.txt                                    | What do these 3 lines print? <br> ``` >>> s1 = "Best School" >>> s2 = "Best School" >>> print(s1 is s2) ``` |
| 10          | 10-answer.txt                                   | What do these 3 lines print? <br> ``` >>> l1 = [1, 2, 3] >>> l2 = [1, 2, 3] >>> print(l1 == l2) ``` |
| 11          | 11-answer.txt                                   | What do these 3 lines print? <br> ``` >>> l1 = [1, 2, 3] >>> l2 = [1, 2, 3] >>> print(l1 is l2) ``` |
| 12          | 12-answer.txt                                   | What do these 3 lines print? <br> ``` >>> l1 = [1, 2, 3] >>> l2 = l1 >>> print(l1 == l2) ``` |
| 13          | 13-answer.txt                                   | What do these 3 lines print? <br> ``` >>> l1 = [1, 2, 3] >>> l2 = l1 >>> print(l1 is l2) ``` |
| 14          | 14-answer.txt                                   | What does this script print? <br> ``` l1 = [1, 2, 3] l2 = l1 l1.append(4) print(l2) ``` |
| 15          | 15-answer.txt                                   | What does this script print? <br> ``` l1 = [1, 2, 3] l2 = l1 l1 = l1 + [4] print(l2) ``` |
| 16          | 16-answer.txt                                   | What does this script print? <br> ``` def increment(n): n += 1 a = 1 increment(a) print(a) ``` |
| 17          | 17-answer.txt                                   | What does this script print? <br> ``` def increment(n): n.append(4) l = [1, 2, 3] increment(l) print(l) ``` |
| 18          | 18-answer.txt                                   | What does this script print? <br> ``` def assign_value(n, v): n = v l1 = [1, 2, 3] l2 = [4, 5, 6] assign_value(l1, l2) print(l1) ``` |
| 19          | 19-copy_list.py                                 | Python function `def copy_list(l):` that returns a copy of a list. |
| 20          | 20-answer.txt                                   | Is `a` a tuple? <br> ``` a = () ``` |
| 21          | 21-answer.txt                                   | Is `a` a tuple? <br> ``` a = (1, 2) ``` |
| 22          | 22-answer.txt                                   | Is `a` a tuple? <br> ``` a = (1) ``` |
| 23          | 23-answer.txt                                   | Is `a` a tuple? <br> ``` a = (1, ) ``` |
| 24          | 24-answer.txt                                   | What does this script print? <br> ``` a = (1) b = (1) a is b ``` |
| 25          | 25-answer.txt                                   | What does this script print? <br> ``` a = (1, 2) b = (1, 2) a is b ``` |
| 26          | 26-answer.txt                                   | What does this script print? <br> ``` a = () b = () a is b ``` |
| 27          | 27-answer.txt                                   | Will the last line of this script print `139926795932424`? <br> ``` >>> id(a) 139926795932424 >>> a [1, 2, 3, 4] >>> a = a + [5] >>> id(a) ``` |
| 28          | 28-answer.txt                                   | Will the last line of this script print `139926795932424`? <br> ``` >>> a [1, 2, 3] >>> id (a) 139926795932424 >>> a += [4] >>> id(a) ``` |
| 29          | 100-magic_string.py                             | Python function `magic_string()` that returns the string `"BestSchool"` n times the number of iteration. |
| 30          | 101-locked_class.py                             | Python class `LockedClass` with no attributes that prevents the user from dynamically creating any new instance attributes not called `first_name`. |
| 31          | 103-line1.txt<br>102-line2.txt                  | How many `int` objects are created by the execution of the first line in this script? |
| 32          | 104-line1.txt<br>104-line2.txt<br>104-line3.txt<br>104-line4.txt<br>104-line5.txt | How many `int` objects are created by the execution of the second line in this script? <br> After the execution of line 3, is the `int` object pointed to by `a` deleted? <br> After the execution of line 4, is the `int` object pointed to by `b` deleted? <br> How many `int` objects are created by the execution of the last line in this script? |
| 33          | 105-line1.txt                                   | Before the execution of line 2 in this script, how many `int` objects have been created and are still in memory? |
| 34          | 106-line1.txt<br>106-line2.txt<br>106-line3.txt<br>106-line4.txt<br>106-line5.txt | How many `str` objects are created by the execution of the first line in this script? <br> How many `str` objects are created by the execution of the second line in this script? <br> After the execution of line 3, is the `str` object pointed to by `a` deleted? <br> After the execution of line 4, is the `str` object pointed to by `b` deleted? <br> How many `str` objects are created by the execution of the last line in this script? |

