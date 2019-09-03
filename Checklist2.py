"""checklist = list()

    # CREATE
def create(item):
    checklist.append(item)
    
    # READ
def read(index):
    return checklist[index]

print("hello \033[0;35m world")"""

from termcolor import colored

print colored('hello', 'red'), colored('world', 'green')