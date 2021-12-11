from dataset_operations import DataSet_Operations

class run:
	def main(self):
		self.dat = DataSet_Operations()
		self.dat.import_dataset_measurements()
		

run=run()
run.main()

print(run.dat.dataSet[1]['name'])
print(run.dat.dataSet[1]['n'])
print(run.dat.dataSet[1]['x'])
print(run.dat.dataSet[1]['y'])
