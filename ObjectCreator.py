from Particle import Particle as pa
from ParticleAndSpring import ParticleAndSpring as PaS
from PhysicalSystem import PhysicalSystem as ps
import math as ma
'''This defines the bottom object's initial position, velocity, acceleration and name'''
BottomObject = pa([0,0],[1,0],[0,0],'BO',1)
'''This defines the bottom object's initial position, velocity, acceleration and name'''
'''It also defines the mass of the top object as well as the spring constant and damping coefficenet of the spring attatching the top and bottom object'''
TopObject = PaS([0,0],[1,0],[0,0],'TO',1,10,0)
'''This defines the specific quantities of the parameters laid out in the physical system class'''
Forward = ps(50000,0.01,TopObject,BottomObject)
Forward.Movement()