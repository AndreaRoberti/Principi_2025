from coppeliasim_zmqremoteapi_client import RemoteAPIClient
from PandaRobot import *

import matplotlib.pyplot as plt
import numpy as np

# Python examples 
# https://github.com/CoppeliaRobotics/zmqRemoteApi/tree/master/clients/python 

client = RemoteAPIClient()

panda = PandaRobot(client, "Panda")

panda.startSimulation()



# Parameters
T_total = 10   # Total trajectory duration
t_acc = 2      # Acceleration time
t_flat = 5     # Constant velocity time
t_dec = 3      # Deceleration time
v_max = 2      # Maximum velocity

# Time vector
t = np.linspace(0, T_total, 1000)

# Compute velocity trajectory
velocity = panda.trapezoidal_trajectory(t, t_acc, t_flat, t_dec, v_max)

# Plotting
# plt.figure(figsize=(8, 4))
# plt.plot(t, velocity, label="Trapezoidal Velocity Profile", color="b")
# plt.xlabel("Time [s]")
# plt.ylabel("Velocity [m/s]")
# plt.title("Trapezoidal Trajectory")
# plt.legend()
# plt.grid()
# plt.show()



while (t := panda.simulationTime()) < 5:
    print(f'Simulation time: {t:.2f} [s]')

    panda.getStatus()

    panda.stepSimulation()

panda.stopSimulation()