import pygame
from misc import Grid
import random

def udf(ll): # robi up down flip
    return list(reversed(ll))

def trans(ll): # robi transpozycję czyli zamienia 
    res = []
    for row in zip(*ll):
        res.append(list(row))
    return res

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

def push_d(cells):
    changed = False
    for i in range(3):
        for j in range(4):
            if cells[i][j].number != 0 and cells[i+1][j].number == 0:
                cells[i+1][j].number = cells[i][j].number
                cells[i][j].number = 0
                changed = True
    return changed

def merge_d(cells):
    for i in range(3):
        for j in range(4):
            if cells[i][j].number != 0 and cells[i][j].number == cells[i+1][j].number:
                cells[i][j].number = cells[i][j].number * 2
                cells[i+1][j].number = 0

def move_d(cells):
    changed = False
    changed = push_d(cells) or changed
    merge_d(cells)
    changed = push_d(cells) or changed
    return changed

def move_u(cells):
    good_form = udf(cells)
    changed = move_d(good_form)
    return changed

def move_l(cells):
    good_form = udf(trans(cells))
    changed = move_d(good_form)
    return changed
    
def move_r(cells):
    good_form = trans(cells)
    changed = move_d(good_form)
    return changed

def move_possible(cells):
    for i in range(4):
        for j in range(4):
            if cells[i][j].number==0:
                return True
    for i in range(3):
        for j in range(4):
            if cells[i][j].number == cells[i+1][j].number:
                return True
    for i in range(4):
        for j in range(4):
            if cells[i][j].number == cells[i][j+1].number:
                return True
    return False

def loop(objects, moves):
    cells = objects['Grid'].cells
    available_moves = {
        "move_down" : move_d,
        "move_up" : move_u,
        "move_left" : move_l,
        "move_right": move_r
    }
    should_draw = False
    if not move_possible(cells):
        mainloop = False
        return should_draw, mainloop
    if len(moves) > 0:
        should_draw = True
        changed = False
        for move in moves:
            changed = available_moves[move](cells)
        if changed:
            spawn_two(cells)

    pygame.time.wait(10)
    return should_draw, True

def draw(objects, should_draw, screen):
    if should_draw:
        objects['Grid'].draw(screen)
    pygame.display.flip()

def init():
    pygame.init()
    pygame.font.init()
    height = 480
    width = 600
    size = width, height
    screen = pygame.display.set_mode((width, height))
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    mainloop = True

    objects = {}
    objects['Grid'] = Grid(size)
    spawn_two(objects['Grid'].cells)
    return mainloop, screen, objects

def main():
    mainloop, screen, objects = init()

    draw(objects, True, screen)
    while mainloop:
        mainloop1, moves = events()
        should_draw, mainloop2 = loop(objects, moves)
        draw(objects, should_draw, screen)

        mainloop = mainloop1 and mainloop2
    end()

main()