import sys,os

# get current path
pythonbox_path = os.path.dirname(__file__)
customs_path = pythonbox_path + r"\customs"
packages_path = pythonbox_path + r"\packages"

# add path to python sys path
sys.path.append(customs_path)
sys.path.append(packages_path)
print("Modify PYTHONPATH...")

# read pythonbox.ini and add to environment path
if(os.path.exists("pythonbox.ini")):
    f = open("pythonbox.ini", "r")
    raw_lines = f.read()
    f.close()
    raw_lines = raw_lines.replace("\r", "")
    raw_lines = raw_lines.rstrip("\n ")
    raw_lines = raw_lines.split("\n")
    os_path_splitted = os.environ["PATH"].split(";")
    reading_path = False
    for line in raw_lines:
        if (len(line) == 0 or line[0] == "*"):
            continue
        if (len(line) == 0 or line[0] == "["):
            if reading_path: 
                break
            if line == "[System environment path]":
                reading_path = True
                continue
        if reading_path:
            path_splitted = line.split("\\")
            if path_splitted[0] == ".":
                path_splitted[0] = pythonbox_path
                line = "\\".join(path_splitted)
            os_path_splitted.append(line)
    os.environ["PATH"] = ";".join(os_path_splitted)
    print("Modify system environment PATH")
else:
    print("File: pythonbox.ini not found, system environment PATH will not be modified.")
