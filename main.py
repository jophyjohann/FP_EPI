from dataset_operations import *

def init():
	insert_dataset_files()
	datasets_change_comma_to_dot()

def main():
	init()
	import_dataset_measurements()
	print()

	pass

main()