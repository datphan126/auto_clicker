# Auto Clicker
This software allows you to select coordinates on your screen and perform repetitive mouse click at those coordinates.

**Installation:**
Install Python 2+
Set Python as the application to open python files (i.e. files ending with .py)
Run auto_clicker.py

**Usages:**
Press "r" key to start recording coordinates. Each time you click on a position, the coordinates of that position is shown on the terminal.
Press "r" key again to stop coordinates recording mode
Press "c" key to choose to use the coordinates you have selected
Press "s" key to start automatic mouse clicks
If you want to stop, press "s" key again
If you want to exit, press "e" key
If you want to save the coordinates, open the python script and add the coordinates to the mode section on the top. For example, if you want to assign coordinates "1288, 608" and "1138, 594" to F1 key, simply modify the element associated with the key: **"Key.f1": [[1288, 608], [1138, 594]]**
