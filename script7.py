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
		def func_double_slit_original(x, x0, L, a, b, Lambda, I0, U):
			theta = (x - x0) / L
			F = a * np.pi * theta / Lambda
			G = b * np.pi * theta / Lambda
			return I0 * np.cos(G) ** 2 * (np.sin(F) / F) ** 2 + U
		
		def func_double_slit(x, x0, a, b, I0, U):
			Lambda = 670e-6
			L = 500
			theta = (x - x0) / L
			F = a * np.pi * theta / Lambda
			G = b * np.pi * theta / Lambda
			return I0 * np.cos(G) ** 2 * (np.sin(F) / F) ** 2 + U
		
      
		### Plot ... ###
		
		dataSet_No = 9 # Doppel-Spalt Lampe
		data = dataSet[dataSet_No]
		name = data['name'][24:-20]
		
		print(50*"_"+"\n\nPlotting: ", name.replace("_"," "))
		
		plot_ra = [1,-2]
		fit_ra = [43,-30]
		fit_plot_ra = [43,-30]
		
		data['x'] = data['x'][plot_ra[0]:plot_ra[1]]
		data['y'] = data['y'][plot_ra[0]:plot_ra[1]]
		
		fit_param_original = [["x₀" ,"L ","a " ,"b ",     "λ ","I₀","U "],
									[5.0 , 550,  0.5, 2  , 670.1e-6,   2, 0.5],		# max values
									[4.29, 500, 0.07, 0.5,   670e-6, 1.4, 0.1],		# start values
									[4.0 , 450,0.001, 0.1, 669.9e-6,   1,   0]]		# min values
		
		fit_param = [["x₀" ,"a " ,"b ", "I₀","U "],
									[5.0 ,  0.5, 4  ,   1600, 170],		# max values
									[4.29, 0.07, 0.5, 1500, 100],		# start values
									[4.0 ,0.001, 0.1,   1,   50]]		# min values
		
		func = func_double_slit
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
		plt.xlim(0, 8.5)
		plt.ylim(0,1500)
		plt.savefig(self.export_folder + name + "_Fit" + self.export_extension, bbox_inches='tight')
		maximize()
		plt.show()