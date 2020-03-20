import numpy as np
import math as ma
import copy
'''This is a class that creates and object with the basic properties needed so that it can be modelled moving in two dimentions as are required for this simulation'''
class Particle:
    '''This defines allows for the particle to have a position, velocity and acceleration, all of which are needed in order for it to be modelled as moving'''
    def __init__(self, Position, Velocity, Acceleration, Name, Mass):
        '''Name is defineed as just a string as it will simply be a word associated with one of the particles so they can be differentiated more easily'''
        self.Name = Name
        '''Position, Velocity and Acceleration are all defined as numpy arrays, where the data types are float'''
        self.Position = np.array(Position, dtype = float)
        self.Velocity = np.array(Velocity, dtype = float)
        self.Acceleration = np.array(Acceleration, dtype = float)
        '''Defined as a float, as mass is a scalar value'''
        self.Mass = Mass
        if Mass <= 0:
            raise ValueError("Doesn't describe a real particle, mass must be greater than 0")

    '''This returns the particle as defined with all of it's characteristics'''
    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}'.format(self.Name,self.Mass,self.Position, self.Velocity,self.Acceleration)
    '''The code below defines an update method for both position and velocity using a constant acceleration, this method is the Euler update method'''
    '''The only variable that has to be defined in it is 'delt' which represents the timestep in seconds'''
    def update(self,delt):
        self.Position = self.Position + self.Velocity*delt
        self.Velocity = self.Velocity + self.Acceleration*delt
    '''The code below defines an update method for both position and velocity using a constant acceleration, this method is the Euler Cromer update method'''
    '''The only variable that has to be defined in it is 'delt' which represents the timestep in seconds'''
    def update2(self,delt):
        self.Velocity = self.Velocity + self.Acceleration*delt
        self.Position = self.Position + self.Velocity*delt
    '''This is a section of code that will allow a driving force to be applied to one of the particles'''
    '''This is a sinosidal driving force that has two defining characteristics, the amplitude defined by the variable 'Amp' and it's frequency (in hertz) defined by the variable of the same name'''
    def updatefunction(self,Amp,frequency):
        self.Position[1] = Amp*ma.sin(((2*ma.pi)*frequency)*self.Position[0])
    
    '''This sets the name of the particle to the one given to it'''
    def setName(self,Name):
        self.Name = Name
    '''Equality function is required so that when the testing on the respective 'movement' functions are completed that the assigned Mass in the Particle and Spring function is the same that is called in the test function'''
    def __eq__(self,sample):
        '''the allclose function of the numpy class is needed to make sure that the values are the same within a given tolerance'''
        '''If they aren't the same then they will not be returned'''
        return np.allclose(self.Position, sample.Position,atol=1e-10) and np.allclose(self.Velocity,sample.Velocity,atol=1e-10) and np.allclose(self.Acceleration,sample.Acceleration,atol=1e-10)