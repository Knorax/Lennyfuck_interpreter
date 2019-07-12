#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
from enum import Enum
import re
from TwoDimensionTableManager import *

class CodeManager(dict) :

    # Enum containing the Error Codes (I'll add more eventually)
    class ErrorCodes(Enum) :
        MISSING_RIGHT_BRACKET = {"id" : -1, "msg" : "Missing right bracket"}
        NO_MATCH_FOR_RIGHT_BRACKET = {"id" : -2, "msg" : "Missing left bracket"}

    # Enumerate the Lennies and their brainfuck+3 equivalent
    class Lennies(Enum) :
        __order__ = "DOT_LENY COMMA_LENY MOVE_LEFT_LENY MOVE_RIGHT_LENY MOVE_UP_LENY MOVE_DOWN_LENY LEFT_BRACKET_LENY RIGHT_BRACKET_LENY PLUS_LENY MINUS_LENY TERMINATOR_LENY"
        DOT_LENY = {"lenny" : "(♥ ͜ʖ♥)", "bfuck3" : "."}
        COMMA_LENY = {"lenny" : "ᕙ( ͡° ͜ʖ ͡°)ᕗ", "bfuck3" : ","}
        MOVE_LEFT_LENY = {"lenny" : "(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ.*", "bfuck3" : "<"}
        MOVE_RIGHT_LENY = {"lenny" : "ᕦ( ͡°ヮ ͡°)ᕥ", "bfuck3" : ">"}
        MOVE_UP_LENY = {"lenny" : "ᕦ( ͡° ͜ʖ ͡°)ᕥ", "bfuck3" : "^"}
        MOVE_DOWN_LENY = {"lenny" : "( ͡°╭͜ʖ╮ ͡°)", "bfuck3" : "v"}
        LEFT_BRACKET_LENY = {"lenny" : "( ͡°(", "bfuck3" : "["}
        RIGHT_BRACKET_LENY = {"lenny" : ") ͡°)", "bfuck3" : "]"}
        PLUS_LENY = {"lenny" : "( ͡° ͜ʖ ͡°)", "bfuck3" : "+"}
        MINUS_LENY = {"lenny" : "(> ͜ʖ<)", "bfuck3" : "-"}
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
        error = self.buildBracketPairs()
        if(error != 0) :
            print(error)

    # Convert the Lennies into brainfuck (simply because Lenny is hard to gauge something)
    def convertToBrainfuck3(self) :
        for lenny in self.Lennies :
            self["code"] = self["code"].replace(lenny.value["lenny"], lenny.value["bfuck3"])

    # Clean the code... Actually just remove the whitespace characters
    def cleanBrainfuck3Code(self) :
        self["code"] = re.sub(r'\s+', '', self["code"])

    # Build the bracket pairs dictionary so it gets easier to jump when we get to those commands
    def buildBracketPairs(self) :
        openedBracketId = []
        # Loops through every characters in the code
        for i in range(len(self["code"])) :
            # When we see a left bracket ([), add its id to the list
            if(self["code"][i] == self.Lennies.LEFT_BRACKET_LENY.value["bfuck3"]) :
                openedBracketId.append(i)
            # When we see a right bracket ([), get the last bracket from the list and put it in the dictionary
            # with a key equal to the id of the right bracket. Then delete the last item in the list
            elif(self["code"][i] == self.Lennies.RIGHT_BRACKET_LENY.value["bfuck3"] and len(openedBracketId) != 0) :
                self["bracketPairs"][i] = openedBracketId.pop()
            # If we have a right bracket but our list is empty, it means there is a left bracket missing for this one
            elif(self["code"][i] == self.Lennies.RIGHT_BRACKET_LENY.value["bfuck3"] and len(openedBracketId) == 0) :
                return {"error" : self.ErrorCodes.NO_MATCH_FOR_RIGHT_BRACKET.value["msg"], "position" : i}
        # After the loop, check if there are unassigned bracket id in the list (to detect missing right brackets)
        if(len(openedBracketId) != 0) :
            return {"error" : self.ErrorCodes.MISSING_RIGHT_BRACKET.value["msg"], "position" : openedBracketId[0]}
        # Return 0 upon success
        return 0

    # Get the right bracket paired with the left bracket at this id
    # Var :
    #       - currentId : id of the left bracket we are at right now
    def getPairedRightBracket(self, currentId) :
        # Since the dictionary is organised as {"rightBracketId" : "leftBracketId", ...}
        # We look through the items in it and return the key paired with value of a given id
        for rBracketId, lBracketId in self["bracketPairs"].items() :
            if(currentId == lBracketId) :
                return rBracketId
    # Get the left bracket paired with the right bracket at this id
    # Var :
    #       - currentId : id of the right bracket we are at right now
    def getPairedLeftBracket(self, currentId) :
        return self["bracketPairs"][currentId]

    # Get the command at this id
    # Var :
    #       - currentId : id of the command we are currently at
    def getCommandAtId(self, currentId) :
        return self["code"][currentId]

    # Wait for an input, it must be a single ascii character
    def getSingleCharAsInput(self) :
        print("Please enter a character.")

        while(True) :
            sys.stdout.flush()
            c = raw_input()
            if(c == "exit") :
                break
            elif(len(c) != 1) :
                print("Wrong input, enter a single character and press Enter...")
            else :
                return ord(c[0])

    # Execute the code
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
                table.update(currentXPos, currentYPos, self.getSingleCharAsInput())
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
                if(table[currentXPos][currentYPos] != 0) :
                    currentId = self.getPairedLeftBracket(currentId)
            elif(currentCommand == self.Lennies.TERMINATOR_LENY.value["bfuck3"]) :
                break

            currentId+=1

        return 1
