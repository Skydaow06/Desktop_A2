cell_size = 80

def setup():
    size(cell_size*9, cell_size*9)

def draw():
    background(200)
    drawGrid()

def drawGrid():
    i = 0
    while (i <= 9):   
        line(cell_size*i, 0, cell_size*i, height)
        i += 1

    j = 0
    while (j<= 9):   
        line(0, cell_size*j, width, cell_size*j)
        j += 1
