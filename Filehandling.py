import os

if os.path.exists("E:/programming/PythonProgramming/test_file.txt"):
    f = open("E:/programming/PythonProgramming/test_file.txt", "r")
    print(f.read())
else:
    print("file not foumd")


