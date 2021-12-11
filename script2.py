from dataset_operations import DataSet_Operations
import matplotlib.pyplot as plt
import numpy as np

class run:
	def __init__(self):
		self.dat = DataSet_Operations()
		self.dat.import_dataset_measurements()

		self.export_folder = "export_script1/"
		self.export_extension = ".pdf"


	def main(self):
		dataSet = self.dat.dataSet


		### Plot all measured datasets (11) and export them for overwiev ###
		
		data = dataSet[0]
		print(80*"_"+"\n\nPlotting: ",data['name'])
		
		fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
		plt.plot(data['x'], data['y'], '.')
		plt.title(label=data['name'][24:-20])
		plt.savefig(self.export_folder+data['name'][24:-20]+self.export_extension, bbox_inches='tight')
		plt.show()

