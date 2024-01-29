#include <Python.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        fprintf(stderr, ": Argument is not a string\n");
        return;
    }

    Py_ssize_t length = PyUnicode_GetLength(p);
    const Py_UNICODE *unicode = PyUnicode_AsUnicode(p);

    for (Py_ssize_t i = 0; i < length; ++i) {
        if (unicode[i] < 32 || unicode[i] > 126) {
            printf("\\u%04x", unicode[i]);
        } else {
            printf("%c", unicode[i]);
        }
    }

    printf("\n");
}
