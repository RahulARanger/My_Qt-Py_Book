We use pyuic5 commands to convert ui to the python code.

# Some Important Points

### * Try to modify the variable names of the widgets while creating them in the designer or creator.

### * Some useful commands:
        * pyuic5
        * pyuic5 --help for more useful commands
        * pyuic5 -p (path for the ui file) to preview the ui 
        * pyuic5 -d -p (path for the ui file) previews and prints the debug info it's execution
        * pyuic5 -x -o (path for the new.py file) (path for the .ui file) converts the ui file to the .py file and makes it executabl
        * pyuic5 --version for displaying the version of the pyuic5

### *  Don't modify the ui file so generated try to inherit that object. we may use that file again.

