import pytest as pyt
import numpy as np
import math as ma
from ParticleForUse import Particle as Pa 
from ParticleAndSpring import ParticleAndSpring as PaS
from PhysicalSystemAmend import PhysicalSystem as ps

def test_update(): 
    TestP = Pa([0.0,0.0],[0.0,0.0],[1.0,1.0],'TestP')
    TestP.update(1)
    TestPexp = Pa([0.0,0.0],[1.0,1.0],[1.0,1.0],'TestP')

    assert TestP == TestPexp
    
def test_update_2():
    
    TestPEC = Pa([0.0,0.0],[0.0,0.0],[1.0,1.0],'TestP')
    TestPEC.update2(1)
    TestPECexp = Pa([1.0,1.0],[1.0,1.0],[1.0,1.0],'TestP')

    assert TestPEC == TestPECexp

def test_acceleration():
    TestObject1 = Pa([0,-1],[1,0],[0,0],'BO')
    TestObject2 = PaS([0,0],[1,0],[0,0],'TO',1,10,0)

    Test1 = ps(2,1,TestObject2,TestObject1)
    Test1.Movement()

    finaltestobject = Test1.TopObject.Acceleration[1]
    dy = (TestObject2.Position[1] - TestObject1.Position[1])-1
    finaltestexp = (1/(TestObject2.Mass))*(-(TestObject2.LinF)*dy)

    assert finaltestobject == finaltestexp
