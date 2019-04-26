#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)


class Cell:
    def __init__(self, i, j, cell_size):
        self.row = i
        self.col = j
        self.cell_size = cell_size
        self.number = 0

    def __repr__(self):
        return f"Row: {self.row}, Col: {self.col}, Number: {self.number}"
    
    def draw(self, surface):
        w, h = self.cell_size
        i, j = self.row, self.col

        color = 255//(self.number+1),0,0
        
        pygame.draw.rect(surface, color, (i*w, j*h, (i+1)*w, (j+1)*h))
        
        myfont = pygame.font.SysFont("monospace", 60)

        label = myfont.render(str(self.number), 1, (255,255,0))
        
        surface.blit(label, (i*w, j*h + 60//2))

class Grid:
    def __init__(self, whigh, wwidth):
        self.whigh = whigh
        self.wwidth = wwidth
        cell_size = (whigh // 4, wwidth // 4)
        self.cells = [[Cell(i, j, cell_size) for i in range(4)] for j in range(4)]

    def draw(self, surface):
        for row in self.cells:
            for cell in row:
                cell.draw(surface)


def events(objects):
    mainloop = True
    available_moves = {
        pygame.K_DOWN : "move_down", 
        pygame.K_UP : "move_up",
        pygame.K_RIGHT : "move_right",
        pygame.K_LEFT : "move_left"
    }
    moves = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            if event.key in available_moves:
                moves.append(available_moves[event.key])
    return mainloop, moves

def flush(cells, dir, prev_moved = False):
    moved = False
    print("Hi")
    if dir == "down":
        for i in range(3):
            for j in range(4):
                if cells[i][j].number != 0 and cells[i+1][j].number == 0:
                    cells[i+1][j].number = cells[i][j].number
                    cells[i][j].number = 0
                    moved = True
    elif dir == "up":
        for i in range(1,4):
            for j in range(4):
                if cells[i][j].number != 0 and cells[i-1][j].number == 0:
                    cells[i-1][j].number = cells[i][j].number
                    cells[i][j].number = 0
                    moved = True
    elif dir == "left":
        for i in range(4):
            for j in range(1, 4):
                if cells[i][j].number != 0 and cells[i][j-1].number == 0:
                    cells[i][j-1].number = cells[i][j].number
                    cells[i][j].number = 0
                    moved = True
    elif dir == "right":
        for i in range(4):
            for j in range(3):
                if cells[i][j].number != 0 and cells[i][j+1].number == 0:
                    cells[i][j+1].number = cells[i][j].number
                    cells[i][j].number = 0
                    moved = True
    if moved:
        moved = flush(cells, dir, moved)
    return moved or prev_moved
def d_move(cells):
    moved = False
    moved = moved or flush(cells, "down")
    for i in range(3):
        for j in range(4):
            if cells[i][j].number != 0 and cells[i][j].number == cells[i+1][j].number:
                cells[i][j].number = 0
                cells[i+1][j].number *= 2
                moved = True
    moved = flush(cells, "down") or moved
    return moved

def u_move(cells):
    moved = False
    moved = moved or flush(cells, "up")
    for i in range(3, 0, -1):
        for j in range(4):
            if cells[i][j].number != 0 and cells[i][j].number == cells[i-1][j].number:
                cells[i][j].number = 0
                cells[i-1][j].number *= 2
                moved = True
    moved = flush(cells, "up")  or moved
    return moved

def l_move(cells):
    moved = False
    moved = moved or flush(cells, "left")
    for i in range(4):
        for j in range(3):
            if cells[i][j].number != 0 and cells[i][j].number == cells[i][j+1].number:
                cells[i][j].number = 0
                cells[i][j+1].number *= 2
                moved = True
    moved = flush(cells, "left") or moved
    return moved

def r_move(cells):
    moved = False
    moved = moved or flush(cells, "right")
    for i in range(4):
        for j in range(1,4):
            if cells[i][j].number != 0 and cells[i][j].number == cells[i][j-1].number:
                cells[i][j].number = 0
                cells[i][j-1].number *= 2
                moved = True
    moved = flush(cells, "right") or moved
    return moved

def move_possible(cells):
    possible = False
    for i in range(3):
        for j in range(3):
            if cells[i][j].number == 0 or \
                cells[i][j].number == cells[i][j+1].number or \
                cells[i][j].number == cells[i+1][j+1].number:
                possible = True
                # print(possible)
                break
    if cells[-1][-1].number == 0:
        possible = True
    return possible

def spawn_two(cells):
    cells_list = [cell for cell_row in cells for cell in cell_row]
    free_cells = list(filter(lambda cell: cell.number == 0, cells_list))
    ind = random.randint(0, len(free_cells)-1)
    free_cells[ind].number = 2

def loop(objects, moves):
    pygame.time.wait(50)
    mainloop = True
    available_moves = {
        "move_down" : d_move,
        "move_up" : u_move,
        "move_right" : r_move,
        "move_left" : l_move
    }
    grid = objects['Grid']
    cells = grid.cells
    m_possible = move_possible(cells)
    if m_possible:
        moved = False
        for move in moves:
            moved = available_moves[move](cells)
        if moved:
            spawn_two(cells)
    else:
        print("GAME OVER")
        mainloop = False
    return mainloop
    
def draw(objects: dict, surface): # opisałem typ zmiennej objects
    for ob in objects.values():
        ob.draw(surface)

    pygame.display.flip()

def init():
    pygame.init()
    pygame.font.init()
    objects = {}
    mainloop = True          
    FPS = 30
    playtime = 0.0

    width, height = 640, 480
    size = width, height
    screen = pygame.display.set_mode((640,480))
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))

    objects['Grid'] = Grid(width, height)
    # print(objects[0].cells)
    spawn_two(objects['Grid'].cells)

    return objects, mainloop, screen

def main():
    objects, mainloop, screen = init()
    
    while mainloop:
        mainloop, moves = events(objects)
        mainloop = loop(objects, moves) and mainloop
        draw(objects, screen)
    
    pygame.quit()
    
main()