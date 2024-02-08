"""
BUGS: Once The Monster is killed and move the program looks for the monster and its not there
crashing the program. I can still hear the monster when its killed. can move into its killbox and
not die
- Possible fix would be to make hero immune to monster
Error Handling for incorrect input

"""

# IMPORT STATEMENTS
import pyfiglet
from os import system
import PySimpleGUI as psg
from level import Level
from hero import Hero


# CREATING CLASS Objects
level = Level()
hero = Hero()

# GLOBAL VARIABLES
GAME_ON = True

# Import Game File pop-up
print(pyfiglet.figlet_format("The Cave", font='slant'))
select_file = psg.popup_get_file('Select a File', title='File Selector')

# Initialize Game Files
level.load_level(select_file)
hero.spawn_hero()


# TEST CODE HERE


# Main Game Loop
def main(game_status):
    while game_status:
        action = int(
            input("Choose your action.  \n 1. Move \n 2. Attack \n 3. Use Flashlight \n 4. Give up\n "
                  "Action: "))
        if action == 1:
            direction = input("Which direction do you move? N, S, E, W or C for Cancel Move: ").upper()
            system('cls')
            if direction == 'N':
                hero.move_north()
                if Cave.win_conditions():
                    game_status = False
                hero.player_map()
            elif direction == 'S':
                hero.move_south()
                if Cave.win_conditions():
                    game_status = False
                hero.player_map()
            elif direction == 'E':
                hero.move_east()
                if Cave.win_conditions():
                    game_status = False
                hero.player_map()
            elif direction == 'W':
                hero.move_west()
                if Cave.win_conditions():
                    game_status = False
                hero.player_map()
            elif direction == 'C':
                continue
            else:
                print("You did not enter a valid direction.")

        elif action == 2:
            if hero.has_spear:
                hero.hero_attack()
                hero.player_map()
            else:
                print("You no longer have a spear.")

        elif action == 3:
            Hero.flash_light()
            hero.player_map()

        elif action == 4:
            game_status = False

        else:
            print("You did not enter a valid action.")


if __name__ == '__main__':
    main(game_status=GAME_ON)
