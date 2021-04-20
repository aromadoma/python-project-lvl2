from gendiff.scripts.internal_diff import is_node, is_leaf, get_status, \
    get_value, get_old_value, get_children, has_complex_value, has_children


def format_plain(tree):
    print(f'TREE KEYS: {tree.keys()}')
    if is_leaf(tree):
        print(f'ITS A LEAF')
        if get_status(tree) in ['added', 'removed', 'updated']:
            return get_status(tree)
    print(f'ITS NOT A LEAF')

    path = map(format_plain, tree.keys())
    return list(path)
