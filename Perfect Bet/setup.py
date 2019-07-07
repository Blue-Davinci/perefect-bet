import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = "C:\\Users\\Blue_Davinci\\AppData\\Local\\Programs\\Python\\Python35\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Blue_Davinci\\AppData\\Local\\Programs\\Python\\Python35\\tcl\\tk8.6"
base = None


executables = [Executable("C:\\Users\\Blue_Davinci\\PycharmProjects\\untitled1\\mCheza scraper.py", base=base)]

packages = ['pandas','requests','bs4','idna','numpy']
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "hallo",
    options = options,
    version = "1.0",
    description = '<any description>',
    executables = executables
)
