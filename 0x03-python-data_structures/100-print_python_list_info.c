#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic information about a Python list.
 * @p: Pointer to a Python list object.
 */

void print_python_list_info(PyObject *p)
{
long int size = PyList_Size(p);
int i;
const char *type_name;
PyListObject *list_object = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);

	printf("[*] Allocated = %li\n", list_object->allocated);

	for (i = 0; i < size; i++)
	{
		type_name = Py_TYPE(list_object->ob_item[i])->tp_name;
		printf("Element %i: %s\n", i, type_name);
	}
}
