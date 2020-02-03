import pprint, random, time
from tkinter import Canvas, Tk, Button, Frame

# SETTINGS
ROWS = 35
COLS = 35
CELL_SIZE = 15

# 0 to 1, Chance for Cell to be Alive on Reset
INIT_CHANCE = 0.08 

# Using torus geometry, wraps around to other side

def getNeighbors(cellAlive,x,y):

    """
    If there is living cell adjacent to cell, count it and return it.
    """

    count = 0
    for j in range((y-1),(y+2)):
        for i in range((x-1),(x+2)):
            if not ((i == x) and (j == y)):
                if cellAlive[i%COLS][j%ROWS]:
                    count += 1
    return count


def checkForStateChange(cellAlive,checkTime=False):

    """
    After receiving the number of neighbors from getNeighbors(...) decides
    if that cells lives or dies. When the function is called, all cells
    are checked.
    """

    start = time.time_ns()
    for j in range(ROWS):
        for i in range(COLS):
            n = getNeighbors(cellAlive,i,j)
            if cellAlive[i][j]:
                if not((n==2) or (n==3)):
                    cellAlive[i][j] = False
            else:
                if n == 3:
                    cellAlive[i][j] = True

        
        

class drawingTest(object):
    
    """
    tkinter GUI Elements
    """

    def __init__(self):
        self.windowWidth = COLS * CELL_SIZE
        self.windowHeight = ROWS * CELL_SIZE
        self.root = Tk()

        self.dispCanvas = Canvas(self.root, width=self.windowWidth, height=self.windowHeight)
        
        self.dispCanvas.pack()

        self.myCircle = [[(self.dispCanvas.create_rectangle(CELL_SIZE*i,CELL_SIZE*j,CELL_SIZE*(i+1),CELL_SIZE*(j+1), fill='#222222'))for j in range(COLS)] for i in range(ROWS)]
        self.dispCanvas.pack()
        self.toolbar = Frame(self.root)
        
        self.resetButton = Button(self.toolbar, text="Reset", command=self.resetCells)
        self.resetButton.pack()
        
        self.toolbar.pack()
        self.cellAlive = self.randMatrix()
        self.root.after(0, self.animation(checkTime=True))
        self.root.mainloop()
    
    def randMatrix(self):
        return [[random.random() < INIT_CHANCE for j in range(COLS)] for i in range(ROWS)]


    def resetCells(self):
        self.cellAlive = self.randMatrix()

    def animation(self, checkTime=False):
        if checkTime:
            while True:
                start = time.time_ns()
                #DISPLAY FRAME
                for y in range(ROWS):
                    for x in range(COLS):
                        if self.cellAlive[x][y]:
                            self.dispCanvas.itemconfig(self.myCircle[x][y], fill='green')
                        else:
                            self.dispCanvas.itemconfig(self.myCircle[x][y], fill='#222222')
                #UPDATE FRAME
                self.dispCanvas.update()
                checkForStateChange(self.cellAlive)
                print(f'checkForState Executions/sec: {1/((time.time_ns() - start)/1000000000.0):.2f}')
        else:
            while True:
                #DISPLAY FRAME
                for y in range(ROWS):
                    for x in range(COLS):
                        if self.cellAlive[x][y]:
                            self.dispCanvas.itemconfig(self.myCircle[x][y], fill='green')
                        else:
                            self.dispCanvas.itemconfig(self.myCircle[x][y], fill='#222222')
                #UPDATE FRAME
                self.dispCanvas.update()
                checkForStateChange(self.cellAlive)


    #----DEBUG METHODS---------
    def highlightNeighbors(self,x,y):
        print(f'Origin Point: ({x},{y})')
        for j in range((y-1),(y+2)):
            for i in range((x-1),(x+2)):
                print(f'({i},{j})')
                if not ((i == x) and (j == y)):
                    self.dispCanvas.itemconfig(self.myCircle[i%COLS][j%ROWS], fill='purple')
                else:
                    self.dispCanvas.itemconfig(self.myCircle[i%COLS][j%ROWS], fill='blue')


    def highlightCorners(self):
        self.dispCanvas.itemconfig(self.myCircle[0][0], fill='red')
        self.dispCanvas.itemconfig(self.myCircle[COLS-1][0], fill='red')
        self.dispCanvas.itemconfig(self.myCircle[0][ROWS-1], fill='red')
        self.dispCanvas.itemconfig(self.myCircle[COLS-1][ROWS-1], fill='red')
    #------END DEBUG METHODS------


def main():
    drawingTest()
if __name__ == '__main__':
    main()


        

