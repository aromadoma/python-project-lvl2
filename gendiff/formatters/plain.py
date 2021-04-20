from gendiff.scripts.internal_diff import is_node, get_name, is_leaf, \
    get_status, get_value, get_old_value, get_children, has_children


def get_plain(node):

    def walk(node, path):
        print('Start walk')

        path += get_name(node)

        if is_leaf(node):
            output = {'path': path, 'status': get_status(node), 'value': get_value(node)}
            print(f'Walk returns a dictionary {output}')
            return output

        print(f'NODE is {node}')
        children = get_children(node)
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
    return all_nodes
