from typing import List


def open_file(file_name: str, mode: str, encoding: str) -> List:
    with open(file_name, mode, encoding=encoding) as f:
        result = [line for line in f.readlines()]
        string = file_name + '\n'
        result.append(string)
    return result


def get_general_file(file_name: str, text: List[str], encoding: str, mode='a'):
    with open(file_name, mode, encoding=encoding) as f:
        f.write(text[-1])
        length = str(len(text))
        f.write(length + '\n')
        f.writelines(text[:-1])
        f.write('\n')


all_files = []
file_one = (open_file('1.txt', 'r', 'utf-8'))
file_two = (open_file('2.txt', 'r', 'utf-8'))
file_three = (open_file('3.txt', 'r', 'utf-8'))
# print(file_one)

all_files.append(file_one)
all_files.append(file_two)
all_files.append(file_three)

all_files = sorted(all_files, key=len)
print(all_files)
for file in all_files:
    get_general_file('4.txt', file, 'utf-8')
