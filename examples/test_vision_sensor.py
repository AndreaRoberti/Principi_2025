from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import cv2

client = RemoteAPIClient()
sim = client.require('sim')
simIM = client.require('simIM')

sim.setStepping(True)


rgbVisionSensor=sim.getObject('/camera_color_optical_frame')

sim.startSimulation()

while (t := sim.getSimulationTime()) < 3:
    img, [resX, resY] = sim.getVisionSensorImg(rgbVisionSensor)
    img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)

    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 1)

    cv2.imshow('', img)
    cv2.waitKey(1)

    sim.step()

sim.stopSimulation()