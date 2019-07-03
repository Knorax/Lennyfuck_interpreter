#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from enum import Enum
import copy
import re

class Lennies(Enum) :
    PLUS_LENY = "( ͡° ͜ʖ ͡°)"
    MINUS_LENY = "(> ͜ʖ<)"
    DOT_LENY = "(♥ ͜ʖ♥)"
    COMMA_LENY = "ᕙ( ͡° ͜ʖ ͡°)ᕗ"
    MOVE_LEFT_LENY = "(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ.*"
    MOVE_RIGHT_LENY = "ᕦ( ͡°ヮ ͡°)ᕥ"
    MOVE_UP_LENY = "ᕦ( ͡° ͜ʖ ͡°)ᕥ"
    MOVE_DOWN_LENY = "( ͡°╭͜ʖ╮ ͡°)"
    LEFT_BRACKET_LENY = "( ͡°("
    REIGHT_BRACKET_LENY = ") ͡°)"
    TERMINATOR_LENY = "ಠ_ಠ"
# Adds a cell to the table of values (to keep track of the pointer and values)
def addTablePos(x, y, table) :
        table.append({
        "x" : x,
        "y" : y,
        "val" : 0
        })

# Check the syntax of the Lenny code (eventually, i'd like a stack trace if it is not valid)
def checkSyntax(code) :
    # Remove all lennies found and trim it afterwards
    cleanCode = copy.copy(code)
    for lenny in Lennies :
        if(lenny.value in cleanCode) :
            cleanCode = cleanCode.replace(lenny.value, '')

    cleanCode = cleanCode.strip()
    # If nothing is left, it means all Lennies are good Lennies and there are no bad characters in the code
    return len(cleanCode) == 0

# Interprets the Lenny code and converts it to python
def interpret(path):
    # Init our value table
    table = [{
    "x" : 0,
    "y" : 0,
    "val" : 0
    }]

    # Open file to read the code from
    f = open(path, "r")
    code = f.read()
    # We know our manners, we close the file after using it
    f.close()

    # Check if Lenny is here, if not we get outta here
    if(len(code) == 0) :
        return -1

    # Do a simple syntax check
    goodCode = checkSyntax(code)

    # If the code is no bueno, yee your last haw and exit
    if(not goodCode) :
        return -2

    # TODO: add behaviour of each Lennies


    return 1

worked = interpret("D:\\Sam El Terror\\Documents\\Qt Project\\Lenny\\Python\\test.txt")
if(worked == 1) :
    print("The code is fully Lennisizible!")
elif(worked == -1)
    print("Lenny took a stroll, so there's nothing to do here...")
elif(worked == -2)
    print("There's a spy in those Lennies!")
