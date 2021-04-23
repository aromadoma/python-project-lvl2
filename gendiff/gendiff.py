import argparse
from gendiff.parser import parse
from gendiff.internal_diff import get_internal_diff
from gendiff.formatter.stylish import format_stylish
from gendiff.formatter.plain import format_plain
from gendiff.formatter.json import format_json


def generate_diff(file1_path, file2_path, view="stylish"):
    """Return diff in a specified format"""
    file1_data = parse(file1_path)
    file2_data = parse(file2_path)
    diff = get_internal_diff(file1_data, file2_data)
    if view == "stylish":
        return format_stylish(diff)
    elif view == "plain":
        return format_plain(diff)
    elif view == "json":
        return format_json(diff)


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('file1')
    parser.add_argument('file2')
    parser.add_argument("-f", "--format", choices=['stylish', 'plain', 'json'],
                        default='stylish', help="set format of output")
    args = parser.parse_args()
    print(generate_diff(args.file1, args.file2, args.format))


if __name__ == '__main__':
    main()
