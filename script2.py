from dataset_operations import DataSet_Operations

from scipy.optimize import curve_fit
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
		
		'''
		self.popt={}
		self.pcov={}
		popt=self.popt
		pcov=self.pcov
		'''

		### Define some fitting functions

		def func_double_slit(x, a, b):
			return a*x + b

		### Plot ... ###
		
		dataSet_No = 4
		data = dataSet[dataSet_No]
		print(80*"_"+"\n\nPlotting: ",data['name'])
		
		plot_ra = [0,1000]
		fit_ra = [0,1000]
		fit_plot_ra = [0,1000]
		
		fit_param = [["a", "b"],
									[  0,   1],		# max values
									[  0,   1],		# start values
									[  0,   1]]		# min values

		func = func_double_slit
		popt, pcov = curve_fit(func, data['x'][fit_ra[0]:fit_ra[1]], data['y'][fit_ra[0]:fit_ra[1]], fit_param[2])#, bounds=(fit_param[3],fit_param[1]))

		#popt[dataSet_No]=1
		#pcov[dataSet_No]=2
		setattr(self, "popt"+str(dataSet_No), popt)
		setattr(self, "pcov"+str(dataSet_No), pcov)
		
		fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
		plt.plot(data['x'][plot_ra[0]:plot_ra[1]], data['y'][plot_ra[0]:plot_ra[1]], '.')
		plt.plot(data['x'][fit_plot_ra[0]:fit_plot_ra[1]], func(data['x'][fit_plot_ra[0]:fit_plot_ra[1]],*popt), 'r--')
		plt.title(label=data['name'][24:-20])
		plt.savefig(self.export_folder+data['name'][24:-20]+self.export_extension, bbox_inches='tight')
		plt.show()

		print(popt4)