#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from enum import Enum
from TwoDimensionTableManager import *
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

def getNextLenny(lenny, code, startIndex) :
    for(lenny in Lennies) :
        if(re.search('\A'+lenny.value, code[startIndex:startIndex+20])) :
            return lenny.value

def executeCode(code) :
    table = TwoDimensionTableManager(0, 0, 0)
    currentXPos = 0
    currentYPos = 0
    currentIndex = 0;

    while(len(code) > currentIndex) :
        lennyFound = getNextLenny(lenny, code, startIndex)
        if(lennyFound == Lennies.PLUS_LENY) :
            lennyFound = Lennies.PLUS_LENY

            if(table[currentXPos][currentYPos] == 255) :
                table[currentXPos][currentYPos] = 0
            else :
                table[currentXPos][currentYPos]++

        elif(isNextLenny(Lennies.PLUS_LENY, code, currentIndex)) :
            lennyFound = Lennies.MINUS_LENY
            if(table[currentXPos][currentYPos] == 0) :
                table[currentXPos][currentYPos] = 255
            else :
                table[currentXPos][currentYPos]--
        elif(isNextLenny(Lennies.PLUS_LENY, code, currentIndex)) :
            lennyFound = Lennies.DOT_LENY
            print("%c", table[currentXPos][currentYPos])
        elif(isNextLenny(Lennies.PLUS_LENY, code, currentIndex)) :
            lennyFound = Lennies.COMMA_LENY
            isBadInput = True
            while(isBadInput)
                c = raw_input()
                if(len(c) != 1) :
                    print("Wrong input, enter a single character and press Enter...")
                else :
                    isBadInput = False
            table.update(currentXPos, currentYPos, )
        elif(isNextLenny(Lennies.PLUS_LENY, code, currentIndex)) :
            lennyFound = Lennies.MOVE_LEFT_LENY
            table.moveLeft(currentXPos, currentYPos)
            currentXPos--;
        elif(isNextLenny(Lennies.PLUS_LENY, code, currentIndex)) :
            lennyFound = Lennies.MOVE_RIGHT_LENY
            table.moveRight(currentXPos, currentYPos)
            currentXPos++;
        elif(isNextLenny(Lennies.PLUS_LENY, code, currentIndex)) :
            lennyFound = Lennies.MOVE_UP_LENY
            table.moveUp(currentXPos, currentYPos)
            currentYPos++;
        elif(isNextLenny(Lennies.PLUS_LENY, code, currentIndex)) :
            lennyFound = Lennies.MOVE_DOWN_LENY
            table.moveDown(currentXPos, currentYPos)
            currentYPos--;
        elif(isNextLenny(Lennies.PLUS_LENY, code, currentIndex)) :
            lennyFound = Lennies.LEFT_BRACKET_LENY
        elif(isNextLenny(Lennies.PLUS_LENY, code, currentIndex)) :
            lennyFound = Lennies.REIGHT_BRACKET_LENY

        elif(isNextLenny(Lennies.PLUS_LENY, code, currentIndex)) :
            return 1

# Interprets the Lenny code and converts it to python
def interpret(path):

    # Open file to read the code from
    f = open(path, "r")
    code = f.read()
    code = re.sub("\s+", '', code) # remove all whitespace characters

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
    executeCode(code)

    return 1

worked = interpret("D:\\Sam El Terror\\Documents\\Qt Project\\Lenny\\Python\\test.txt")
if(worked == 1) :
    print("The code is fully Lennisizible!")
elif(worked == -1) :
    print("Lenny took a stroll, so there's nothing to do here...")
elif(worked == -2) :
    print("There's a spy in those Lennies!")
