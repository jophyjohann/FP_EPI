from dataset_operations import DataSet_Operations


class run:

	def __init__(self):
		self.dat = DataSet_Operations()

		self.n_scripts = 2

		for i in range(1,self.n_scripts+1):
			exec("import script"+str(i))
			exec("self.s"+str(i)+"=script"+str(i)+".run()")
		
		self.dat.insert_dataset_files()
		self.dat.datasets_change_comma_to_dot()


	def script_start(self):
		x = input()
		while(True):
			if x.isdigit() and int(x) <= run.n_scripts and int(x) > 0:
				exec("run.s"+x+".main()")
			elif x[:-1].isdigit() and x[-1:]=="d" and int(x[:-1]) <= run.n_scripts and int(x[:-1]) > 0:
				while(True):
					exec("run.s"+x[:-1]+".main()")
					print(80*"_"+"\nStarting script again..")
			else:
				print('Loading all..\n')
				for i in range(run.n_scripts):
					exec("run.s"+str(i+1)+".main()")
			print('\nExecuted sucessfully...')
			y = input()
			if y != '' and y != x:
				x = y


	def main(self):
		self.__init__()
		self.dat.import_dataset_measurements()

		self.script_start()


run=run()

run.main()