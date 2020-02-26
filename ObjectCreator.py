from ParticleForUse import ParticleFunction as pa
from PhysicalSystem import PhysicalSystem as ps

baseobject = pa([0,0],[0,0],[1,0],'BO', 1)
topobject = pa([0,1],[0,0],[1,0],'TO', 1)

baseobject.Name

System = [baseobject,topobject]

Forward = ps(100,1,System)
Forward.Movement()