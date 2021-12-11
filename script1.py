from dataset_operations import DataSet_Operations

import matplotlib.pyplot as plt
import numpy as np

class run:
	def main(self):
		self.dat = DataSet_Operations()
		self.dat.import_dataset_measurements()
run=run()
run.main()		

dat=run.dat

dataSet=dat.dataSet

print(dataSet[1]['name'])
print(dat.dataSet[1]['n'])
print(dat.dataSet[1]['x'])
print(dat.dataSet[1]['y'])



fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
plt.plot(p_1, U_1, '.', label='Untergrund Messung')
plt.show()

'''
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