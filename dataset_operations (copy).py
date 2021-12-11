import glob, os

folder_name="measurements"
file_extension=".csv"

#automatically inserted dataset_files:
dataset_files = ["",
								 "",
								 "",
								 ""]


def datasets_change_comma_to_dot():
	os.chdir(folder_name)
	for filename in glob.glob("*" + file_extension):
		print(filename)
		file =  open(filename,"r")
		data =file.read().replace(",", ".")
		file = open(filename,"w")
		file.write(data)
		file.close()


def insert_dataset_files(new_filenames):
	this_file = __name__ + ".py"

	filename_list = '['
	for file in new_filenames:
		filename_list += '"' + file + '",\n								 '
	filename_list += ']'

	print(filename_list)

	'''
	file = open(this_file,"r")
	data = file.read()
	file = open(this_file,"w")
	file.write(data.replace("#automatically inserted dataset_files:\ndataset_files=", "#automatically inserted dataset_files:\ndataset_files=" + filename_list))
	file.close()
	'''

def create_dataset():
	pass

def import_datasets():
	# Laser Untergrund
	#L_Underground
	pass

def start_insert():
	os.chdir(folder_name)
	for filename in glob.glob("*" + file_extension):
		insert_dataset_files(filename + file_extension)