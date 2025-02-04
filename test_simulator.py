from unittest import TestCase
from Simulator import *
from World import *
import numpy as np


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """
    def setUp(self):
        self.sim = Simulator()

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        input = np.array([[0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,1,1,1,0,0,0],
                          [0,0,0,0,1,0,1,0,0,0],
                          [0,0,0,0,1,1,1,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0]])

        expecpted_output = np.array([[0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,5,5,5,5,5,0,0],
                                     [0,0,0,5,4,4,4,5,0,0],
                                     [0,0,0,5,4,0,4,5,0,0],
                                     [0,0,0,5,4,4,4,5,0,0],
                                     [0,0,0,5,5,5,5,5,0,0],
                                     [0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0]])

        world = World(10)
        world.world = input

        self.sim.set_pattern("B123/S123/A5")

        self.sim.set_world(world)
        update = self.sim.update()

        self.assertEquals(expecpted_output.all(), update.world.all())

    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)
