class Level:
    # Class Variables
    Master_Level = []
    Wall_Loc = []
    Spawn_Loc = []
    TREASURE = []
    PIT = []
    MONSTER = []

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

        # Generate a list of all wall locations.
        for i, sublist in enumerate(Level.Master_Level):
            for j, element in enumerate(sublist):
                if element == 'W':
                    Level.Wall_Loc.append([i, j])

        # Generate a list of all possible spawn locations.
        for i, sublist in enumerate(Level.Master_Level):
            for j, element in enumerate(sublist):
                if element == 'E':
                    Level.Spawn_Loc.append([i, j])

        # Generate the treasure location and saves it to a list
        for i, sublist in enumerate(Level.Master_Level):
            for j, element in enumerate(sublist):
                if element == 'T':
                    Level.TREASURE.append([i, j])

        # Generate the pit location and saves it to a list
        for i, sublist in enumerate(Level.Master_Level):
            for j, element in enumerate(sublist):
                if element == 'P':
                    Level.PIT.append([i, j])

        # Generate the monster location and saves it to a list
        for i, sublist in enumerate(Level.Master_Level):
            for j, element in enumerate(sublist):
                if element == 'M':
                    Level.MONSTER.append([i, j])
