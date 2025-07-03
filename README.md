# despyner = python + designer

## Setup
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
SingletonSplash("SOME_IMAGE_TO_DIAPLAY")
SingletonSplash().message("Loading...")
...
SingletonSplash().message("Something is happening...")
...
SingletonSplash().message("Something else is happening...")
```