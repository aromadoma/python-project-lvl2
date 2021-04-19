import argparse
from gendiff.scripts.parser import parse
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain


def generate_diff(file1_path, file2_path, view="stylish"):
    """Return diff in a specified format"""

    file1_data = parse(file1_path)
    file2_data = parse(file2_path)
    diff = get_inner_diff(file1_data, file2_data)
    if view == "stylish":
        return format_stylish(diff)
    elif view == "plain":
        return format_plain(diff)


def has_children(element):
    """Return True, if element has children (is dictionary)"""
    return isinstance(element, dict)


def get_added_keys_diff(tree1, tree2):
    diff = {}
    added_keys = tree2.keys() - tree1.keys()
    for key in added_keys:
        diff.update({key: {"type": "leaf",
                           "status": "added",
                           "value": tree2[key]
                           }
                     })
    return diff


def get_removed_keys_diff(tree1, tree2):
    diff = {}
    removed_keys = tree1.keys() - tree2.keys()
    for key in removed_keys:
        diff.update({key: {"type": "leaf",
                           "status": "removed",
                           "value": tree1[key]
                           }
                     })
    return diff


def get_common_keys_diff(tree1, tree2):
    diff = {}
    common_keys = tree2.keys() & tree1.keys()
    for key in common_keys:

        # Оба ключа содержат словари:
        if has_children(tree1[key]) and has_children(tree2[key]):
            children = get_inner_diff(tree1[key], tree2[key])
            diff.update({key: {"type": "node",
                               "children": children
                               }
                         })
        # Один ключ - словарь, второй - нет:
        elif has_children(tree1[key]) != has_children(tree2[key]):
            diff.update({key: {"type": "leaf",
                               "status": "updated",
                               "old_value": tree1[key],
                               "value": tree2[key]
                               }
                         })
        # Оба ключа не словари, изменения не было:
        elif tree1[key] == tree2[key]:
            diff.update({key: {"type": "leaf",
                               "status": "not_updated",
                               "value": tree1[key]
                               }
                         })
        # Оба ключа не словари, изменение было:
        else:
            diff.update({key: {"type": "leaf",
                               "status": "updated",
                               "old_value": tree1[key],
                               "value": tree2[key]
                               }
                         })

    return diff


def get_inner_diff(tree1, tree2):

    diff = {}
    diff.update(get_added_keys_diff(tree1, tree2))
    diff.update(get_removed_keys_diff(tree1, tree2))
    diff.update(get_common_keys_diff(tree1, tree2))

    return diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format", default='stylish', help="set format of output")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
