from coppeliasim_zmqremoteapi_client import RemoteAPIClient
from UR5Robot import *

import matplotlib.pyplot as plt
import numpy as np

# Python examples 
# https://github.com/CoppeliaRobotics/zmqRemoteApi/tree/master/clients/python 

client = RemoteAPIClient()

ur5 = UR5Robot(client, "UR5")

ur5.startSimulation()

while (t := ur5.simulationTime()) < 15:
    print(f'Simulation time: {t:.2f} [s]')

    ur5.getStatus()

    ur5.stepSimulation()

ur5.stopSimulation()