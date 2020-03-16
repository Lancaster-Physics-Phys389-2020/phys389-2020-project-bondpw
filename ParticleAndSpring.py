from ParticleForUse import Particle as Pa
import numpy as np
'''This is a class that will use the property of inheritence in order to give a created particle the extra properties of: Mass, linear spring coefficent and a damping coefficient, all of which are needed to simulate a particle moving ontop of a realistic spring'''
class ParticleAndSpring(Pa):
    '''This is defining the extra terms that will be used, and what they should be, i.e. a float'''
    def __init__(self, Position=np.array([0,1],dtype=float), Velocity=np.array([0,0],dtype=float), Acceleration = np.array([0,0],dtype=float), Name = 'TopObject1', Mass = 1.0, LinF = 1.0, DampF = 1.0):
        super().__init__(Position = Position, Velocity = Velocity, Acceleration = Acceleration, Name = Name) 
        self.Mass = Mass
        '''This raises an error message if the mass wouldn't describe a real particle'''
        if self.Mass <= 0:
            raise ValueError("Mass must be greater than 0")
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