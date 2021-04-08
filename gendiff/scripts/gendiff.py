import argparse
import os
import json


def generate_diff(file_path1, file_path2):
    file1 = open(os.path.abspath(file_path1))
    file2 = open(os.path.abspath(file_path2))
    file1_data = json.load(file1)
    file2_data = json.load(file2)
    file1.close()
    file2.close()

    result = '{\n'

    keys = set(file1_data)
    keys.update(file2_data)
    keys = sorted(list(keys))

    for key in keys:
        if file1_data.get(key):
            if file2_data.get(key):
                if file1_data[key] == file2_data[key]:
                    result += f'    {key}: {file1_data[key]}\n'
                else:
                    result += f'  - {key}: {file1_data[key]}\n'
                    result += f'  + {key}: {file2_data[key]}\n'
            else:
                result += f'  - {key}: {file1_data[key]}\n'
        else:
            result += f'  + {key}: {file2_data[key]}\n'

    result += '}'

    return result


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
