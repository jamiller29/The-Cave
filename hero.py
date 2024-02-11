# IMPORT STATEMENTS
from level import Level
from random import choice
import pyfiglet


class Hero:
    # Class Variables
    Player_Map = []
    Player_Map_visible = []
    GAME_STATUS = True

    def __init__(self):
        self.speed = 1
        self.attack_range = 2
        self.has_spear = True
        self.has_compas = True
        self.has_map = True
        self.monster_slain = False


    def gen_player_map(self):
        for _ in range(20):
            row = []
            for _ in range(20):
                row.append(' ')
            Hero.Player_Map.append(row)

    def gen_player_map_x(self):
        for _ in range(20):
            row = []
            for _ in range(20):
                row.append(' ')
            Hero.Player_Map_visible.append(row)

    @staticmethod
    def spawn_hero():  # Randomly Spawn the Hero
        pass
        level_dmz = []
        monster_dmz = []
        pit_dmz = []
        treasure_dmz = []
        Level.dmz(Level.MONSTER[0][0], Level.MONSTER[0][1], Level.Master_Level, monster_dmz, 3)
        Level.dmz(Level.PIT[0][0], Level.PIT[0][1], Level.Master_Level, pit_dmz, 2)
        Level.dmz(Level.TREASURE[0][0], Level.TREASURE[0][1], Level.Master_Level, treasure_dmz, 2)
        level_dmz = monster_dmz + treasure_dmz + treasure_dmz
        for x, y in enumerate(level_dmz):
            for a, b in enumerate(Level.Spawn_Loc):
                if y == b:
                    Level.Spawn_Loc.remove(y)
        hero_location = choice(Level.Spawn_Loc)
        hero_location_x = hero_location[0]
        hero_location_y = hero_location[1]
        Level.Master_Level[hero_location_x][hero_location_y] = 'H'
        Hero.Player_Map[hero_location[0]][hero_location[1]] = 'H'
        Hero.Player_Map_visible[hero_location[0]][hero_location[1]] = 'H'

    @staticmethod
    def player_map():
        for row in Hero.Player_Map:
            print(' '.join(row))

    @staticmethod
    def player_map_visible():
        for row in Hero.Player_Map_visible:
            print(' '.join(row))

    @staticmethod
    def dm_map():
        for row in Level.Master_Level:
            print(' '.join(row))

    @staticmethod
    def compas():
        treasure_location = Level.MONSTER
        hero_location = []
        Level.find_position(Level.Master_Level, hero_location, 'H')
        print(f'Your location: {hero_location[0]}, Treasure Location: {treasure_location[0]}')

    def listen(self):
        hero_location = []
        Level.find_position(Level.Master_Level, hero_location, 'H')
        listen_for_monster = []
        listen_for_pit = []
        Level.dmz(hero_location[0][0], hero_location[0][1], Level.Master_Level, listen_for_monster, 2)
        Level.dmz(hero_location[0][0], hero_location[0][1], Level.Master_Level, listen_for_pit, 1)
        for a, b in enumerate(listen_for_pit):
            for c, d in enumerate(Level.PIT):
                if b == d:
                    print("You hear a howl of wind and feel it against your face as if your standing on the ledge of "
                          "something.")
        if not self.monster_slain:
            for a, b in enumerate(listen_for_monster):
                for c, d in enumerate(Level.MONSTER):
                    if b == d:
                        print("You hear the snarl of a monster somewhere in the darkness.")

    @staticmethod
    def torch():
        hero_location = []
        visible = []
        Level.find_position(Level.Master_Level, hero_location, 'H')
        Level.dmz(hero_location[0][0], hero_location[0][1], Level.Master_Level, visible, 1)

        for a, b in enumerate(Hero.Player_Map):
            for c, d in enumerate(b):
                if d in ['W', 'T', 'P']:
                    Hero.Player_Map[a][c] = ' '

        for a, b in enumerate(visible):
            for c, d in enumerate(Level.Wall_Loc):
                if b == d:
                    Hero.Player_Map[b[0]][b[1]] = 'W'
                    Hero.Player_Map_visible[b[0]][b[1]] = 'W'

        for a, b in enumerate(visible):
            for c, d in enumerate(Level.TREASURE):
                if b == d:
                    Hero.Player_Map[b[0]][b[1]] = 'T'
                    Hero.Player_Map_visible[b[0]][b[1]] = 'T'

        # for a, b in enumerate(visible):
        #     for c, d in enumerate(Level.PIT):
        #         if b == d:
        #             Hero.Player_Map[b[0]][b[1]] = 'P'
        #             Hero.Player_Map_visible[b[0]][b[1]] = 'P'

    def attack(self):
        spear_location = []
        new_spear_location = []
        Level.find_position(Level.Master_Level, spear_location, 'H')
        direction = input("Which way do you throw your spear? N, S, E, or W,: ").upper()

        throw_spear = {
            'N': [-self.attack_range, 0],
            'S': [self.attack_range, 0],
            'E': [0, self.attack_range],
            'W': [0, self.attack_range],
        }

        if direction in throw_spear:
            row_adj, col_adj = throw_spear[direction]
            spear_location[0][0] += row_adj
            spear_location[0][1] += col_adj

        if Level.detect_collision(Level.MONSTER, spear_location):
            print("You throw your spear. It slays the Monster!")
            Level.Master_Level[Level.MONSTER[0][0]][Level.MONSTER[0][1]] = 'E'
            self.has_spear = False
            self.monster_slain = True
        else:
            print("You throw your spear it clangs of the cave floor and is lost in the darkness.")
            self.has_spear = False

    def wall_collision(self, direction):
        current_hero_location = []
        Level.find_position(Level.Master_Level, current_hero_location, 'H')
        if Level.detect_collision(Level.Wall_Loc, current_hero_location):
            print("You ran into a wall!")
            row_adj, col_adj = {
                'N': [self.speed, 0],
                'S': [-self.speed, 0],
                'E': [0, -self.speed],
                'W': [0, self.speed],
            }.get(direction)

            Level.Master_Level[current_hero_location[0][0] + row_adj][current_hero_location[0][1] + col_adj] = 'H'
            Level.Master_Level[current_hero_location[0][0]][current_hero_location[0][1]] = 'W'
            Hero.Player_Map[current_hero_location[0][0] + row_adj][current_hero_location[0][1] + col_adj] = 'H'
            Hero.Player_Map[current_hero_location[0][0]][current_hero_location[0][1]] = 'W'

    def move(self, d):
        current_hero_location = []
        Level.find_position(Level.Master_Level, current_hero_location, 'H')
        row_adj, col_adj = {
            'N': [-self.speed, 0],
            'S': [self.speed, 0],
            'E': [0, self.speed],
            'W': [0, -self.speed],
        }.get(d)

        Level.Master_Level[current_hero_location[0][0] + row_adj][current_hero_location[0][1] + col_adj] = 'H'
        Level.Master_Level[current_hero_location[0][0]][current_hero_location[0][1]] = ' '
        Hero.Player_Map[current_hero_location[0][0] + row_adj][current_hero_location[0][1] + col_adj] = 'H'
        Hero.Player_Map[current_hero_location[0][0]][current_hero_location[0][1]] = ' '
        Hero.Player_Map_visible[current_hero_location[0][0] + row_adj][current_hero_location[0][1] + col_adj] = 'H'
        Hero.Player_Map_visible[current_hero_location[0][0]][current_hero_location[0][1]] = '*'
        Hero.wall_collision(self, direction=d)
        Hero.listen(self)
        Hero.torch()
        Hero.player_map()
        #Level.win_conditions(self)

    def win_conditions(self):
        h_loc = []
        monster_kill_box = []
        Level.dmz(Level.MONSTER[0][0], Level.MONSTER[0][1], Level.Master_Level, monster_kill_box, 1)
        Level.find_position(Level.Master_Level, h_loc, 'H')
        if h_loc == Level.TREASURE:
            print("You found the Treasure!")
            print(print(pyfiglet.figlet_format("You Win", font='slant')))
            Hero.GAME_STATUS = False
            return Hero.GAME_STATUS
        elif h_loc == Level.PIT:
            print("You fell in a pit")
            print(print(pyfiglet.figlet_format("GAME OVER", font='slant')))
            Hero.GAME_STATUS = False
            return Hero.GAME_STATUS
        elif not self.monster_slain:
            if Level.detect_collision(monster_kill_box, h_loc):
                print("The Monster Found You!")
                print(print(pyfiglet.figlet_format("GAME OVER", font='slant')))
                Hero.GAME_STATUS = False




