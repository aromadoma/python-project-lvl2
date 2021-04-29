from gendiff.formatter.tools import is_leaf, get_name, get_status, \
    get_value, get_old_value, get_children, has_complex_value


def make_stylish_value(value, _depth):
    """Return value of leaf in stylish view"""
    _margin = '  ' * _depth
    _prev_margin = '  ' * (_depth - 1)
    if not has_complex_value(value):
        return f'{value}\n'
    stylish_value = '{\n'
    for key in value.keys():
        stylish_value += f'{_margin}  {key}: {make_stylish_value(value[key], _depth + 2)}'
    return stylish_value + f'{_prev_margin}' + '}\n'


def make_stylish_leaf(leaf, _depth):
    """Return leaf in stylish view"""
    _margin = '  ' * _depth
    if get_status(leaf) == 'removed':
        return f'{_margin}- {get_name(leaf)}: ' \
               f'{make_stylish_value(get_value(leaf), _depth + 2)}'
    elif get_status(leaf) == 'added':
        return f'{_margin}+ {get_name(leaf)}: ' \
               f'{make_stylish_value(get_value(leaf), _depth + 2)}'
    elif get_status(leaf) == 'updated':
        return f'{_margin}- {get_name(leaf)}: ' \
               f'{make_stylish_value(get_old_value(leaf), _depth + 2)}' \
               f'{_margin}+ {get_name(leaf)}: ' \
               f'{make_stylish_value(get_value(leaf), _depth + 2)}'
    else:
        return f'{_margin}  {get_name(leaf)}: {get_value(leaf)}\n'


def make_stylish_node(node, _depth):
    """Return node in stylish view"""
    _margin = '  ' * _depth
    return f'{_margin}  {get_name(node)}: {format_stylish(node, _depth + 1)}'


def format_stylish(tree, _depth=0):
    """Return diff in stylish view"""
    stylish_view = '{\n'
    _margin = '  ' * _depth

    children = get_children(tree)
    for child in sorted(children, key=lambda k: k['name']):
        # Обработка конечных узлов:
        if is_leaf(child):
            stylish_view += make_stylish_leaf(child, _depth + 1)
        # Обработка узлов с детьми:
        else:
            stylish_view += make_stylish_node(child, _depth + 1)

    stylish_view = stylish_view + f'{_margin}' + '}\n'
    return stylish_view
