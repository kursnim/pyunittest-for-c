from cffi import FFI
ffibuilder = FFI()
ffibuilder.cdef("int func_sum(int a, int b);")
ffibuilder.set_source("py_sum",'#include "sum_file_h.h"',sources=["sum_file_c.c"])
ffibuilder.compile()