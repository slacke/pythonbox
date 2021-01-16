# Pythonbox

Self contained environment that manage dependencies and path for python.

## Getting Started

1. Clone this project
2. run **package_installer.py** with python
3. Add your code to main.py

### Prerequisites

- Python 3+
- pip for Python

### How to use?

1. Add package name to install in **pythonbox.ini**, I added pyperclip package there just to be an example

2. Run **package_controller.py** to install packages.

The package will install within **outsource_lib** folder and would be add to python path with any code that import pythonbox

If there is any file that need to be in system environment PATH

Add them to [System environment path] section located within pythonbox.ini

## Authors

[me](https://github.com/slacke)

## License

This project is licensed under the MIT License

