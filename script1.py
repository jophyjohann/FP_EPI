from dataset_operations import DataSet_Operations

class run:
	def main(self):
		self.dat = DataSet_Operations()
		self.dat.import_dataset_measurements()
		

run=run()
run.main()

print(run.dat.dataSet[1]['name'])
'''
print(run.dat.dataSet[1]['n'])
print(run.dat.dataSet[1]['x'])
print(run.dat.dataSet[1]['y'])

import matplotlib.pyplot as plt
import numpy as np
import importlib
from scipy.optimize import *


N_1, p_1, U_1 = np.loadtxt("Laser_Untergrund.csv", unpack = True, skiprows=10, delimiter=';')
N_2, p_2, U_2 = np.loadtxt("Laser_beide_offen.csv", skiprows=6, delimiter=';')[0]
N_3, p_3, U_3 = np.loadtxt("Laser_linker_Spalt_offen.csv", skiprows=6, delimiter=';')[0]
N_4, p_4, U_4 = np.loadtxt("DS_Laser_rechter_Spalt_offen.csv", skiprows=8, delimiter=';')[0]


fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
plt.plot(p_1, U_1, '.', label='Untergrund Messung')

plt.show()

fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
plt.plot(p_2, U_2, '.', label='Doppelspalt')

plt.show()

fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
plt.plot(p_3, U_3, '.', label='Linker Spalt')

plt.show()

fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
plt.plot(p_4, U_4, '.', label='Rechter Spalt')

plt.show()
'''