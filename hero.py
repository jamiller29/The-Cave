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

    def gen_player_map(self):
        for _ in range(20):
            row = []
            for _ in range(20):
                row.append(' ')
            Hero.Player_Map.append(row)

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

    @staticmethod
    def player_map():
        for row in Hero.Player_Map:
            print(' '.join(row))

    @staticmethod
    def dm_map():
        for row in Level.Master_Level:
            print(' '.join(row))

    @staticmethod
    def listen():
        hero_location = []
        Level.find_position(Level.Master_Level, hero_location, 'H')
        listen_for_monster = []
        listen_for_pit = []
        Level.dmz(hero_location[0][0], hero_location[0][1], Level.Master_Level, listen_for_monster, 3)
        Level.dmz(hero_location[0][0], hero_location[0][1], Level.Master_Level, listen_for_pit, 2)
        for a, b in enumerate(listen_for_pit):
            for c, d in enumerate(Level.PIT):
                if b == d:
                    print("You hear a howl of wind and feel it against your face as if your standing on the ledge of "
                          "something.")
        for a, b in enumerate(listen_for_monster):
            for c, d in enumerate(Level.MONSTER):
                if b == d:
                    print("You hear the snarl of a monster somewhere in the darkness.")

    @staticmethod
    def torch():
        hero_location = []
        flashlight = []
        Level.find_position(Level.Master_Level, hero_location, "H")
        Level.dmz(row=hero_location[0][0], col=hero_location[0][1], lst=Level.Master_Level, out_put_lst=flashlight,
                  no_spawn_range=2)
        for x, y in enumerate(flashlight):
            for a, b in enumerate(Level.Wall_Loc):
                if y == b:
                    Hero.Player_Map[b[0]][b[1]] = 'W'
                else:
                    Hero.Player_Map[b[0]][b[1]] = ' '

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
        Hero.Player_Map[current_hero_location[0][0]][current_hero_location[0][1]] = '*'
        Hero.wall_collision(self, direction=d)
        Hero.listen()
        Hero.player_map()
