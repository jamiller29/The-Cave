# IMPORT STATEMENTS
from level import Level
from cave import Cave
from random import choice


class Hero:
    # Class Variables
    Player_Map = []
    SLAIN = False

    def __init__(self):
        self.speed = 1
        self.flashlight = 1
        self.attack_range = 2
        self.has_spear = True

    @staticmethod
    def spawn_hero(): # Randomly Spawn the Hero
        Hero.Player_Map = [[' ' for _ in range(20)] for _ in range(20)]
        sl = choice(Level.Spawn_Loc)
        sl_x = sl[0]
        sl_y = sl[1]
        Level.Master_Level[sl_x][sl_y] = 'H'
        Hero.Player_Map[sl_x][sl_y] = 'H'

    def player_map(self):
        for rows in Level.Master_Level:
            print(rows)
        # for rows in Hero.Player_Map:
        #     print(' '.join(rows))

    def move_north(self):
        n_loc = []
        current_loc = Cave.find_location(lst=Level.Master_Level, tgt='H')
        n_loc_x = current_loc[0] - self.speed
        n_loc.append(n_loc_x)
        n_loc_y = current_loc[1]
        n_loc.append(n_loc_y)
        Level.Master_Level[current_loc[0]][current_loc[1]] = ' '
        Level.Master_Level[n_loc[0]][n_loc[1]] = 'H'
        Hero.Player_Map[current_loc[0]][current_loc[1]] = '*'
        Hero.Player_Map[n_loc[0]][n_loc[1]] = 'H'
        Hero.hero_listen()
        print("You move north one square.")
        if Cave.detect_collision(lst=Level.Wall_Loc, tgt=Cave.find_location(lst=Level.Master_Level, tgt='H')):
            Level.Master_Level[n_loc[0] + 1][n_loc[1]] = 'H'
            Level.Master_Level[n_loc[0]][n_loc[1]] = 'W'
            Hero.Player_Map[n_loc[0] + 1][n_loc[1]] = 'H'
            Hero.Player_Map[n_loc[0]][n_loc[1]] = 'W'
            print("You cannot move through a wall")

    def move_south(self):
        n_loc = []
        current_loc = Cave.find_location(lst=Level.Master_Level, tgt='H')
        n_loc_x = current_loc[0] + self.speed
        n_loc.append(n_loc_x)
        n_loc_y = current_loc[1]
        n_loc.append(n_loc_y)
        Level.Master_Level[current_loc[0]][current_loc[1]] = ' '
        Level.Master_Level[n_loc[0]][n_loc[1]] = 'H'
        Hero.Player_Map[current_loc[0]][current_loc[1]] = '*'
        Hero.Player_Map[n_loc[0]][n_loc[1]] = 'H'
        Hero.hero_listen()
        print("You move South one square.")
        if Cave.detect_collision(lst=Level.Wall_Loc, tgt=Cave.find_location(lst=Level.Master_Level, tgt='H')):
            Level.Master_Level[n_loc[0] - 1][n_loc[1]] = 'H'
            Level.Master_Level[n_loc[0]][n_loc[1]] = 'W'
            Hero.Player_Map[n_loc[0] - 1][n_loc[1]] = 'H'
            Hero.Player_Map[n_loc[0]][n_loc[1]] = 'W'
            print("You cannot move through a wall")

    def move_east(self):
        n_loc = []
        current_loc = Cave.find_location(lst=Level.Master_Level, tgt='H')
        n_loc_x = current_loc[0]
        n_loc.append(n_loc_x)
        n_loc_y = current_loc[1] + self.speed
        n_loc.append(n_loc_y)
        Level.Master_Level[current_loc[0]][current_loc[1]] = ' '
        Level.Master_Level[n_loc[0]][n_loc[1]] = 'H'
        Hero.Player_Map[current_loc[0]][current_loc[1]] = '*'
        Hero.Player_Map[n_loc[0]][n_loc[1]] = 'H'
        Hero.hero_listen()
        print("You move east one square.")
        if Cave.detect_collision(lst=Level.Wall_Loc, tgt=Cave.find_location(lst=Level.Master_Level, tgt='H')):
            Level.Master_Level[n_loc[0]][n_loc[1] - 1] = 'H'
            Level.Master_Level[n_loc[0]][n_loc[1]] = 'W'
            Hero.Player_Map[n_loc[0]][n_loc[1] - 1] = 'H'
            Hero.Player_Map[n_loc[0]][n_loc[1]] = 'W'
            print("You cannot move through a wall")

    def move_west(self):
        n_loc = []
        current_loc = Cave.find_location(lst=Level.Master_Level, tgt='H')
        n_loc_x = current_loc[0]
        n_loc.append(n_loc_x)
        n_loc_y = current_loc[1] - self.speed
        n_loc.append(n_loc_y)
        Level.Master_Level[current_loc[0]][current_loc[1]] = ' '
        Level.Master_Level[n_loc[0]][n_loc[1]] = 'H'
        Hero.Player_Map[current_loc[0]][current_loc[1]] = '*'
        Hero.Player_Map[n_loc[0]][n_loc[1]] = 'H'
        Hero.hero_listen()
        print("You move west one square.")
        if Cave.detect_collision(lst=Level.Wall_Loc, tgt=Cave.find_location(lst=Level.Master_Level, tgt='H')):
            Level.Master_Level[n_loc[0]][n_loc[1] + 1] = 'H'
            Level.Master_Level[n_loc[0]][n_loc[1]] = 'W'
            Hero.Player_Map[n_loc[0]][n_loc[1] + 1] = 'H'
            Hero.Player_Map[n_loc[0]][n_loc[1]] = 'W'
            print("You cannot move through a wall")

    @staticmethod
    def hero_listen():
        h = Cave.find_location(lst=Level.Master_Level, tgt='H')
        p_loc = [Cave.find_location(lst=Level.Master_Level, tgt='P')]
        #m_loc = [Cave.find_location(lst=Level.Master_Level, tgt='M')]
        m_loc = Level.MONSTER[0]
        row = h[0]
        col = h[1]
        listen_pit = [
            [row - 1, col],  # Top
            [row + 1, col],  # Bottom
            [row, col - 1],  # Left
            [row, col + 1],  # Right
        ]

        rowm = h[0]
        colm = h[1]
        listen_monster = [
            [rowm - 2, colm],  # Top
            [rowm + 2, colm],  # Bottom
            [rowm, colm - 2],  # Left
            [rowm, colm + 2],  # Right
            [row - 2, col - 2],  # Top-left
            [row - 2, col + 2],  # Top-right
            [row + 2, col - 2],  # Bottom-left
            [row + 2, col + 2],  # Bottom-right
        ]
        for x, y in enumerate(listen_pit):
            for a, b in enumerate(p_loc):
                if y == b:
                    print("You feel rush of wind as if you're standing on the ledge of something")
        for x, y in enumerate(listen_monster):
            for a, b in enumerate([m_loc]):
                if y == b:
                    print("You hear the snarl of a monster somewhere in the darkness.")

    @staticmethod
    def flash_light():
        h = Cave.find_location(lst=Level.Master_Level, tgt='H')
        t_loc = [Cave.find_location(lst=Level.Master_Level, tgt='T')]
        p_loc = [Cave.find_location(lst=Level.Master_Level, tgt='P')]
        row = h[0]
        col = h[1]
        flashlight = [
            [row - 1, col],  # Top
            [row + 1, col],  # Bottom
            [row, col - 1],  # Left
            [row, col + 1],  # Right
            [row - 1, col - 1],  # Top-left
            [row - 1, col + 1],  # Top-right
            [row + 1, col - 1],  # Bottom-left
            [row + 1, col + 1],  # Bottom-right
        ]
        for x, y in enumerate(flashlight):
            for a, b in enumerate(Level.Wall_Loc):
                if y == b:
                    Hero.Player_Map[b[0]][b[1]] = 'W'
        for x, y in enumerate(flashlight):
            for a, b in enumerate(p_loc):
                if y == b:
                    Hero.Player_Map[b[0]][b[1]] = 'P'
        for x, y in enumerate(flashlight):
            for a, b in enumerate(t_loc):
                if y == b:
                    Hero.Player_Map[b[0]][b[1]] = 'T'

    def hero_attack(self):

        h = Cave.find_location(lst=Level.Master_Level, tgt='H')
        spear_loc_x = h[0]
        spear_loc_y = h[1]
        #m_loc = [Cave.find_location(lst=Level.Master_Level, tgt='M')]
        #m_loc = Level.MONSTER
        direction = input("Which direction do you throw your spear? N, S, E, W ").upper()

        if direction == 'N':
            spear_loc = [spear_loc_x - 2, spear_loc_y]
            print(spear_loc)
            print(Level.MONSTER[0])
            if spear_loc == Level.MONSTER[0]:
                #Level.Master_Level[m_loc[0]][m_loc[1]] = ' '
                print("You throw your spear and slay the monster")
                Hero.SLAIN = True
                self.has_spear = False
            else:
                print("Your spear clangs off the cave floor. Its lost in the darkness")
                self.has_spear = False

        elif direction == 'S':
            spear_loc = [spear_loc_x + 2, spear_loc_y]
            if spear_loc == Level.MONSTER[0]:
                #Level.Master_Level[m_loc[0]][m_loc[1]] = ' '
                print("You throw your spear and slay the monster")
                Hero.SLAIN = True
                self.has_spear = False
            else:
                print("Your spear clangs off the cave floor. Its lost in the darkness")
                self.has_spear = False

        elif direction == 'E':
            spear_loc = [spear_loc_x, spear_loc_y + 2]
            if spear_loc == Level.MONSTER[0]:
                #Level.Master_Level[m_loc[0]][m_loc[1]] = ' '
                print("You throw your spear and slay the monster")
                Hero.SLAIN = True
                self.has_spear = False
            else:
                print("Your spear clangs off the cave floor. Its lost in the darkness")
                self.has_spear = False

        elif direction == 'W':
            spear_loc = [spear_loc_x, spear_loc_y - 2]
            if spear_loc == Level.MONSTER[0]:
                #Level.Master_Level[m_loc[0]][m_loc[1]] = ' '
                print("You throw your spear and slay the monster")
                Hero.SLAIN = True
                self.has_spear = False
            else:
                print("Your spear clangs off the cave floor. Its lost in the darkness")
                self.has_spear = False

        else:
            print("You did not enter a valid direction")


