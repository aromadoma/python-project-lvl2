from gendiff.scripts.internal_diff import is_node, is_leaf, get_status, \
    get_value, get_old_value, get_children, get_name, has_complex_value


def get_stylish_value(value, _depth):
    _margin = '  ' * _depth
    stylish_value = ''
    if not has_complex_value(value):
        stylish_value += f'{value}\n'
        return stylish_value

    stylish_value += '{\n'
    for key in value.keys():
        stylish_value += f'{_margin}  {key}: ' \
                         f'{get_stylish_value(value[key], _depth + 1)}'
    stylish_value += f'{_margin}'
    stylish_value += '}\n'

    return stylish_value


def get_stylish_leaf(node, _depth):
    stylish_leaf_view = ''
    _margin = '  ' * _depth
    if get_status(node) == 'removed':
        stylish_leaf_view += f'{_margin}- {get_name(node)}: '
        stylish_leaf_view += get_stylish_value(
            get_value(node), _depth + 1
        )
    elif get_status(node) == 'added':
        stylish_leaf_view += f'{_margin}+ {get_name(node)}: '
        stylish_leaf_view += get_stylish_value(get_value(node), _depth + 1)
    elif get_status(node) == 'updated':
        stylish_leaf_view += f'{_margin}- {get_name(node)}: '
        stylish_leaf_view += get_stylish_value(
            get_old_value(node), _depth + 1
        )
        stylish_leaf_view += f'{_margin}+ {get_name(node)}: '
        stylish_leaf_view += get_stylish_value(
            get_value(node), _depth + 1
        )
    else:
        stylish_leaf_view += \
            f'{_margin}  {get_name(node)}: {get_value(node)}\n'

    return stylish_leaf_view


def get_stylish_node(node, _depth):
    stylish_node_view = ''
    _margin = '  ' * _depth
    stylish_node_view += '{}  {}: {}'.format(
        _margin, get_name(node), format_stylish(get_children(node), _depth + 1)
    )
    return stylish_node_view


def format_stylish(tree, _depth=0):
    stylish_view = '{\n'
    _margin = '  ' * _depth
    for node in sorted(tree, key=lambda k: k['name']):

        # Обработка конечных узлов:
        if is_leaf(node):
            stylish_view += get_stylish_leaf(node, _depth + 1)
        # Обработка узлов с детьми:
        elif is_node(node):
            stylish_view += get_stylish_node(node, _depth + 1)

    stylish_view += f'{_margin}'
    stylish_view += '}\n'

    return stylish_view
