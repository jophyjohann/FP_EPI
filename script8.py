from dataset_operations import DataSet_Operations

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

class run:
	def __init__(self):
		self.dat = DataSet_Operations()
		self.dat.import_dataset_measurements()

		self.export_folder = "export_" + __name__ + "/"
		self.export_extension = ".pdf"


	def main(self):
		dataSet = self.dat.dataSet
		
		def maximize():
			'''maximizes the matplotlib plot window'''
			mng = plt.get_current_fig_manager()
			mng.resize(*mng.window.maxsize())
    
		dataSet_No = 4  # Dunkelmessung PM
		data1 = dataSet[dataSet_No]
		name1 = data1['name'][24:-20]
		
		print(50*"_"+"\n\nPlotting: ", name1.replace("_"," "))

		dataSet_No = 5 # Hellmessung  PM
		data2 = dataSet[dataSet_No]
		name2 = data2['name'][24:-20]
		
		print(50*"_"+"\n\nPlotting: ", name2.replace("_"," "))

		plt.plot(data1['x'], data1['y'], '-', label='name1')
		plt.plot(data2['x'], data2['y'], '-', label='name2')
		plt.plot([0.55, 0.55], [0, 1500], 'r--')
		plt.title(label=name1.replace("_"," "))
		plt.ylim(0, 1400)
		plt.savefig(self.export_folder + name1 + "_Fit" + self.export_extension, bbox_inches='tight')
		maximize()
		plt.show()