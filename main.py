from dataset_operations2 import DataSet_Operations

class run:
	def __init__(self):
		self.dat = DataSet_Operations()
		self.dat.insert_dataset_files()
		self.dat.datasets_change_comma_to_dot()
		#insert_dataset_files()
		#datasets_change_comma_to_dot()

	def main(self):
		print("läuft")
		self.__init__()
		self.dat.import_dataset_measurements()
		print(self.dat.dataSet)
		
r=run()
r.main()