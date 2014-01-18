import os.path
import fnmatch
import json




def main():
	curr_path = os.getcwd()

	path_content_list = os.listdir(curr_path)

	path_file_list = [txt_file for txt_file in path_content_list if os.path.isfile(os.path.join(curr_path,txt_file))]

	path_txt_list = fnmatch.filter(path_file_list, '*.txt')

	biggest_num_of_children = 0

	for txt_file in path_txt_list:
		#print os.path.join(curr_path, txt_file)
		try:
			with open(txt_file, "r") as obj_file:
				Qobject = json.load(obj_file)
				print Qobject['object'] + str(len(Qobject['children']))

				num_of_children = len(Qobject['children'])

				if num_of_children > biggest_num_of_children:
					most_children = Qobject
					biggest_num_of_children = num_of_children
				
				print most_children['object'] + str(len(most_children['children']))



			raw_input()
		except KeyboardInterrupt:
			break


if __name__ == '__main__':
    main()