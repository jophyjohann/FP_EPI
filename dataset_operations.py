import glob, os

folder_name="measurements"
file_extension=".csv"


def dataset_change_comma_to_dot():
	os.chdir(folder_name)
	for filename in glob.glob("*"+file_extension):
		#print(filename)
		file=open(filename,"r")
		data=file.read().replace(",",".")
		file=open(filename,"w")
		file.write(data)
		file.close()
