import pygame
from misc import Grid
import random

def init():
    pygame.init()
    hight = 480
    width = 600
    screen = pygame.display.set_mode((width, hight))
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    mainloop = True

    objects = {}
    objects['Grid'] = Grid()

    return mainloop, screen, objects

def end():
    pygame.quit()

def events():
    mainloop = True
    available_moves = {
        pygame.K_DOWN : "move_down",
        pygame.K_UP : "move_up",
        pygame.K_LEFT : "move_left",
        pygame.K_RIGHT : "move_right"
    }
    moves = []
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            if event.key in available_moves:
                moves.append(available_moves[event.key])
            
    return mainloop, moves

def spawn_two(cells):
    cells_list = [cell for cells_row in cells for cell in cells_row] # zamień listę list elementów na listę elementów
    free_cells = list(filter(lambda cell: cell.number == 0, cells_list))
    ind = random.randint(0, len(free_cells) - 1)
    free_cells[ind].number = 2
    print(free_cells)

def move_d(cells):
    pass

def move_u(cells):
    pass

def move_l(cells):
    pass
    
def move_r(cells):
    pass
    
def loop(objects, moves):
    cells = objects['Grid'].cells
    available_moves = {
        "move_down" : move_d,
        "move_up" : move_u,
        "move_left" : move_l,
        "move_right": move_r
    }
    if len(moves) > 0:
        for move in moves:
            available_moves[move](cells)
        spawn_two(cells)

    pygame.time.wait(1000)

def draw(objects):
    objects['Grid'].draw()

def main():
    mainloop, screen, objects = init()

    while mainloop:
        mainloop, moves = events()
        loop(objects, moves)
        draw(objects)
    end()

main()