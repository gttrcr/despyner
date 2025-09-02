# despyner = python + designer

## Setup despyner
If you want to use this repo in your amazing and transcendental python project you only need to complete the following tasks:

1. Execute `pip3 install pyside6`
Yes, it is just one simple `pip3` command

## Code structure
If you want to be compliant with *my very personal and arbitrary* choice of project structure, these are the guidelines I suggest.

1. Use `pyside6-designer` to make `*.ui` files with user interface, popups and screens
2. Use `dn` to convert a `*.ui` file in a `*.py` file based on pyside6
3. Put every `*.ui` file in the `ui` folder (`dn` will create corresponding `*.py` files in the same folder)
4. Put every ux `*.py` file in the `ux` folder connected to the corresponding `ui/*.py` file
5. Use `globals.py` file to declare every global variable
6. Use `single_include.py` file to store the entire list of libraries, packages, imports you will need
7. Use `SingletonSplash` to make the wait while the program loads more pleasant:
```py
SingletonSplash("SOME_IMAGE_TO_DISPLAY")
SingletonSplash().message("Loading...")
...
SingletonSplash().message("Something is happening...")
...
SingletonSplash().message("Something else is happening...")
```

### example of main.py file
```python
import sys

sys.dont_write_bytecode = True

from os import path
from PySide6.QtWidgets import QApplication
from despyner.SingletonSplash import SingletonSplash


def abs_path(filename, ref_position=__file__):
    return path.abspath(path.join(path.dirname(ref_position), filename))


app = QApplication(sys.argv)
SingletonSplash(abs_path("SOME_IMAGE_TO_DISPLAY", __file__))
SingletonSplash().message("Loading...")

import Config
from despyner.QtMger import WindowManager

# in this example the main window is named Dashboard

# the ui is ui/Dashboard.py (generated from ui/dashboard.ui and dn)
from ui.Dashboard import Ui_Dialog

# the ux is ux/Dashboard.py
from ux.Dashboard import Dashboard

if __name__ == "__main__":
    SingletonSplash().message("Starting...")
    Config.Config("config.json") # this is optional
    c = Config.Config().config # this is optional
    win = WindowManager(Ui_Dialog, Dashboard, c)
    win.show()
    SingletonSplash().close()
    sys.exit(app.exec())
```

### example of `ux.Dashboard.py`
```python
import globals
from single_include import Qt
from despyner.QtMger import get_icon, i_name


class Dashboard:
    def __init__(self, ui, dialog, args=None):
        self.ui = ui
        self.dialog = dialog
        self.args = args
        
        self.dialog.setWindowState(Qt.WindowMaximized)
        self.ui.tabWidget.setTabIcon(0, get_icon(i_name.WAVES, globals.theme))
        self.ui.tabWidget.setTabIcon(1, get_icon(i_name.NOTE_STACK, globals.theme))
```

## `build.sh`
It is a tool to build an executable application using `PyInstaller`. Consider you are inside your project folder and despyner is a submodule of your project.
```bash
python3 despyner/build.py main.py --name EXECUTABLE_NAME --onedir --windowed --add-data ../SOURCE_FILE:DESTINATION_FILE --add-data ../SOURCE_FOLDER:DESTINATION_FOLDER
```
Note that when you use `add-data`, `PyInstaller` is, by default, in the `build` folder. Then, you have to use `../` to move from `build` to a higher level. You can add source file or folder and you can call `add-data` as many times as you want.

## `dn.py`
It is a very useful tool that listens for any changes to any `.ui` file located in any folder or subfolder above the level at which `dn.py` is run.