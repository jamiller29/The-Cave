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
GAME_STATUS = True

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
hero.spawn_hero()


# TEST CODE HERE


# Main Game Loop
def main(game_on):
    while game_on:
        clear()
        action = int(input("Choose your action.  \n 1. Move \n 2. Attack \n 3. Give Up\n "
                           "Action: "))
        if action == 1:
            direction = input("What direction do you move? N, S, E, or W: ").upper()
            hero.move(d=direction)
        elif action == 2:
            Hero.dm_map()
        elif action == 3:
            # choice = input("Would you like to save your game? Y or N: ").upper()
            # if choice == 'Y':
            #     save_game_as = input("Save Game As? All one word: ").lower()
            #     level.write_level(Level.Master_Level, save_game_as)
            game_on = False


if __name__ == '__main__':
    main(game_on=GAME_STATUS)
