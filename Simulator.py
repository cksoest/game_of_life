from World import *

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, pattern=None, world=None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.first_run = True
        self.generation = 0
        if pattern == None:
            self.pattern = "B3/S23"
        else:
            self.pattern = pattern
        if world == None:
            self.world = World(20)
        else:
            self.world = world

    @staticmethod
    def count_living_cells(neigbours):
        living_cells = 0
        for i in neigbours:
            if i > 0:
                living_cells = living_cells + 1
        return living_cells

    def apply_rules(self, x, y, new_world, cell, amount_living_cells):
        bsa = self.pattern_to_numbers()
        change_check = True

        for num in bsa[0]:
            if (cell == 0) and (amount_living_cells == num):
                new_world.set(x, y, bsa[2])
                change_check = False
                break

        for num in bsa[1]:
            if (cell == 1) and (amount_living_cells == num):
                new_world.set(x, y, self.world.get(x,y))
                change_check = False
                break

        if change_check:
            old_value = self.world.get(x, y)
            if old_value == 0:
                new_world.set(x, y, old_value)
            else:
                new_world.set(x, y, old_value-1)
        return new_world

    def pattern_to_numbers(self):
        b, s, a = [], [], 1
        splitted = self.pattern.split(sep="/")

        loop_times = 0
        if len(splitted) == 2:
            loop_times = 2
        if len(splitted) == 3:
            loop_times = 3

        for i in range(loop_times):
            for char in splitted[i]:
                if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    if i == 0:
                        b.append(int(char))
                    elif i == 1:
                        s.append(int(char))
                    elif i == 2:
                        a = int(char)
        return b, s, a

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1
        if self.first_run:
            a = self.pattern_to_numbers()[2]
            for y in range(self.world.width):
                for x in range(self.world.height):
                    if self.world.get(x,y) > 0:
                        self.world.set(x, y, a)
            self.first_run = False

        new_world = World(self.world.width, self.world.height)
        for y in range(self.world.width):
            for x in range(self.world.height):
                neighbours = self.world.get_neighbours(x, y)
                cell = self.world.get(x, y)
                amount_living_cells = self.count_living_cells(neighbours)
                new_world = self.apply_rules(x, y, new_world, cell, amount_living_cells)
        self.world = new_world
        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world

    def set_pattern(self, pattern):
        self.pattern = pattern

    def get_patern(self):
        return self.pattern
