import argparse
from gendiff.scripts.parser import parse
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.scripts.internal_diff import get_internal_diff


def generate_diff(file1_path, file2_path, view="stylish"):
    """Return diff in a specified format"""
    file1_data = parse(file1_path)
    file2_data = parse(file2_path)
    diff = get_internal_diff(file1_data, file2_data)
    if view == "stylish":
        return format_stylish(diff)
    elif view == "plain":
        return format_plain(diff)


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format", choices=['stylish', 'plain'],
                        default='stylish', help="set format of output")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
