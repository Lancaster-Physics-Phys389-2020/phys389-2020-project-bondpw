import numpy as np
import copy as cp


class PhysicalSystem:
    def __init__ (self, steps, delt, system):
        self.steps = steps
        self.delt = delt
        self.system = system

    def Movement (self):

        SystemData = []
   
        
        for i in range(self.steps):
            data = []

            for j in self.system: # in range(steps):
                j.update(self.delt)
                #data.append(cp.deepcopy(j))
            data = cp.deepcopy(self.system)
            print(self.system)
            SystemData.append(data)
        np.save("DataForAnalysis",SystemData)


