from gendiff.scripts.internal_diff import is_node, is_leaf, get_status, \
    get_value, get_old_value, get_children, has_complex_value


def get_stylish_leaf_value(value, _depth):
    stylish_leaf_value = ''
    _margin = '  ' * _depth
    if has_complex_value(value):
        stylish_leaf_value += f'{format_stylish(value, _depth + 1)}'
    else:
        stylish_leaf_value += f'{value}\n'
    return stylish_leaf_value


def get_stylish_leaf(tree, node, _depth):
    stylish_leaf_view = ''
    _margin = '  ' * _depth
    if get_status(tree[node]) == 'removed':
        stylish_leaf_view += f'{_margin}- {node}: '
        stylish_leaf_view += get_stylish_leaf_value(
            get_value(tree[node]), _depth
        )
    elif get_status(tree[node]) == 'added':
        stylish_leaf_view += f'{_margin}+ {node}: '
        stylish_leaf_view += get_stylish_leaf_value(
            get_value(tree[node]), _depth
        )
    elif get_status(tree[node]) == 'updated':
        stylish_leaf_view += f'{_margin}- {node}: '
        stylish_leaf_view += get_stylish_leaf_value(
            get_old_value(tree[node]), _depth
        )
        stylish_leaf_view += f'{_margin}+ {node}: '
        stylish_leaf_view += get_stylish_leaf_value(
            get_value(tree[node]), _depth
        )
    else:
        stylish_leaf_view += \
            f'{_margin}  {node}: {get_value(tree[node])}\n'

    return stylish_leaf_view


def get_stylish_complex_values(tree, node, _depth):
    stylish_complex_values_view = ''
    _margin = '  ' * _depth
    if has_complex_value(tree[node]):
        stylish_complex_values_view += '{}  {}: {}'.format(
           _margin, node, format_stylish(tree[node], _depth + 1)
        )
    else:
        stylish_complex_values_view += '{}  {}: {}\n'.format(
            _margin, node, tree[node]
        )
    return stylish_complex_values_view


def get_stylish_node(tree, node, _depth):
    stylish_node_view = ''
    _margin = '  ' * _depth
    stylish_node_view += '{}  {}: {}'.format(
        _margin, node, format_stylish(get_children(tree[node]), _depth + 1)
    )
    return stylish_node_view


def format_stylish(tree, _depth=1):
    stylish_view = '{\n'
    for node in sorted(tree.keys()):
        # Обработка конечных узлов:
        if is_leaf(tree[node]):
            stylish_view += get_stylish_leaf(tree, node, _depth)
        # Обработка узлов с детьми:
        elif is_node(tree[node]):
            stylish_view += get_stylish_node(tree, node, _depth)
        # Обработка complex values:
        else:
            stylish_view += get_stylish_complex_values(tree, node, _depth)

    stylish_view += f'{"  " * (_depth - 1)}'
    stylish_view += '}\n'

    return stylish_view
