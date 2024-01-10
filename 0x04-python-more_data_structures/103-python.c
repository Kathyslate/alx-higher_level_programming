#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic information about a Python list object
 * @p: A Python list object
 */
void print_python_list(PyObject *p)
{
    PyListObject *list;
    Py_ssize_t i, size;
    int is_list = PyList_Check(p);

    if (!is_list)
    {
        printf("Error: [<%s>] is not a Python list\n", Py_TYPE(p)->tp_name);
        return;
    }

    list = (PyListObject *)p;
    size = Py_SIZE(list);

    printf("[*] Python list object %p with %ld items:\n", list, size);
    for (i = 0; i < size; i++)
    {
        printf("Element %ld: ", i);
        if (PyLong_Check(list->ob_item[i]))
            printf("%ld\n", PyLong_AsLong(list->ob_item[i]));
        else
            printf("<not an integer>\n");
    }
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object
 * @p: A Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes;
    Py_ssize_t size, i;
    int is_bytes = PyBytes_Check(p);

    if (!is_bytes)
    {
        printf("Error: [<%s>] is not a Python bytes object\n", Py_TYPE(p)->tp_name);
        return;
    }

    bytes = (PyBytesObject *)p;
    size = bytes->ob_size;

    printf("[*] Python bytes object %p with %ld bytes:\n", bytes, size);
    printf("  first 10 bytes: ");
    for (i = 0; i < 10 && i < size; i++)
        printf("%02x ", bytes->ob_sval[i]);
    if (size > 10)
        printf("...");
    printf("\n");
}
