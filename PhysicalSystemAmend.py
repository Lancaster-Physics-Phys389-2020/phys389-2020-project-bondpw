import numpy as np
import copy as cp
import math as ma

'''This class will define the physical system that the particle will be moving in'''
class PhysicalSystem:
    '''This is defining the parameters of the system'''
    ''' 'Steps', defines the amount of times the system will be updated'''
    ''' 'delt' which is short for 'delta t' is the size of the time step '''
    '''Top Object, and Bottom Object are the two particles that comprise the system, with bottom object being that providing the driving force, and top object being the one that is acted on'''
    def __init__ (self, steps, delt, TopObject,BottomObject):
        self.steps = steps
        self.delt = delt
        if delt <= 0:
            raise ValueError("Time step must be greater than 0")
        self.TopObject = TopObject
        self.BottomObject = BottomObject

    '''This defines how the object will move'''
    def Movement (self):
        '''This is a list that will contain all of the information of each particle at each step in the simulation'''
        SystemData = []
        '''This loop ensures that the simulation runs for the amount of steps defined'''
        for i in range(self.steps):
            '''tempacc is a initial variable that will be amended, it is 0 at the beginning so new acceleration can be added onto this, as it doens't depend on the previous step'''
            tempacc = 0.0
            ''''dy' is a variable which is the amount spring is displaced from it's equillibrium position'''
            dy = (self.TopObject.Position[1] - self.BottomObject.Position[1])-1
            '''This adds on to temp acc what the acceleration of the system would be based on the variable dy and the velocity of the object being acted on.'''
            tempacc += (1/(self.TopObject.Mass))*-((self.TopObject.LinF)*dy + self.TopObject.DampF*self.TopObject.Velocity[1])
            '''This changes the acceleration of the system (only applicable in the y direction) to tempacc, which is the variable equal to the systems acceleration'''
            self.TopObject.Acceleration[1] = tempacc
            '''This updates the Top Object using the system information using one of the two update methods defined in the Particle Class'''
            '''For the Euler method use 'update' for Euler Cramer method use 'update2' '''
            self.TopObject.update2(self.delt)
            '''This sets the function for the Bottom Object to move in, making it act as a driving force'''
            self.BottomObject.updatefunction(0.01,0.515)
            '''This updates the position of the bottom object, the same update methods can be used for this as described above in top object'''
            self.BottomObject.update2(self.delt)
            '''This saves the data for the top object '''
            data1 = cp.deepcopy(self.TopObject)
            '''This saves the data for the bottom object'''
            data2 = cp.deepcopy(self.BottomObject)
            '''This updates the system data list with the data for the top and bottom objects'''
            SystemData.append(data1)
            SystemData.append(data2)
        '''Once all iterations are complete, this saves the system data so it can be used for analysis'''
        np.save("DataForAnalysis",SystemData)

