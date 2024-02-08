# IMPORT STATEMENTS
from level import Level
from random import choice


class Hero:
    # Class Variables
    Player_Map = []

    def __init__(self):
        self.speed = 1
        self.flashlight = 1
        self.attack_range = 2
        self.has_spear = True

    @staticmethod
    def spawn_hero():  # Randomly Spawn the Hero
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

    @staticmethod
    def update_map(c_loc, n_loc):
        Level.Master_Level[c_loc[0]][c_loc[1]] = ' '
        Level.Master_Level[n_loc[0]][n_loc[1]] = 'H'
        Hero.Player_Map[c_loc[0]][c_loc[1]] = '*'
        Hero.Player_Map[n_loc[0]][n_loc[1]] = 'H'


    def wall_collision(self, direc, n_loc):
        if Level.detect_collision(Level.Master_Level, 'H'):
            if direc == 'N':
                Level.Master_Level[n_loc[0] + self.speed][n_loc[1]] = 'H'
                Level.Master_Level[n_loc[0]][n_loc[1]] = 'W'
                Hero.Player_Map[n_loc[0] + self.speed][n_loc[1]] = 'H'
                Hero.Player_Map[n_loc[0]][n_loc[1]] = 'W'
                print("You cannot move through a wall!")
            elif direc == 'S':
                Level.Master_Level[n_loc[0] - self.speed][n_loc[1]] = 'H'
                Level.Master_Level[n_loc[0]][n_loc[1]] = 'W'
                Hero.Player_Map[n_loc[0] - self.speed][n_loc[1]] = 'H'
                Hero.Player_Map[n_loc[0]][n_loc[1]] = 'W'
                print("You cannot move through a wall!")
            elif direc == 'E':
                Level.Master_Level[n_loc[0]][n_loc[1] - self.speed] = 'H'
                Level.Master_Level[n_loc[0]][n_loc[1]] = 'W'
                Hero.Player_Map[n_loc[0]][n_loc[1] - self.speed] = 'H'
                Hero.Player_Map[n_loc[0]][n_loc[1]] = 'W'
                print("You cannot move through a wall!")
            else: # West
                Level.Master_Level[n_loc[0]][n_loc[1] + self.speed] = 'H'
                Level.Master_Level[n_loc[0]][n_loc[1]] = 'W'
                Hero.Player_Map[n_loc[0]][n_loc[1] + self.speed] = 'H'
                Hero.Player_Map[n_loc[0]][n_loc[1]] = 'W'
                print("You cannot move through a wall!")



    @staticmethod
    def listen():
        h_loc = []
        p_loc = []
        m_loc = []
        listen_for_monster = []
        listen_for_pit = []
        Level.find_position(Level.Master_Level, h_loc, 'H')
        Level.find_position(Level.Master_Level, p_loc, 'P')
        Level.find_position(Level.Master_Level, m_loc, 'M')
        Level.dmz(row=h_loc[0][0], col=[0][1], lst=Level.Master_Level, out_put_lst=listen_for_pit, no_spawn_range=2)
        Level.dmz(row=h_loc[0][0], col=[0][1], lst=Level.Master_Level, out_put_lst=listen_for_monster, no_spawn_range=3)
        for x, y in enumerate(listen_for_pit):
            for i, j in enumerate(p_loc):
                if y == j:
                    print("You feel rush of wind as if you're standing on the ledge of something")
        for a, b in enumerate(listen_for_monster):
            for c, d in enumerate(m_loc):
                if b == d:
                    print("You hear the snarl of a monster somewhere in the darkness.")

    def hero_move(self):
        direction = input("Which direction do you move? N, S, E, W:  ").upper()
        n_loc = []
        current_loc = []
        Level.find_position(Level.Master_Level, current_loc, 'H')
        if direction == 'N':
            n_loc_x = current_loc[0] - self.speed
            n_loc_y = current_loc[1]
            n_loc.append(n_loc_x)
            n_loc.append(n_loc_y)
            Hero.listen()
            Hero.update_map(current_loc, n_loc)
            Hero.wall_collision(direc=direction, n_loc=n_loc)
        elif direction == 'S':
            n_loc_x = current_loc[0] + self.speed
            n_loc_y = current_loc[1]
            n_loc.append(n_loc_x)
            n_loc.append(n_loc_y)
            Hero.listen()
            Hero.update_map(current_loc, n_loc)
            Hero.wall_collision(direc=direction, n_loc=n_loc)
        elif direction == 'E':
            n_loc_x = current_loc[0]
            n_loc_y = current_loc[1] + self.speed
            n_loc.append(n_loc_x)
            n_loc.append(n_loc_y)
            Hero.listen()
            Hero.update_map(current_loc, n_loc)
            Hero.wall_collision(direc=direction, n_loc=n_loc)
        elif direction == 'W':
            n_loc_x = current_loc[0]
            n_loc_y = current_loc[1] - self.speed
            n_loc.append(n_loc_x)
            n_loc.append(n_loc_y)
            Hero.listen()
            Hero.update_map(current_loc, n_loc)
            Hero.wall_collision(direc=direction, n_loc=n_loc)
        else:
            print('You entered an invalid direction.')
