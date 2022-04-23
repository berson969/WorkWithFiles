# Задача №3


import os


FILE_PATH_RES = os.path.join(os.getcwd(),'WorkWithFiles','res.txt')

with open(FILE_PATH_RES, 'w') as rs:
    rs.write('')

def read_files(file):
    FILE_PATH = os.path.join(os.getcwd(),'WorkWithFiles',file)
    with open(FILE_PATH, 'r') as f:
        file_for_read = f.readlines()
        len_ = len(file_for_read)
        file_for_read.append(file)
        dict_files[len_] = file_for_read


dict_files = {}
read_files('1.txt')
read_files('2.txt')
read_files('3.txt')
# print(dict_files)

with open(FILE_PATH_RES, 'a') as rs:
    for len_ in sorted(dict_files):
        file_name = dict_files[len_].pop(len_)
        rs.write(file_name + '\n')
        print(file_name)
        rs.write(str(len_) + '\n')
        print(str(len_))
        [rs.write(line) for line in dict_files[len_]]
        [print(line.strip('\n')) for line in dict_files[len_]]
        rs.write('\n')





