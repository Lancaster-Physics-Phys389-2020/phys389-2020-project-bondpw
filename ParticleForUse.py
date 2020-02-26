import numpy as np
import math
import copy

class ParticleFunction:

    def __init__(self, Position_x, Position_y, Velocity, Acceleration, Name, Mass):
        self.Name = Name
        self.Position_x = Position_x
        self.Position_y = Position_y
        self.Velocity = np.array(Velocity)
        self.Acceleration = np.array(Acceleration)
        self.mass = Mass

    def __repr__(self):
        return 'Particle: %10s, Mass: %.5e, Position_x: %.5e, Position_y: %.5e, Velocity: %s, Acceleration: %s'%(self.Name,self.mass,self.Position_x,self.Position_y, self.Velocity,self.Acceleration)

    def update(self,delt):
        self.Position_x = self.Position_x + self.Velocity[0]*delt
        self.Position_y = self.Position_y + self.Velocity[1]*delt
        self.Velocity = self.Velocity + self.Acceleration*delt
        
    def updatefunction(self):
        self.Position_y = ma.sin(self.Position_x)

    def setName(self,Name):
        self.Name = Name

class Particle:
  
    def __init__(self, Position, Velocity, Acceleration, Name, Mass):
        self.Name = Name
        self.position = np.array(Position, dtype=float)
        self.velocity = np.array(Velocity)
        self.acceleration = np.array(Acceleration)
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
