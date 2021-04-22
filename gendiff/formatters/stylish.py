from gendiff.formatters.tools import is_leaf, get_name, get_status, \
    get_value, get_old_value, get_children, has_complex_value


def get_stylish_value(value, _depth):
    _margin = '  ' * _depth
    stylish_value = ''
    if not has_complex_value(value):
        stylish_value += f'{value}\n'
        return stylish_value

    stylish_value += '{\n'
    for key in value.keys():
        stylish_value += f'{_margin}  {key}: {get_stylish_value(value[key], _depth + 1)}'
    stylish_value += f'{_margin}'
    stylish_value += '}\n'

    return stylish_value


def get_stylish_leaf(leaf, _depth):
    stylish_leaf = ''
    _margin = '  ' * _depth
    if get_status(leaf) == 'removed':
        stylish_leaf += f'{_margin}- {get_name(leaf)}: '
        stylish_leaf += get_stylish_value(get_value(leaf), _depth + 1)
    elif get_status(leaf) == 'added':
        stylish_leaf += f'{_margin}+ {get_name(leaf)}: '
        stylish_leaf += get_stylish_value(get_value(leaf), _depth + 1)
    elif get_status(leaf) == 'updated':
        stylish_leaf += f'{_margin}- {get_name(leaf)}: '
        stylish_leaf += get_stylish_value(get_old_value(leaf), _depth + 1)
        stylish_leaf += f'{_margin}+ {get_name(leaf)}: '
        stylish_leaf += get_stylish_value(
            get_value(leaf), _depth + 1
        )
    else:
        stylish_leaf += \
            f'{_margin}  {get_name(leaf)}: {get_value(leaf)}\n'

    return stylish_leaf


def get_stylish_node(node, _depth):
    stylish_node = ''
    _margin = '  ' * _depth
    stylish_node += '{}  {}: {}'.format(
        _margin, get_name(node), format_stylish(node, _depth + 1)
    )
    return stylish_node


def format_stylish(tree, _depth=0):
    stylish_view = '{\n'
    _margin = '  ' * _depth

    children = get_children(tree)
    for child in sorted(children, key=lambda k: k['name']):

        # Обработка конечных узлов:
        if is_leaf(child):
            stylish_view += get_stylish_leaf(child, _depth + 1)

        # Обработка узлов с детьми:
        else:
            stylish_view += get_stylish_node(child, _depth + 1)

    stylish_view += f'{_margin}'
    stylish_view += '}\n'

    return stylish_view
