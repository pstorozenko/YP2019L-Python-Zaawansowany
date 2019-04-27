
class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.number = 0
    
    def draw(self):
        print(self.number, end="")
    
    def __repr__(self):
        return f"Cell ({self.i}, {self.j}, number: {self.number})"


class Grid:
    def __init__(self):
        self.cells = [[Cell(i,j) for i in range(4)] for j in range(4)]

    def draw(self):
        print("=" * 30)
        for i in range(4):
            for j in range(4):
                self.cells[i][j].draw()
                print('\t', end="")
            print()
        print("=" * 30)