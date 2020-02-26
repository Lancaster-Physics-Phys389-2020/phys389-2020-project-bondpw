import numpy as np
import math
import copy

class Particle:
  
    def __init__(self, Position, Velocity, Acceleration, Name, Mass):
        self.Name = Name
        self.position = np.array(Position, dtype=float)
        self.velocity = np.array(Velocity, dtype=float)
        self.acceleration = np.array(Acceleration, dtype=float)
        self.mass = Mass

    def __repr__(self):
        return 'Particle: %10s, Mass: %.5e, Position: %s, Velocity: %s, Acceleration: %s'%(self.Name,self.mass,self.position, self.velocity,self.acceleration)

    def update(self, delt):
        self.position = self.position + self.velocity*delt
        self.velocity = self.velocity + self.acceleration*delt

    def setPosition(self, Position):
        self.position = np.array(Position)


    def setName(self, Name):
        self.Name = Name


class ParticleFunction(Particle):
        
    def updatefunction(self):
        self.position[1] = math.sin(self.position[0])

 
