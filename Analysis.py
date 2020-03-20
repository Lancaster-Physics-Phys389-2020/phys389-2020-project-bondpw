import numpy as np
import matplotlib.pyplot as plt

data = np.load("DataForAnalysis.npy", allow_pickle= True)
#data1 = np.load("DataForAnalysisKE.npy", allow_pickle = True)
#data2 = np.load("DataForAnalysisPE.npy", allow_pickle = True)
#data3 = np.load("DataForAnalysisSUM.npy", allow_pickle = True)

TOdata = []
BOdata = []

for i in range(len(data)):
    if data[i].Name == 'TO':
        TOdata.append(data[i].Position)
    if data[i].Name == 'BO':
        BOdata.append(data[i].Position)       


TO_x = []
TO_y = []
BO_x = []
BO_y = []

for i in range(len(TOdata)):
   TO_x.append(TOdata[i][0])
   TO_y.append(TOdata[i][1])
   BO_x.append(BOdata[i][0])
   BO_y.append(BOdata[i][1])

fig = plt.figure()

plt.plot(BO_x,BO_y)
plt.plot(TO_x, TO_y)

plt.show()

#fig = plt.figure()
#plt.plot(BO_x,data1)
#plt.plot(BO_x,data2)

#plt.show()

#fig = plt.figure()
#plt.plot(BO_x,data3)
#plt.show()