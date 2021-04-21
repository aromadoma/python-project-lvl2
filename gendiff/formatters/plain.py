from gendiff.scripts.internal_diff import is_node, get_name, is_leaf, \
    get_status, get_value, get_old_value, get_children, has_children


def flatten(tree):
    result = []

    def walk(subtree):
        for item in subtree:
            if isinstance(item, list):
                walk(item)
            else:
                result.append(item)
    walk(tree)
    return result


def get_plain(node):

    def walk(subnode, path):
        print('Start walk')

        path += get_name(subnode)

        if is_leaf(subnode):
            output = {'path': path,
                      'status': get_status(subnode),
                      'value': get_value(subnode)
                      }
            print(f'Walk returns a dictionary {output}')
            return output

        print(f'NODE is {subnode}')
        children = get_children(subnode)
        nodes = []
        path += '.'
        for child in children:
            print(f'CHILD IS {child}')
            nodes.append(walk(child, path))

        return nodes

    return walk(node, '')


def format_plain(tree):
    print(f'Start format_plain')
    all_nodes = []
    for node in tree:
        all_nodes.append(get_plain(node))
    return flatten(all_nodes)
