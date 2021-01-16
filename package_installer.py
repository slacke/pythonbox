import os

all_packages = []
pythonbox_path = ""

def read_pythonbox_file():
    if(os.path.exists("pythonbox.ini")):
        f = open("pythonbox.ini", "r")
        raw_lines = f.read()
        raw_file = raw_lines
        f.close()
        raw_lines = raw_lines.replace("\r", "")
        raw_lines = raw_lines.rstrip("\n ")
        raw_lines = raw_lines.split("\n")
        reading_package = False
        for line in raw_lines:
            if (len(line) == 0 or line[0] == "*"):
                continue
            if (len(line) == 0 or line[0] == "["):
                if reading_package:
                    break
                if line == "[Package]":
                    reading_package = True
                    continue
            if reading_package:
                line = line.strip(" ")
                all_packages.append(line)

def install_package(package_name):
    command = r"pip install --upgrade --target={0} {1}".format(pythonbox_path, package_name)
    os.system(command)

if __name__ == "__main__": 
    pythonbox_path = os.path.join(os.path.dirname(__file__), "outsource_lib")
    if not os.path.exists(pythonbox_path):
        os.mkdir(pythonbox_path)
    read_pythonbox_file()
    if all_packages:
        for package_name in all_packages:
            install_package(package_name)
    else:
        print("There is no package to install, Add your package in pythonbox.ini")
    os.system("pause")