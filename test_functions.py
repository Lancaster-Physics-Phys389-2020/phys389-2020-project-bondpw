import pytest as pyt
import numpy as np
from ParticleForUse import Particle as Pa 

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