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

		#define uncertainty of given L and Lambda
		delta_L = 50
		delta_Lambda = 20e-6
		
		#define mean values of Lambda and L:
		L = 500
		Lambda = 670e-6

		Lambda_values = [Lambda - delta_Lambda, Lambda, Lambda + delta_Lambda]
		L_values = [L - delta_L, L, L + delta_L]

		Lambda = Lambda_values[1]
		L = L_values[1]

	  ### Define some fitting functions
		def func_single_slit(x, x0, a, I0, U):
			theta = (x - x0) / L
			F = a * np.pi * theta / Lambda
			return I0 * (np.sin(F) / F) ** 2 + U


	### Plot ... ###
		
		dataSet_No = 10 # Nur rechter Spalt Lampe
		data = dataSet[dataSet_No]
		name = data['name'][24:-20]
		
		print(50*"_"+"\n\nPlotting: ", name.replace("_"," "))
		
		plot_ra = [1,-2]
		fit_ra = [30,-10]
		fit_plot_ra = [30,-10]
		
		data['x'] = data['x'][plot_ra[0]:plot_ra[1]]
		data['y'] = data['y'][plot_ra[0]:plot_ra[1]]
		
		fit_param = [["x₀" , "a " ,"I₀","U "],
									[ 5.5,   0.5, 610,  50],		# max values
									[4.29,  0.07, 300, 0.1],		# start values
									[3.5 , 0.001, 270,   0]]		# min values
		
		func = func_single_slit
		
		popt = 3 * [None]
		pcov = 3 * [None]
		for i in range(0,3):
			Lambda = Lambda_values[i]
			L = L_values[i]
			popt[i], pcov[i] = curve_fit(func, data['x'][fit_ra[0]:fit_ra[1]], data['y'][fit_ra[0]:fit_ra[1]], fit_param[2], bounds=(fit_param[3],fit_param[1]))
		
		setattr(self, "popt"+str(dataSet_No), popt)
		setattr(self, "pcov"+str(dataSet_No), pcov)
		
		print("\nFit Parameter:")
		print("Param.  Wert    Δ(Fit)      Δ(λ,L)       -> Param(min...max)")
		for param in fit_param[0]:
			i = fit_param[0].index(param)
			print("{} = {:.7}\t±{:.7f} \t[±{:.6f}]  \t({:.4}...{:.4f})".format(param,popt[1][i],np.sqrt(np.diag(pcov[1]))[i],np.abs(popt[2][i] - popt[0][i]) + np.sqrt(np.diag(pcov[0]))[i] + np.sqrt(np.diag(pcov[2]))[i],min(popt[0][i],popt[2][i]) - np.sqrt(np.diag(pcov[0]))[i], max(popt[0][i],popt[2][i]) + np.sqrt(np.diag(pcov[2]))[i]))
		
		Lambda = Lambda_values[1]
		L = L_values[1]

		fit_x = np.linspace(data['x'][fit_plot_ra[0]:fit_plot_ra[1]][0], data['x'][fit_plot_ra[0]:fit_plot_ra[1]][-1], 1000)
		
		fig = plt.figure(figsize=(8, 4), dpi=120).add_subplot(1, 1, 1)
		plt.plot(data['x'], data['y'], '.')
		plt.plot(fit_x, func(fit_x,*popt[1]), 'r--')
		plt.xlabel('Detektorspaltposition x / mm')
		plt.ylabel('Impulsrate 1 / s')
		plt.title(label=name.replace("_"," "))
		plt.xlim(0, 8.5)
		plt.ylim(0, 610)
		plt.savefig(self.export_folder + name + "_Fit" + self.export_extension, bbox_inches='tight')
		maximize()
		plt.show()