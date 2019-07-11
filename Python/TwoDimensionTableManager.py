

class TwoDimensionTableManager(dict):
    # Init our value table
    # {x1 : {y1 : valueAtx1y1, y2 : valueAtx1y2, ...}, x2 : {y1 : valueAtx2y1, ...}}
    #
    # First value at (0,0) is initialized as 0
    def __init__(self, x, y, val):
        self[x] = {y : val}

    # Function to add or update values at position (x, y)
    def update(self, x, y, val):
        if(x in self) :
            self[x][y] = val
        else :
            self[x] = {y : val}

    def moveUp(self, currentXPos, currentYPos):
        if((currentYPos + 1) not in self) :
            self.update(currentXPos, currentYPos + 1, 0)
        return currentYPos + 1

    def moveDown(self, currentXPos, currentYPos):
        if((currentYPos - 1) not in self) :
            self.update(currentXPos, currentYPos - 1, 0)
        return currentYPos - 1

    def moveRight(self, currentXPos, currentYPos):
        if((currentXPos + 1) not in self or currentYPos not in self[currentXPos + 1]) :
            self.update(currentXPos + 1, currentYPos, 0)
        return currentXPos + 1

    def moveLeft(self, currentXPos, currentYPos):
        if((currentXPos - 1) not in self or currentYPos not in self[currentXPos - 1]) :
            self.update(currentXPos - 1, currentYPos, 0)
        return currenXPos -1

    def incrementValueAt(self, currentXPos, currentYPos) :
        if(self[currentXPos][currentYPos] == 255) :
            self[currentXPos][currentYPos] = 0
        else :
            self[currentXPos][currentYPos]+=1

    def decrementValueAt(self, currentXPos, currentYPos) :
        if(self[currentXPos][currentYPos] == 0) :
            self[currentXPos][currentYPos] = 255
        else :
            self[currentXPos][currentYPos]-=1
