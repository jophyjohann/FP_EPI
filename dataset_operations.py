import glob, os


folder_name="measurements/"
file_extension=".csv"


this_file = __name__ + ".py"
working_path = os.getcwd()

#automatically inserted dataset_files:
dataset_files = ["EPI_010_20211209-104606_DS_Laser_Untergrund_20211209-104502.csv",
								 "EPI_010_20211209-111211_DS_Laser_beide_offen_20211209-110611.csv",
								 "EPI_010_20211209-112504_DS_Laser_linker_Spalt_offen_20211209-112029.csv",
								 "EPI_010_20211209-113144_DS_Laser_rechter_Spalt_offen_20211209-112624.csv",
								 "EPI_010_20211209-120351_DS_Lampe_Kalibrierung_closed_shutter_20211209-115826.csv",
								 "EPI_010_20211209-121129_DS_Lampe_Kalibrierung_opened_shutter_20211209-120507.csv",
								 "EPI_010_20211209-122000_DS_Lampe_Kalibrierung_zaehlrate_bei_arbeitsspannung_closed_shutter_20211209-121701.csv",
								 "EPI_010_20211209-123020_DS_Lampe_Kalibrierung_zaehlrate_bei_arbeitsspannung_opened_shutter_20211209-122225.csv",
								 "EPI_010_20211209-140834_DS_Lampe_linker_Spalt_offen_20211209-132953.csv",
								 "EPI_010_20211209-143459_DS_Lampe_beide_offen_20211209-141521.csv",
								 "EPI_010_20211209-145858_DS_Lampe_rechter_Spalt_offen_20211209-143658.csv",
								 ]
#end of automatically inserted dataset_files


def datasets_change_comma_to_dot():
	for filename in dataset_files:
		#print(filename)
		file =  open(folder_name + filename,"r")
		data =file.read().replace(",", ".")
		file = open(folder_name + filename,"w")
		file.write(data)
		file.close()


def insert_dataset_files():
	os.chdir(folder_name)
	new_filenames = glob.glob("*" + file_extension)
	os.chdir(working_path)

	filename_list = '['
	for file in new_filenames:
		filename_list += '"' + file + '",\n								 '
	filename_list += ']'
	filename_list.replace(",\n								 ]","]")
	filename_list += "\n"

	file = open(this_file,"r")
	data = file.read()
	file = open(this_file,"w")
	start_string = "#automatically inserted dataset_files:"
	stop_string = "#end of automatically inserted dataset_files"
	additional_string = "\ndataset_files = "
	dataset_spot=data[data.find(start_string):data.find(stop_string)] + stop_string
	file.write(data.replace(dataset_spot, start_string + additional_string + filename_list + stop_string))
	file.close()

def import_dataset_measurements():
	dataSet=len(dataset_files)*[]
	for i in range(len(dataset_files)):
		dataSet[i] = {
        'name': dataset_files[i],
				'n': np.loadtxt(dataset_files + file_extension, unpack=True,comment="#",usecols=(0)),
        'x': np.loadtxt(dataset_files + file_extension, unpack=True,comment="#",usecols=(1)),
        'y': np.loadtxt(dataset_files + file_extension, unpack=True,comment="#",usecols=(2)),
    		}
	