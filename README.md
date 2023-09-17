# Python Virtual Envrionment Program
A very minimal shell-like virtual environment program in Python.
With this program, you are able to use it like a small shell.
You can add external command libraries with your own code and use the program's input commands to use your library.

To create a library, put the library in the folder indicated in config.ini, under library-dir.
Your program requires a `__command__()` function which has a string argument that goes through an if..elif..else pattern, if a command isn't found
`return True`.
(Take an example from the license library in extCmds/license.py)
You will need to register your program name in the file indicated in config.ini, under registry-json, after you have started the program and
executed the input command `creg`.

You are able to edit config.ini,
To change registry-json, add the filename of where the json registry is.
To change library-dir, state the directory where the libraries are held.
(To go deeper into directories, use . to split directory names instead of / or \\.

Thanks for using this program!
