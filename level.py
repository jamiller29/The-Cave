import pyfiglet
from random import choice

class Level:
    # Class Variables
    Master_Level = []
    Wall_Loc = []
    Spawn_Loc = []
    TREASURE = []
    PIT = []
    MONSTER = []
    COMPAS = []


    def __init__(self):
        self.rows = 20
        self.cols = 20

    @classmethod
    # Load the game file.
    def load_level(cls, select_file):
        with open(select_file) as file:
            lvl = file.read()

        # Remove any white spaces inside the file.
        for i in range(0, len(lvl), 40):
            level_slice = list(lvl[i:i + 39])
            while ' ' in level_slice:
                level_slice.remove(' ')
            # print(level_slice)
            Level.Master_Level.append(level_slice)


    @staticmethod
    def find_position(lst, output_lst, tgt):
        for i, sublist in enumerate(lst):
            for j, element in enumerate(sublist):
                if element == tgt:
                    output_lst.append([i, j])

    # A function to write the level to a text file.
    @classmethod
    def write_level(cls, lst, file_name):
        file_name = open(file_name, "w")
        for line in lst:
            file_name.write(' '.join(line) + '\n')
        file_name.close()

    @staticmethod
    def detect_collision(lst, tgt):
        for x, y in enumerate(tgt):
            for a, b in enumerate(lst):
                if y == b:
                    return True

    # A function to get adjacent index locations to a target.
    @staticmethod
    def dmz(row, col, lst, out_put_lst, no_spawn_range):
        if no_spawn_range == 1:
            i, j = 1, 2
        elif no_spawn_range == 2:
            i, j = 2, 3
        else:
            i, j = 3, 4
        for x in range(row - i, row + j):
            for y in range(col - i, col + j):
                if 0 <= x < len(lst) and 0 <= y < len(lst[row]):
                    out_put_lst.append([x, y])

    def spawn_compas(self):
        compas_location = choice(Level.Spawn_Loc)
        compas_location_x = compas_location[0]
        compas_location_y = compas_location[1]
        Level.Master_Level[compas_location_x][compas_location_y] = 'C'










