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
		data = dataSet[dataSet_No]
		name = data['name'][24:-20]
		
		print(50*"_"+"\n\nPlotting: ", name.replace("_"," "))

		plt.plot(data['x'], data['y'], '-', label='name1')
		plt.title(label=name.replace("_"," "))
		plt.ylim(0, 1400)
		plt.savefig(self.export_folder + 'name123' + self.export_extension, bbox_inches='tight')
		maximize()
		plt.show()