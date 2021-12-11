from dataset_operations import DataSet_Operations
import matplotlib.pyplot as plt
import numpy as np

class run:
	def __init__(self):
		self.dat = DataSet_Operations()
		self.dat.import_dataset_measurements()


	def main(self):
		dataSet = self.dat.dataSet


		for data in dataSet:
			print(80*"_"+"\n\nPlotting: ",data['name'])
		
			fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
			plt.plot(data['x'], data['y'], '.', label='Untergrund Messung')
			plt.title(label=data['name'][24:-20])
			plt.show()

