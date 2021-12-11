import glob, os

folder_name="measurements"
file_extension=".csv"

#automatically inserted dataset_files:
dataset_files = ["",
								 "",
								 "",
								 ""]
#end of automatically inserted dataset_files


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
	filename_list.replace(",\n								 ]","]")

	print(filename_list)

	file = open(this_file,"r")
	data = file.read()
	#file = open(this_file,"w")
	start_string = "#automatically inserted dataset_files:"
	stop_string = "#end of automatically inserted dataset_files"
	additional_string = "\ndataset_files = "
	dataset_spot=data[data.find(start_string):data.find(stop_string)]

	file.write(data.replace(dataset_spot, dataset_spot + additional_string + filename_list))
	file.close()
	

def create_dataset():
	pass

def import_datasets():
	# Laser Untergrund
	#L_Underground
	pass

def start_insert():
	os.chdir(folder_name)
	filenames = glob.glob("*" + file_extension)
	insert_dataset_files(filenames)