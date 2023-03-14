# # check os
# from sys import platform
# if platform == "linux" or platform == "linux2":
#     # linux
#     print ("Linux")
# elif platform == "darwin":
#     # OS X
#     print ("MacOS")
# elif platform == "win32":
#     # Windows...
#     print ("Windows")
# 
# import psutil
# print(psutil.disk_usage(".").free)
import os
from os import path
from shutil import disk_usage

print([i / 1000000 for i in disk_usage(path.realpath('/'))])
print()