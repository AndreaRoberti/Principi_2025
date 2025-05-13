from coppeliasim_zmqremoteapi_client import RemoteAPIClient
from PandaRobot import *

import matplotlib.pyplot as plt
import numpy as np

# Python examples 
# https://github.com/CoppeliaRobotics/zmqRemoteApi/tree/master/clients/python 

client = RemoteAPIClient()
sim = client.require('sim')

panda = PandaRobot(client, "Franka")

red_ring = sim.getObject(':/Red_ring')


panda.startSimulation()

while (t := panda.simulationTime()) < 5:
    # print(f'Simulation time: {t:.2f} [s]')

    position_red_ring = sim.getObjectPosition(red_ring, sim.handle_world)
    print(position_red_ring)

    panda.getStatus()

    panda.stepSimulation()

panda.stopSimulation()