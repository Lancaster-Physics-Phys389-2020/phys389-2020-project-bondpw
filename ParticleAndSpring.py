from Particle import Particle as Pa
import numpy as np
'''This is a class that will use the property of inheritence in order to give a created particle the extra properties of: linear spring coefficent and a damping coefficient, all of which are needed to simulate a particle moving ontop of a realistic spring'''
class ParticleAndSpring(Pa):
    '''This is defining the extra terms that will be used, and what they should be, i.e. a float'''
    def __init__(self, Position=np.array([0,1],dtype=float), Velocity=np.array([0,0],dtype=float), Acceleration = np.array([0,0],dtype=float), Name = 'TopObject1', Mass = 1.0, LinF = 1.0, DampF = 1.0):
        super().__init__(Position = Position, Velocity = Velocity, Acceleration = Acceleration, Name = Name, Mass = Mass) 
        self.LinF = LinF 
        '''This raises an error message if the spring constant wouldn't describe a real spring'''
        if self.LinF <= 0:
            raise ValueError("Spring constant must be greater than 0")
        self.DampF = DampF
        '''This raises an error message if the damping coefficient '''
        if self. DampF < 0:
            raise ValueError("Damping coefficient must greater than, or equal to 0")

    '''This returns the new object once it has been created'''
    def __repr__(self):  
        return 'TopObject1: {0}, Mass: {1:12.3e}, LinF: {2:12.3e}, DampF: {3:12.3e}, Position: {4}, Velocity: {5}, Acceleration: {6}'.format(self.Name,self.Mass,self.LinF,self.DampF,self.Position,self.Velocity,self.Acceleration)
    '''Defines the potential energy of the system based on the spring th'''
    def potentialenergy(self):
        '''This is the equation for potential energy, position -1 is used because this is the distance from the equillibrium point of the particle'''
        return 0.5*self.LinF*(self.Position[1]-1)*(self.Position[1]-1)
    '''Defines the kinetic energy at one place'''
    '''Only the y component is imortant as there is a constant x velocity so we kow this is conserved anyway'''
    def kineticenergy(self):
        return 0.5*self.Mass*(self.Velocity[1])*(self.Velocity[1])
    '''Equality function is required so that when the testing on the respective 'movement' functions are completed that the assigned Mass in the Particle and Spring function is the same that is called in the test function'''
    def __eq__(self,sample):
        '''the allclose function of the numpy class is needed to make sure that the values are the same within a given tolerance'''
        '''If they aren't the same then they will not be returned'''
        return np.allclose(self.Mass,sample.Mass,atol=1e-10) and np.allclose(self.LinF,sample.LinF,atol=1e-10),np.allclose(self.DampF,sample.DampF,atol=1e-10)