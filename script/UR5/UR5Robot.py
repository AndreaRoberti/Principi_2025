from Robot import Robot
import numpy as np

class UR5Robot(Robot):
    def __init__(self, client, robot_name):
        super().__init__(client, robot_name)
 
        self.ur5_joints_ = []
        for i in range(6):
            self.ur5_joints_.append('joint' + str(i+1))
        
        print("Joint handles:", self.ur5_joints_)
        
        self.setJoints(self.ur5_joints_)
        
    def getStatus(self):
        print(self.getJointPosition()) 

