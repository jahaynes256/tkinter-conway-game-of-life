import pprint
import random
import time

rows = 10
cols = 10
cellSize = 5

def randMatrix():
    return [[1 == random.randint(0,1) for j in range(cols)] for i in range(rows)]


def printMatrix(list2D): #DEBUG: Display Data Structure
    for j in range(rows):
        for i in range(cols):
            if list2D[i][j]:
                print("■ ", end='')
            else:
                print("  ", end= '')
        print()
    print()


def getNeighbors(cellAlive,x,y): #Possibly Logically Incorrect
    count = 0
    for j in range((y-1)%rows,(y+2)%rows):
        for i in range((x-1)%cols,(y+2)%cols):
            if cellAlive[i][j]:
                count += 1
    return count


def checkForStateChange(cellAlive):
    for j in range(rows):
        for i in range(cols):
            n = getNeighbors(cellAlive,i,j)
            if cellAlive[i][j]:
                if not(2 <= n <= 3):
                    cellAlive[i][j] = False
            else:
                if n == 3:
                    cellAlive[i][j] = True


def main():
    cellAlive = randMatrix()
    while True:
        checkForStateChange(cellAlive)
        printMatrix(cellAlive)
        time.sleep(0.2)


if __name__ == '__main__':
    main()

        

