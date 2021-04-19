import argparse
from gendiff.scripts.parser import parse
from gendiff.scripts.formatter import format_stylish


def generate_diff(file1_path, file2_path, view="stylish"):
    """Return diff in a specified format"""

    file1_data = parse(file1_path)
    file2_data = parse(file2_path)

    diff = get_inner_diff(file1_data, file2_data)

    if view == "stylish":
        return format_stylish(diff)
    elif view == "plain":
        pass

    return diff


def has_children(element):
    """Return True, if element has children (is dictionary)"""
    return isinstance(element, dict)


def get_added_keys_diff(data1, data2):
    diff = {}
    added_keys = data2.keys() - data1.keys()
    for key in added_keys:
        diff.update({key: {"type": "leaf",
                           "status": "added",
                           "value": data2[key]
                           }
                     })
    return diff


def get_removed_keys_diff(data1, data2):
    diff = {}
    removed_keys = data1.keys() - data2.keys()
    for key in removed_keys:
        diff.update({key: {"type": "leaf",
                           "status": "removed",
                           "value": data1[key]
                           }
                     })

    return diff


def get_common_keys_diff(data1, data2):
    diff = {}
    common_keys = data2.keys() & data1.keys()
    for key in common_keys:

        # Оба ключа содержат словари:
        if has_children(data1[key]) and has_children(data2[key]):
            children = get_inner_diff(data1[key], data2[key])
            diff.update({key: {"type": "node",
                               "children": children
                               }
                         })

        # Один ключ - словарь, второй - нет:
        elif has_children(data1[key]) != has_children(data2[key]):
            diff.update({key: {"type": "leaf",
                               "status": "updated",
                               "old_value": data1[key],
                               "value": data2[key]
                               }
                         })

        # Оба ключа не словари:
        elif data1[key] == data2[key]:
            diff.update({key: {"type": "leaf",
                               "status": "not_updated",
                               "value": data1[key]
                               }
                         })
        else:
            diff.update({key: {"type": "leaf",
                               "status": "updated",
                               "old_value": data1[key],
                               "value": data2[key]
                               }
                         })

    return diff


def get_inner_diff(data1, data2):

    diff = {}
    diff.update(get_added_keys_diff(data1, data2))
    diff.update(get_removed_keys_diff(data1, data2))
    diff.update(get_common_keys_diff(data1, data2))

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
