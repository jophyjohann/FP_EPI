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
		def func_double_slit(x, x0, L, a, Lambda, I0, d):
      theta = (x - x0) / L
      C = (np.cos(np.pi*d*np.sin(theta)/Lambda))**2
      F = a * np.pi * theta / Lambda
      return I0 * (np.sin(F) / F) ** 2 + 0.07
