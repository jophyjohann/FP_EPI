from dataset_operations import DataSet_Operations

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

class run:
	def __init__(self):
		self.dat = DataSet_Operations()
		self.dat.import_dataset_measurements()

		self.export_folder = "export_script2/"
		self.export_extension = ".pdf"


	def main(self):
		dataSet = self.dat.dataSet
		
		### Define some fitting functions
		def func_single_slit(x, x0, L, a, Lambda, I0, U):
			theta = (x - x0) / L
			F = a * np.pi * theta / Lambda
			return I0 * (np.sin(F) / F) ** 2 + U	#alternative for sinus: return I0 * ((F-(1/6)*F**3+(1/120)*F**5) / F) ** 2 + U

		def func_double_slit(x, a, b):

			return a*x + b


		### Plot ... ###
		
		dataSet_No = 2
		data = dataSet[dataSet_No]
		print(50*"_"+"\n\nPlotting: ",data['name'])
		
		plot_ra = [1,-2]
		fit_ra = [0,None]
		fit_plot_ra = [0,None]
		
		data['x'] = data['x'][plot_ra[0]:plot_ra[1]]
		data['y'] = data['y'][plot_ra[0]:plot_ra[1]]
		
		fit_param = [["x0", "L", "a","Lambda", "I0", "U"],
									[4.2, 700, 1e5,     600,    1, 0.5],		# max values
									[3.8, 400, 6e4,     546, 0.41, 0.1],		# start values
									[3.3, 200, 1e4,     500,  0.1,   0]]		# min values

		func = func_single_slit
		popt, pcov = curve_fit(func, data['x'][fit_ra[0]:fit_ra[1]], data['y'][fit_ra[0]:fit_ra[1]], fit_param[2])#, bounds=(fit_param[3],fit_param[1]))

		setattr(self, "popt"+str(dataSet_No), popt)
		setattr(self, "pcov"+str(dataSet_No), pcov)
		
		print(popt)
		fit_x = np.linspace(data['x'][0], data['x'][-1], 1000)
		
		fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
		plt.plot(data['x'], data['y'], '.')
		plt.plot(fit_x, func(fit_x,*popt), 'r--')
		plt.title(label=data['name'][24:-20])
		plt.savefig(self.export_folder+data['name'][24:-20]+"_Fit"+self.export_extension, bbox_inches='tight')
		plt.show()
