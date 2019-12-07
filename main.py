from Visualisation import *
from Simulator import *
import time

# Configuratie
VISUALISATION=True
PATTERN = "B31/S23"

if __name__ == "__main__":
    w = World(110)
    sim = Simulator(PATTERN, w)

    if VISUALISATION:
        vis = Visualisation(sim)
    else:
        while True:
            # Create new world and print to screen
            print(sim.update())
            # slow down simulation
            time.sleep(0.5)