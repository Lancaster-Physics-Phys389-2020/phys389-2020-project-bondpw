import pytest as pyt
import numpy as np
from ParticleForUse import Particle as Pa 

def test_update(): 
    assert Pa([1.0,1.0],[1.0,1.0],[1.0,1.0],'TestObject').update(5) == Pa([6.0,6.0],[6.0,6.0],[1.0,1.0],'TestObject')
    
    assert Pa([1.0,1.0],[1.0,1.0],[1.0,1.0],'TestObject').update2(5) == Pa([31.0,31.0],[6.0,6.0],[1.0,1.0],'TestObject')