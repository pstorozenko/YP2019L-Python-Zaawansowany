import pygame

class Cell:
    def __init__(self, i, j, cell_size):
        self.i = i
        self.j = j
        self.size = cell_size
        self.number = 0
    
    def draw(self, surface):
        print("Rysuję")
        # print(self.number, end="")
        #pygame.draw.rect()
        w, h = self.size
        i, j = self.i, self.j # to samo jakbym zrobił i = self.i j = self.j w dwóch linijkach

        color = self.number,self.number,self.number
        pygame.draw.rect(surface, color, (i*w, j*h,(i+1)*w, (j+1)*h))

        myfont = pygame.font.SysFont("arial", 60)

        label = myfont.render(str(self.number), 1, (255,255,0))

        surface.blit(label,(i*w +30, j*h + 30))
    
    def __repr__(self):
        return f"Cell ({self.i}, {self.j}, number: {self.number})"


class Grid:
    def __init__(self, size):
        cell_size = size[0] // 4, size[1] // 4
        self.cells = [[Cell(i, j, cell_size) for i in range(4)] for j in range(4)]

    def draw(self, surface):
        # print("=" * 30)
        for i in range(4):
            for j in range(4):
                self.cells[i][j].draw(surface)
                # print('\t', end="")
            # print()
        # print("=" * 30)