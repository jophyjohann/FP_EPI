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
    
		
		for x in range(2,8):
			#exec("import script"+str(x))
			#setattr(self, "s"+str(x), popt)
			#exec("s"+str(x)+"=script"+str(x)+".run()")
		
			#exec("print(s2.main.popt2)")
			pass

		import script2
		s2_run = script2.run()
		s2 = s2_run.__init__()
		print(s2.popt)
		
		#print(50*"_"+"\n\nPlotting: test123")

		fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
		#plt.plot(popt)
		plt.title(label=name.replace("_"," "))
		plt.savefig(self.export_folder + "test123" + self.export_extension, bbox_inches='tight')
		maximize()
		#plt.show()