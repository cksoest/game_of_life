from World import *

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world

    @staticmethod
    def count_living_cells(neigbours):
        living_cells = 0
        for i in neigbours:
            if i == 1:
                living_cells = living_cells + 1
        return living_cells

    @staticmethod
    def apply_rules(x, y, new_world, cell, amount_living_cells):
        if (cell == 1) and (amount_living_cells == 2):
            new_world.set(x, y, 1)
        elif (cell == 1) and (amount_living_cells == 3):
            new_world.set(x, y, 1)
        elif (cell == 0) and (amount_living_cells == 3):
            new_world.set(x, y, 1)
        else:
            new_world.set(x, y, 0)

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1
        new_world = World(self.world.width, self.world.height)
        for y in range(self.world.width):
            for x in range(self.world.height):
                neighbours = self.world.get_neighbours(x, y)
                cell = self.world.get(x, y)
                amaount_living_cells = self.count_living_cells(neighbours)
                self.apply_rules(x, y, new_world, cell, amaount_living_cells)
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