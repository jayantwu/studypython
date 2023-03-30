from ctypes import *

so_obj = cdll.LoadLibrary("./libhello.so")

so_obj.say()


