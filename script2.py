from dataset_operations import DataSet_Operations
import matplotlib.pyplot as plt
import numpy as np

class run:
	def __init__(self):
		self.dat = DataSet_Operations()
		self.dat.import_dataset_measurements()


	def main(self):
		dataSet = self.dat.dataSet

		print("script2.py is running!")