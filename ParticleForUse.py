import numpy as np
import math
import copy

class Particle:
  
    def __init__(self, Position, Velocity, Acceleration, Name, Mass):
        self.Name = Name
        self.position = np.array(Position, dtype=float)
        self.velocity = np.array(Velocity)
        self.acceleration = np.array(Acceleration)
        self.mass = Mass

    def __repr__(self):
        return 'Particle: %10s, Mass: %.5e, Position: %s, Velocity: %s, Acceleration: %s'%(self.Name,self.mass,self.position, self.velocity,self.acceleration)

    def update(self, deltaT):
        self.position = self.position + self.velocity*deltaT
        self.velocity = self.velocity + self.acceleration*deltaT

    def setPosition(self, Position):
        self.position = np.array(Position)

    def setName(self, Name):
        self.Name = Name


    #velocity = np.array([0, 0])
    #position = np.array([0, 0])
    #acceleration = np.array([0,0])
    #Name = "default"
    #mass = 1.     
    
    
