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

	  ### Define some fitting functions
		def func_single_slit(x, x0, a, I0, U):
			L = 500
			Lambda = 670e-6
			theta = (x - x0) / L
			F = a * np.pi * theta / Lambda
			return I0 * (np.sin(F) / F) ** 2 + U


	### Plot ... ###
		
		dataSet_No = 10 # Nur linker Spalt Lampe
		data = dataSet[dataSet_No]
		name = data['name'][24:-20]
		
		print(50*"_"+"\n\nPlotting: ", name.replace("_"," "))
		
		plot_ra = [1,-2]
		fit_ra = [30,-10]
		fit_plot_ra = [30,-10]
		
		data['x'] = data['x'][plot_ra[0]:plot_ra[1]]
		data['y'] = data['y'][plot_ra[0]:plot_ra[1]]
		
		fit_param = [["x₀" , "a " ,"I₀","U "],
									[ 5.5,   0.5, 630,  20],		# max values
									[4.29,  0.07, 600, 0.1],		# start values
									[3.5 , 0.001, 570,   0]]		# min values
		
		func = func_single_slit
		popt, pcov = curve_fit(func, data['x'][fit_ra[0]:fit_ra[1]], data['y'][fit_ra[0]:fit_ra[1]], fit_param[2], bounds=(fit_param[3],fit_param[1]))

		setattr(self, "popt"+str(dataSet_No), popt)
		setattr(self, "pcov"+str(dataSet_No), pcov)
		
		print("\nFit Parameter:")
		for param in fit_param[0]:
			i = fit_param[0].index(param)
			print("{} = {:.4g} ± {:.4g}".format(param,popt[i],np.sqrt(np.diag(pcov))[i]))
		
		fit_x = np.linspace(data['x'][fit_plot_ra[0]:fit_plot_ra[1]][0], data['x'][fit_plot_ra[0]:fit_plot_ra[1]][-1], 1000)
		
		fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
		plt.plot(data['x'], data['y'], '.')
		plt.plot(fit_x, func(fit_x,*popt), 'r--')
		plt.title(label=name.replace("_"," "))
		plt.savefig(self.export_folder + name + "_Fit" + self.export_extension, bbox_inches='tight')
		maximize()
		plt.show()