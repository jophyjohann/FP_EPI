from dataset_operations import DataSet_Operations
import matplotlib.pyplot as plt
import numpy as np

class run:
	def __init__(self):
		self.dat = DataSet_Operations()
		self.dat.import_dataset_measurements()


	def main(self):
		dataSet = self.dat.dataSet

		print(80*"_"+"\n\nPlotting: ",dataSet[0]['name'])

		fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
		plt.plot(dataSet[0]['x'], dataSet[0]['y'], '.', label='Untergrund Messung')
		plt.title()
		plt.show()


		print(80*"_"+"\n\nPlotting: ",dataSet[1]['name'])

		fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
		plt.plot(dataSet[1]['x'], dataSet[1]['y'], '.', label='Doppelspalt')
		plt.show()


		print(80*"_"+"\n\nPlotting: ",dataSet[2]['name'])

		fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
		plt.plot(dataSet[2]['x'], dataSet[2]['y'], '.', label='Linker Spalt')
		plt.show()


		print(80*"_"+"\n\nPlotting: ",dataSet[3]['name'])

		fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
		plt.plot(dataSet[3]['x'], dataSet[3]['y'], '.', label='Rechter Spalt')
		plt.show()
