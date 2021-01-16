# What is pythonbox?
Self contained environment that manage dependencies and path for python.
System environment PATH will also be modified with the path in pythonbox.ini

# Requirement
- Python 3+
- PIP

# How to use?

Add package name to install in pythonbox.ini, I added pyperclip package there just to be an example

Then run package_controller.py to install packages.

If there is any file that need to be in system environment PATH

Add them to [System environment path] section located within pythonbox.ini
