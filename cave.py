# IMPORT STATEMENTS
from level import Level
import pyfiglet
from os import system


class Cave:
    T_Loc = []
    lvl = Level.Master_Level

    def __init__(self):
        pass

    @staticmethod
    def find_location(lst, tgt):
        for i, row in enumerate(lst):
            for j, element in enumerate(row):
                if element == tgt:
                    return [i, j]

    @staticmethod
    def detect_collision(lst, tgt):
        t_loc = []
        h = tgt
        t_loc.append(h)
        for x, y in enumerate(t_loc):
            for a, b in enumerate(lst):
                if y == b:
                    return True

    @staticmethod
    def win_conditions():
        from hero import Hero
        game_status = False
        t_loc = []
        h_loc = [Cave.find_location(Level.Master_Level, 'H')]
        # m_loc = Cave.find_location(Level.Master_Level, 'M')
        # m_loc = Level.MONSTER
        t_loc.append(Level.TREASURE)
        mk = False

        # if not Hero.SLAIN:
        row = Level.MONSTER[0][0]
        col = Level.MONSTER[0][1]
        m_killbox = [
            [row - 1, col],  # Top
            [row + 1, col],  # Bottom
            [row, col - 1],  # Left
            [row, col + 1],  # Right
        ]

        for x, y in enumerate(h_loc):
            for a, b in enumerate(m_killbox):
                if y == b:
                    mk = True

        if Hero.SLAIN:
            mk = False

        if h_loc == Level.TREASURE:
            system('cls')
            game_status = True
            print("You found the Treasure!")
            print(print(pyfiglet.figlet_format("You Win", font='slant')))
        elif h_loc == Level.PIT:
            system('cls')
            game_status = True
            print("You fell in a pit")
            print(print(pyfiglet.figlet_format("GAME OVER", font='slant')))
        elif mk:
            system('cls')
            game_status = True
            print("The Monster found you")
            print(print(pyfiglet.figlet_format("GAME OVER", font='slant')))
        return game_status
