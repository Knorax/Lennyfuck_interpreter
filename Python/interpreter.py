#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
from CodeManager import *
import copy

# Interprets the Lenny code and converts it to python
def interpret(path):

    # Open file to read the code from
    f = open(path, "r")

    # Read content
    code = f.read()

    # Print the code as is
    print(code)

    # Pass it to our code manager (to clean it and execute it later)
    codeManager = CodeManager(code)
    
    # Print the converted code (the code in Lenny is converted in Brainfuck+3 to make it easier to decode it)
    print(codeManager["code"])

    # We know our manners, we close the file after using it
    f.close()

    # Execute it!
    return codeManager.execute()


if(len(sys.argv) > 1) :
    print(sys.argv[1])
    worked = interpret(sys.argv[1])
    if(worked == 1) :
        print("The code is fully Lennisizible!")
    elif(worked == -1) :
        print("Lenny took a stroll, so there's nothing to do here...")
    elif(worked == -2) :
        print("There's a spy in those Lennies!")
