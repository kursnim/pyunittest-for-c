from cffi import FFI
ffibuilder = FFI()
ffibuilder.set_source("py_HelloWorld",'#include <stdio.h>')
ffibuilder.cdef("int printf(const char *format, ...);")
ffibuilder.compile()

from py_HelloWorld.lib import printf
printf(b"Hello, world!\n")