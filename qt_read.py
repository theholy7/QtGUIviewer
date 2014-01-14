import os.path
import fnmatch




def main():
	curr_path = os.getcwd()

	path_content_list = os.listdir(curr_path)

	path_file_list = [txt_file for txt_file in path_content_list if os.path.isfile(os.path.join(curr_path,txt_file))]

	path_txt_list = fnmatch.filter(path_file_list, '*.txt')


if __name__ == '__main__':
    main()