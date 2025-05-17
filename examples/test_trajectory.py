from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import time
from scipy.spatial.transform import Rotation as R

client = RemoteAPIClient()
sim = client.require('sim')
sim.setStepping(True)

way_1 = sim.getObject(':/way_1')
way_2 = sim.getObject(':/way_2')
target = sim.getObject(':/Target')
center = sim.getObject(':/Center')

num_points = 100
delay = 0.05

# Get dummy positions
pos_1 = np.array(sim.getObjectPosition(way_1, -1))
pos_2 = np.array(sim.getObjectPosition(way_2, -1))
center = np.array(sim.getObjectPosition(center, -1))

# === OFFLINE TRAJECTORY CALCULATION ===
# center = (pos_1 + pos_2) / 2 --> u can use the center of ur sphere. 
radius = np.linalg.norm(pos_1 - center)

# circular plane
v1 = (pos_1 - center)
v1 /= np.linalg.norm(v1)
normal = np.cross(v1, [0, 0, 1])
if np.linalg.norm(normal) < 1e-6:
    normal = np.array([0, 1, 0])
normal /= np.linalg.norm(normal)
v2 = np.cross(normal, v1)

trajectory = []  # (position, orientation)

for i in range(num_points):
    angle = 2 * np.pi * i / num_points
    point = center + radius * (np.cos(angle) * v1 + np.sin(angle) * v2)

    # Orientation: Z axis points ALWAYS to center
    z_axis = center - point
    z_axis /= np.linalg.norm(z_axis)
    x_axis = np.cross([0, 1, 0], z_axis)
    if np.linalg.norm(x_axis) < 1e-6:
        x_axis = np.cross([1, 0, 0], z_axis)
    x_axis /= np.linalg.norm(x_axis)
    y_axis = np.cross(z_axis, x_axis)

    rot_matrix = np.column_stack((x_axis, y_axis, z_axis))
    quat = R.from_matrix(rot_matrix).as_quat()
    
    trajectory.append((point.tolist(), quat.tolist()))

# === ONLINE EXECUTION ===
sim.startSimulation()

for point, quat in trajectory:
    sim.setObjectPosition(target, -1, point)
    sim.setObjectQuaternion(target, -1, quat)
    sim.step()

sim.stopSimulation()
