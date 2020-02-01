import pprint
import random
import time
from tkinter import Canvas, Tk
import multiprocessing.dummy as mp 

rows = 50
cols = 50
cellSize = 10

def randMatrix():
    return [[random.random() > 0.85 for j in range(cols)] for i in range(rows)]


def getNeighbors(cellAlive,x,y): #Possibly Logically Incorrect
    count = 0
    for j in range((y-1)%rows,(y+2)%rows):
        for i in range((x-1)%cols,(x+2)%cols):
            if not ((i == x) and (j == y)):
                #print(f'cords: ({i},{j})')
                if cellAlive[i][j]:
                    count += 1
    return count


def checkForStateChange(cellAlive,checkTime=False):
    if checkTime:
        start = time.time_ns()
        for j in range(rows):
            for i in range(cols):
                n = getNeighbors(cellAlive,i,j)
                if cellAlive[i][j]:
                    if not(2 <= n <= 3):
                        cellAlive[i][j] = False
                else:
                    if n == 3:
                        cellAlive[i][j] = True
        print(f'checkForState Executions/sec: {1/((time.time_ns() - start)/1000000000.0):.2f}')
    else:
        for j in range(rows):
            for i in range(cols):
                n = getNeighbors(cellAlive,i,j)
                if cellAlive[i][j]:
                    if not(2 <= n <= 3):
                        cellAlive[i][j] = False
                else:
                    if n == 3:
                        cellAlive[i][j] = True
        
        

class drawingTest(object):

    def __init__(self):
        self.windowWidth = cols * cellSize
        self.windowHeight = rows * cellSize
        self.root = Tk()

        self.dispCanvas = Canvas(self.root, width=self.windowWidth, height=self.windowHeight)
        
        self.dispCanvas.pack()

        self.myCircle = [[(self.dispCanvas.create_rectangle(cellSize*i,cellSize*j,cellSize*(i+1),cellSize*(j+1), fill='#222222'))for j in range(cols)] for i in range(rows)]
        self.dispCanvas.pack()
        self.cellAlive = randMatrix()
        self.root.after(0, self.animation(checkTime=True))

        self.root.mainloop()

    def animation(self, checkTime=False):
        if checkTime:
            while True:
                start = time.time_ns()
                #DISPLAY FRAME
                for y in range(rows):
                    for x in range(cols):
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
                for y in range(rows):
                    for x in range(cols):
                        if self.cellAlive[x][y]:
                            self.dispCanvas.itemconfig(self.myCircle[x][y], fill='green')
                        else:
                            self.dispCanvas.itemconfig(self.myCircle[x][y], fill='#222222')
                #UPDATE FRAME
                self.dispCanvas.update()
                checkForStateChange(self.cellAlive)

                
def main():
    drawingTest()
if __name__ == '__main__':
    main()


        

