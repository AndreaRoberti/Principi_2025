from coppeliasim_zmqremoteapi_client import RemoteAPIClient

client = RemoteAPIClient()
sim = client.require('sim')

sim.setStepping(True)


sphere = sim.getObject(':/Sphere')

sim.startSimulation()

sim.setObjectPosition(sphere, [0.3,-0.2,1.0], sim.handle_world)

while (t := sim.getSimulationTime()) < 15:
    # print(f'Simulation time: {t:.2f} [s]')

    position_sphere = sim.getObjectPosition(sphere, sim.handle_world)
    print(position_sphere)



    sim.step()
sim.stopSimulation()