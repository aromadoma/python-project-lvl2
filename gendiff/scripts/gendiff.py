import argparse
from gendiff.scripts.parser import parse


def generate_diff(file1_path, file2_path):

    file1_data = parse(file1_path)
    file2_data = parse(file2_path)

    keys = set(file1_data)
    keys.update(file2_data)
    keys = sorted(list(keys))

    diff = '{\n'
    for key in keys:
        if file1_data.get(key):
            if file2_data.get(key):
                if file1_data[key] == file2_data[key]:
                    diff += f'    {key}: {file1_data[key]}\n'
                else:
                    diff += f'  - {key}: {file1_data[key]}\n'
                    diff += f'  + {key}: {file2_data[key]}\n'
            else:
                diff += f'  - {key}: {file1_data[key]}\n'
        else:
            diff += f'  + {key}: {file2_data[key]}\n'
    diff += '}'

    return diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
