from gendiff.scripts.internal_diff import is_node, is_leaf, get_status, \
    get_value, get_old_value, get_children, get_name, is_complex


def get_stylish_value(value, _depth):
    print(f'get_stylish_value start')
    stylish_value = ''
    _margin = '  ' * _depth
    # if has_complex_value(value):
    #     stylish_value += f'{format_test(value, _depth + 1)}'
    # else:
    #     stylish_value += f'{value}\n'
    stylish_value += f'{value}\n'
    print(f'STYLISH LEAF VALUE:\n{stylish_value}\n')
    return stylish_value


def get_stylish_leaf(node, _depth):
    print(f'get_stylish_leaf start')
    stylish_leaf_view = ''
    _margin = '  ' * _depth
    if get_status(node) == 'removed':
        stylish_leaf_view += f'{_margin}- {get_name(node)}: '
        stylish_leaf_view += get_stylish_value(
            get_value(node), _depth
        )
    elif get_status(node) == 'added':
        stylish_leaf_view += f'{_margin}+ {get_name(node)}: '
        stylish_leaf_view += get_stylish_value(
            get_value(node), _depth
        )
    elif get_status(node) == 'updated':
        stylish_leaf_view += f'{_margin}- {get_name(node)}: '
        stylish_leaf_view += get_stylish_value(
            get_old_value(node), _depth
        )
        stylish_leaf_view += f'{_margin}+ {get_name(node)}: '
        stylish_leaf_view += get_stylish_value(
            get_value(node), _depth
        )
    else:
        stylish_leaf_view += \
            f'{_margin}  {get_name(node)}: {get_value(node)}\n'

    print(f'STYLISH LEAF:\n{stylish_leaf_view}\n')
    return stylish_leaf_view


# def get_stylish_complex_values(node, _depth):
#     print(f'get_stylish_complex_values start')
#     stylish_complex_values_view = ''
#     _margin = '  ' * _depth
#     if has_complex_value(node):
#         stylish_complex_values_view += '{}  {}: {}'.format(
#            _margin, node, format_test(node, _depth + 1)
#         )
#     else:
#         stylish_complex_values_view += '{}  {}: {}\n'.format(
#             _margin, get_name(node), node
#         )
#     print(f'STYLISH COMPLEX:\n{stylish_complex_values_view}\n')
#     return stylish_complex_values_view


def get_stylish_node(node, _depth):
    print(f'get_stylish_node start')
    stylish_node_view = ''
    _margin = '  ' * _depth
    stylish_node_view += '{}  {}: {}'.format(
        _margin, node, format_test(get_children(node), _depth + 1)
    )
    print(f'STYLISH NODE:\n{stylish_node_view}\n')
    return stylish_node_view


def format_test(tree, _depth=1):
    stylish_view = '{\n'
    print(f'TREE IS {tree}')
    for node in sorted(tree, key=lambda k: k['name']):
        print(f'NODE IS {node}')
        # Обработка конечных узлов:
        if is_leaf(node):
            print(f'is_leaf(node) func')
            stylish_view += get_stylish_leaf(node, _depth)
        # Обработка узлов с детьми:
        elif is_node(node):
            print(f'is_node(node) func')
            stylish_view += get_stylish_node(node, _depth)
        # Обработка complex values:
        # else:
        #     print(f'complex values func')
        #     stylish_view += get_stylish_complex_values(node, _depth)

    stylish_view += f'{"  " * (_depth - 1)}'
    stylish_view += '}\n'

    return stylish_view
