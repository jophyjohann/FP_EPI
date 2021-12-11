from dataset_operations import DataSet_Operations
import script1

class run:
	def __init__(self):
		self.dat = DataSet_Operations()
		
		self.dat.insert_dataset_files()
		self.dat.datasets_change_comma_to_dot()

	def main(self):
		self.__init__()
		self.dat.import_dataset_measurements()
		#print(self.dat.dataSet)
		
run=run()
run.main()
