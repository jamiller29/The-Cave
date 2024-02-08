# IMPORT STATEMENTS
from level import Level
from random import choice


class Hero:
    # Class Variables
    Player_Map = Level.Master_Level

    def __init__(self):
        self.speed = 1
        self.flashlight = 1
        self.attack_range = 2
        self.has_spear = True

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
        # Hero.Player_Map[hero_location_x][hero_location_y] = 'H'

    @staticmethod
    def player_map():
        # for rows in Level.Master_Level:
        #     print(rows)
        for rows in Hero.Player_Map:
            print(' '.join(rows))

    @staticmethod
    def update_map(new_location, c_loc):
        Level.Master_Level[c_loc[0][0]][c_loc[0][1]] = ' '
        Level.Master_Level[new_location[0][0]][new_location[0][1]] = 'H'

    @staticmethod
    def listen():
        hero_location = []
        Level.find_position(Level.Master_Level, hero_location, 'H')
        listen_for_monster = []
        listen_for_pit = []
        Level.dmz(hero_location[0][0], hero_location[0][1], Level.Master_Level, listen_for_monster, 3)
        Level.dmz(hero_location[0][0], hero_location[0][1], Level.Master_Level, listen_for_pit, 2)
        for a,b in enumerate(listen_for_pit):
            for c,d in enumerate(Level.PIT):
                if b == d:
                    print("You hear a howl of wind and feel it against your face as if your standing on the ledge of "
                          "something.")
        for a,b in enumerate(listen_for_monster):
            for c,d in enumerate(Level.MONSTER):
                if b == d:
                    print("You hear the snarl of a monster somewhere in the darkness.")
        # print(listen_for_pit)
        # print(listen_for_monster)
    def move(self):
        current_hero_location = []
        new_hero_location = []
        Level.find_position(Level.Master_Level, current_hero_location, 'H')
        direction = input("What direction do you move? N, S, E, or W: ").upper()

        if direction == 'N':
            new_hero_location_x = current_hero_location[0][0] - self.speed
            new_hero_location_y = current_hero_location[0][1]
            new_hero_location.append([new_hero_location_x, new_hero_location_y])
            Hero.update_map(new_hero_location, current_hero_location)
            Hero.listen()
            print("You move to the North.")
            if Level.detect_collision(Level.Wall_Loc, new_hero_location):
                Level.Master_Level[new_hero_location[0][0] + self.speed][new_hero_location[0][1]] = 'H'
                Level.Master_Level[new_hero_location[0][0]][new_hero_location[0][1]] = 'W'
                print("You walked into a wall!")

        elif direction == 'S':
            new_hero_location_x = current_hero_location[0][0] + self.speed
            new_hero_location_y = current_hero_location[0][1]
            new_hero_location.append([new_hero_location_x, new_hero_location_y])
            Hero.update_map(new_hero_location, current_hero_location)
            Hero.listen()
            print("You move to the South.")
            if Level.detect_collision(Level.Wall_Loc, new_hero_location):
                Level.Master_Level[new_hero_location[0][0] - self.speed][new_hero_location[0][1]] = 'H'
                Level.Master_Level[new_hero_location[0][0]][new_hero_location[0][1]] = 'W'
                print("You walked into a wall!")

        elif direction == 'E':
            new_hero_location_x = current_hero_location[0][0]
            new_hero_location_y = current_hero_location[0][1] + self.speed
            new_hero_location.append([new_hero_location_x, new_hero_location_y])
            Hero.update_map(new_hero_location, current_hero_location)
            Hero.listen()
            print("You move to the East.")
            if Level.detect_collision(Level.Wall_Loc, new_hero_location):
                Level.Master_Level[new_hero_location[0][0]][new_hero_location[0][1] - self.speed] = 'H'
                Level.Master_Level[new_hero_location[0][0]][new_hero_location[0][1]] = 'W'
                print("You walked into a wall!")

        elif direction == 'W':
            new_hero_location_x = current_hero_location[0][0]
            new_hero_location_y = current_hero_location[0][1] - self.speed
            new_hero_location.append([new_hero_location_x, new_hero_location_y])
            Hero.update_map(new_hero_location, current_hero_location)
            Hero.listen()
            print("You move to the West.")
            if Level.detect_collision(Level.Wall_Loc, new_hero_location):
                Level.Master_Level[new_hero_location[0][0]][new_hero_location[0][1] + self.speed] = 'H'
                Level.Master_Level[new_hero_location[0][0]][new_hero_location[0][1]] = 'W'
                print("You walked into a wall!")

        else:
            print("You did not enter a valid direction")
