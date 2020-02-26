import numpy as np
import copy as cp

class PhysicalSystem:
    def __init__ (self, steps, delt, system):
        self.steps = steps
        self.delt = delt
        self.system = system

    def Movement (self):

        SystemData = []
        Time = []
   
        for i in range(self.steps):

            for j in self.system:
                j.update(self.delt)
            data = cp.deepcopy(self.system)
            SystemData.append(data)

            Time.append((len(SystemData)-1))
        np.save("DataForAnalysis",SystemData)
