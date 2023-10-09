#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - a C function that prints some basic
 *	info about Python lists.
 *@p: a type which contains the information about all Python objects
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *list_obj = (PyListObject *) p;

	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", list_obj->allocated);

	for (i = 0; i < size; i++)
		printf("Element %d: %s\n", i, Py_TYPE(list_obj->ob_item[i])->tp_name);
}
