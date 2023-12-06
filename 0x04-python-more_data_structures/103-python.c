#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints info about a Python bytes object
 *
 * @p: Pointer to a Python object (bytes)
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
char *byte_string;
long int byte_size, i, limit;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	byte_size = ((PyVarObject *)(p))->ob_size;
	byte_string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", byte_size);
	printf("  trying string: %s\n", byte_string);

	limit = (byte_size >= 10) ? 10 : (byte_size + 1);

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
	{
		if (byte_string[i] >= 0)
		{
			printf(" %02x", byte_string[i]);
		}
		else
		{
			printf(" %02x", 256 + byte_string[i]);
		}
	}

	printf("\n");
}


/**
 * print_python_list - Prints info about a Python list object
 *
 * @p: Pointer to a Python object (list)
 * Return: void
 */

void print_python_list(PyObject *p)
{
long int list_size, i;
PyListObject *list_obj;
PyObject *list_item;

list_size = ((PyVarObject *)(p))->ob_size;
list_obj = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", list_obj->allocated);

	for (i = 0; i < list_size; i++)
	{
		list_item = ((PyListObject *)p)->ob_item[i];

		printf("Element %ld: %s\n", i, ((list_item)->ob_type)->tp_name);

		if (PyBytes_Check(list_item))
		{
			print_python_bytes(list_item);
		}
	}
}

