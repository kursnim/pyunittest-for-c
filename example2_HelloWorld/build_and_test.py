from cffi import FFI
ffibuilder = FFI()
ffibuilder.set_source("py_HelloWorld",'#include <stdio.h>')
ffibuilder.cdef("int printf(const char *format, ...);")
ffibuilder.compile()

from py_HelloWorld import ffi
lib = ffi.dlopen()

#import ctypes.util         # or, try this on Windows:
#lib = ffi.dlopen(ctypes.util.find_library("c"))

number = 123

lib.printf(b"Hello, world!\n")
lib.printf(b"int : %d\n", ffi.cast('int', number))
