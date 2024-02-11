"""
BUGS: Once The Monster is killed and move the program looks for the monster and its not there
crashing the program. I can still hear the monster when its killed. can move into its killbox and
not die
- Possible fix would be to make hero immune to monster
Error Handling for incorrect input

"""

# IMPORT STATEMENTS
import pyfiglet
# from os import system
import PySimpleGUI as psg
from level import Level
from hero import Hero
from replit import clear

# CREATING CLASS Objects
level = Level()
hero = Hero()

# GLOBAL VARIABLES


# Import Game File pop-up
print(pyfiglet.figlet_format("The Cave", font='slant'))
select_file = psg.popup_get_file('Select a File', title='File Selector')

# Initialize Game Files
level.load_level(select_file)
Level.find_position(Level.Master_Level, Level.Wall_Loc, 'W')
Level.find_position(Level.Master_Level, Level.Spawn_Loc, 'E')
Level.find_position(Level.Master_Level, Level.MONSTER, 'M')
Level.find_position(Level.Master_Level, Level.TREASURE, 'T')
Level.find_position(Level.Master_Level, Level.PIT, 'P')
hero.gen_player_map()
hero.gen_player_map_x()
hero.spawn_hero()
level.spawn_compas()


# TEST CODE HERE
compas_loc = []
Level.find_position(Level.Master_Level, compas_loc, 'C')
print(compas_loc)

# Main Game Loop
def main():
    game_status = True
    while game_status:
        while True:
            action = input("1. Move\n2. Look at map\n3. Use Compas\n4. Attack\n5. Give Up.\nAction: ")
            if action in ['1', '2', '3', '4', '5']:
                break
            else:
                print('You did not enter a valid action')
        if action == '1':
            while True:
                direction = input('What direction do you want to move? N, S, E, or W: ').upper()
                if direction in ['N', 'S', 'E', 'W']:
                    break
                else:
                    print('You did not enter a valid direction.')
            hero.move(d=direction)
            hero.win_conditions()
            if not Hero.GAME_STATUS:
                game_status = False

        elif action == '2':
            if hero.dm_map:
                Hero.player_map_visible()
            else:
                print("You do not have a map.")
        elif action == '3':
            if hero.has_compas:
                Hero.compas()
            else:
                print("You do not have a compas.")
        elif action == '4':
            if hero.has_spear:
                hero.attack()
            else:
                print("You do not have a spear.")
        elif action == '5':
            game_status = False


if __name__ == '__main__':
    main()
