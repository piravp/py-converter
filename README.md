# Python 3.5 translator
This is a simple script that make python 2.7 runnable with python 3.5.


### Basic Idea
The most common and time consuming problem is adding brackets to the print statements. 
This script runs through your .py file and replaces all ```print "Hello, Word!"``` with ```print ("Hello, World!")``` in less than a second. 

### Using it
The script can be ran within the terminal, or using a simple (and I mean *reeeally* simple) user interface. 


### Todos

Listed after priority.

* Make it runnable without need to download anything else
* Replace keywords such as ```xrange``` > ```range```.
* User should be able to choose which directory to write to.
* Checkbox that lets user choose if comments should be translated. 
* Make UI better with for instance [PyQt](https://en.wikipedia.org/wiki/PyQt). 
* ```print```, without ```" "``` causes the program to crash - should be fixed. 

## Changes
To see a more detailed description of what has changed in Python 3.5, please visit:
https://docs.python.org/3/whatsnew/3.5.html

----------------------