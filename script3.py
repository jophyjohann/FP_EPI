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
		
		print("script3.py is running!")