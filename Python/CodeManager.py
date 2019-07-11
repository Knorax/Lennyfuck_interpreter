#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from enum import Enum
import re
from TwoDimensionTableManager import *

class CodeManager(dict) :

    # Enum containing the Error Codes (I'll add more eventually)
    class ErrorCodes(Enum) :
        MISSING_RIGHT_BRACKET = -1

    # Enumerate the Lennies and their brainfuck+3 equivalent
    class Lennies(Enum) :
        PLUS_LENY = {"lenny" : "( ͡° ͜ʖ ͡°)", "bfuck3" : "+"}
        MINUS_LENY = {"lenny" : "(> ͜ʖ<)", "bfuck3" : "-"}
        DOT_LENY = {"lenny" : "(♥ ͜ʖ♥)", "bfuck3" : "."}
        COMMA_LENY = {"lenny" : "ᕙ( ͡° ͜ʖ ͡°)ᕗ", "bfuck3" : ","}
        MOVE_LEFT_LENY = {"lenny" : "(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ.*", "bfuck3" : "<"}
        MOVE_RIGHT_LENY = {"lenny" : "ᕦ( ͡°ヮ ͡°)ᕥ", "bfuck3" : ">"}
        MOVE_UP_LENY = {"lenny" : "ᕦ( ͡° ͜ʖ ͡°)ᕥ", "bfuck3" : "^"}
        MOVE_DOWN_LENY = {"lenny" : "( ͡°╭͜ʖ╮ ͡°)", "bfuck3" : "v"}
        LEFT_BRACKET_LENY = {"lenny" : "( ͡°(", "bfuck3" : "["}
        RIGHT_BRACKET_LENY = {"lenny" : ") ͡°)", "bfuck3" : "]"}
        TERMINATOR_LENY = {"lenny" : "ಠ_ಠ", "bfuck3" : "x"}

    # Init the Code manager
    # Vars :
    #       - code : the code to execute
    def __init__(self, code) :
        # Put the code in the dictionary at key "code"
        self["code"] = code
        # Convert the Lennies into Brainfuck+3 (sorry Lenny D: )
        self.convertToBrainfuck3()
        # Clean the code (remove whitespace characters)
        self.cleanBrainfuck3Code()
        
        # Init our bracket pairs (so our loops are easier to deal with)
        self["bracketPairs"] = {}
        self.buildBracketPairs()

    def convertToBrainfuck3(self) :
        for lenny in self.Lennies :
            self["code"] = self["code"].replace(lenny.value["lenny"], lenny.value["bfuck3"])

    def cleanBrainfuck3Code(self) :
        self["code"] = re.sub(r'\s+', '', self["code"])

    def buildBracketPairs(self) :
        openedBracketId = []
        for i in range(len(self["code"])) :
            if(self["code"][i] == self.Lennies.LEFT_BRACKET_LENY.value["bfuck3"]) :
                openedBracketId.append(i)
            elif(self["code"][i] == self.Lennies.RIGHT_BRACKET_LENY.value["bfuck3"]) :
                self["bracketPairs"][i] = openedBracketId.pop()
        if(len(openedBracketId) != 0) :
            return {"error" : self.ErrorCodes.MISSING_RIGHT_BRACKET.value, "position" : openedBracketId[0]}
        return 0

    def getPairedRightBracket(self, currentId) :
        for rBracketId, lBracketId in self["bracketPairs"].items() :
            if(currentId == lBracketId) :
                return rBracketId

    def getPairedLeftBracket(self, currentId) :
        return self["bracketPairs"][currentId]

    def getCommandAtId(self, currentId) :
        return self["code"][currentId]

    def getSingleCharAsInput() :
        while(True) :
            c = raw_input()
            if(len(c) != 1) :
                print("Wrong input, enter a single character and press Enter...")
            else :
                return int(c)

    def execute(self) :
        table = TwoDimensionTableManager(0, 0, 0)
        currentXPos = 0
        currentYPos = 0
        currentId = 0

        while(len(self["code"]) > currentId) : # While we aint done
            currentCommand = self.getCommandAtId(currentId) # Check what's Lenny's mood

            if(currentCommand == self.Lennies.PLUS_LENY.value["bfuck3"]) :
                table.incrementValueAt(currentXPos, currentYPos)
            elif(currentCommand == self.Lennies.MINUS_LENY.value["bfuck3"]) :
                table.decrementValueAt(currentXPos, currentYPos)
            elif(currentCommand == self.Lennies.DOT_LENY.value["bfuck3"]) :
                print(chr(table[currentXPos][currentYPos]))
            elif(currentCommand == self.Lennies.COMMA_LENY.value["bfuck3"]) :
                table.update(currentXPos, currentYPos, getSingleCharAsInput())
            elif(currentCommand == self.Lennies.MOVE_LEFT_LENY.value["bfuck3"]) :
                currentXPos = table.moveLeft(currentXPos, currentYPos)
            elif(currentCommand == self.Lennies.MOVE_RIGHT_LENY.value["bfuck3"]) :
                currentXPos = table.moveRight(currentXPos, currentYPos)
            elif(currentCommand == self.Lennies.MOVE_UP_LENY.value["bfuck3"]) :
                currentYPos = table.moveUp(currentXPos, currentYPos)
            elif(currentCommand == self.Lennies.MOVE_DOWN_LENY.value["bfuck3"]) :
                currentYPos = table.moveDown(currentXPos, currentYPos)
            elif(currentCommand == self.Lennies.LEFT_BRACKET_LENY.value["bfuck3"]) :
                if(table[currentXPos][currentYPos] == 0) :
                    currentId = self.getPairedRightBracket(currentId)
            elif(currentCommand == self.Lennies.RIGHT_BRACKET_LENY.value["bfuck3"]) :
                if(table[currentXPos][currentYPos] == 0) :
                    currentId = self.getPairedLeftBracket(currentId)
            elif(currentCommand == self.Lennies.TERMINATOR_LENY.value["bfuck3"]) :
                break

            currentId+=1

        return 1
