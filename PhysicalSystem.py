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

            for j in self.system:
                if j.Name == 'TO':
                    j.update(self.delt)
                    j.updatefunction()
                if j.Name == 'BO':
                    j.update(self.delt)
            data = cp.deepcopy(self.system)
            SystemData.append(data)
        np.save("DataForAnalysis",SystemData)
