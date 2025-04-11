from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import cv2
import math


client = RemoteAPIClient()
sim = client.require('sim')

sim.setStepping(True)

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)

parameters = cv2.aruco.DetectorParameters_create()

camera_matrix = np.array([[772.548, 0, 320], [0, 772.548, 240], [0, 0, 1]], dtype=np.float32)
dist_coeffs = np.zeros((5, 1)) 


marker_length = 0.08


rgbVisionSensor0=sim.getObject('/camera_color_optical_frame')
sim.startSimulation()

while (t := sim.getSimulationTime()) < 10:

    img0, [resX, resY] = sim.getVisionSensorImg(rgbVisionSensor0)
    frame = np.frombuffer(img0, dtype=np.uint8).reshape(resY, resX, 3)

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the markers in the image
    corners, ids, rejected = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    print(ids)
    if ids is not None:
        # Estimate pose of each marker
        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, marker_length, camera_matrix, dist_coeffs)
        print(len(ids))
        print(tvecs)
        # Loop through all detected markers and draw axes
        for i in range(len(ids)):
            # Draw detected marker borders
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)

            # Draw the 3D axes for each marker
            cv2.aruco.drawAxis(frame, camera_matrix, dist_coeffs, rvecs[i], tvecs[i], marker_length * 0.5)

            # Display the translation and rotation vectors on the marker
            rvec_str = f"Rvec: {np.round(rvecs[i][0], 2)}"
            tvec_str = f"Tvec: {np.round(tvecs[i][0], 2)}"
            cv2.putText(frame, rvec_str, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            cv2.putText(frame, tvec_str, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Aruco Pose Estimation', frame)

    sim.step()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()


sim.stopSimulation()