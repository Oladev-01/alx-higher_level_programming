#include <Python.h>
/**
 * print_python_list - this function prints info about python list
 * @p: this is the pointer to the object lists
 * Return: void
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t num, i;
	PyObject *ptr;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid Python List\n");
		return;
	}
	num = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", num);
	for (i = 0; i < num; i++)
	{
		ptr = PyList_GetItem(p, i);
		printf("Elemen %ld: %s\n", i, Py_TYPE(ptr)->tp_name);
	}
}

/**
 * print_python_bytes - this function checks the bytes of an object list
 * @p: the pointer to an item of the list
 * Return; void
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: ");
	for (Py_ssize_t j = 0; j < 10 && j < PyBytes_Size(p); ++j)
	{
		printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[j]);
	}
	printf("\n");
}
