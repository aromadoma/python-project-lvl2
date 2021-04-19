def is_node(element):
    """Return True, if element has type: node"""
    try:
        return element.get("type") == "node"
    except AttributeError:
        return None


def is_leaf(element):
    """Return True, if element has type: leaf"""
    try:
        return element.get("type") == "leaf"
    except AttributeError:
        return None


def get_status(element):
    """Return status of leaf element"""
    return element.get("status")


def get_value(element):
    """Return value of leaf element"""
    return element.get("value")


def get_old_value(element):
    """Return value of leaf element"""
    return element.get("old_value")


def get_children(element):
    """Return children of node element"""
    return element.get("children")


def has_complex_value(element):
    """Return True, if value is dictionary"""
    try:
        return isinstance(element, dict)
    except AttributeError:
        return None


def get_stylish_leaf(tree, node, _margin):
    stylish_leaf_view = ''
    _next_margin = _margin + 2
    if get_status(tree[node]) == 'removed':
        stylish_leaf_view += f'{"  " * _margin}- {node}: '
        if has_complex_value(get_value(tree[node])):
            stylish_leaf_view += \
                f'{format_stylish(get_value(tree[node]), _next_margin)}'
        else:
            stylish_leaf_view += f'{get_value(tree[node])}\n'
    elif get_status(tree[node]) == 'added':
        stylish_leaf_view += f'{"  " * _margin}+ {node}: '
        if has_complex_value(get_value(tree[node])):
            stylish_leaf_view += \
                f'{format_stylish(get_value(tree[node]), _next_margin)}'
        else:
            stylish_leaf_view += f'{get_value(tree[node])}\n'
    elif get_status(tree[node]) == 'updated':
        stylish_leaf_view += f'{"  " * _margin}- {node}: '
        if has_complex_value(get_old_value(tree[node])):
            stylish_leaf_view += '{}\n'.format(
                format_stylish(get_old_value(tree[node]), _next_margin))
        else:
            stylish_leaf_view += f'{get_old_value(tree[node])}\n'
        stylish_leaf_view += f'{"  " * _margin}+ {node}: '
        if has_complex_value(get_value(tree[node])):
            stylish_leaf_view += \
                f'{format_stylish(tree[node], _next_margin)}\n'
        else:
            stylish_leaf_view += f'{get_value(tree[node])}\n'
    else:
        stylish_leaf_view += \
            f'{"  " * _margin}  {node}: {get_value(tree[node])}\n'

    return stylish_leaf_view


def get_stylish_complex_values(tree, node, _margin):
    stylish_complex_values_view = ''
    _next_margin = _margin + 2
    if isinstance(tree[node], dict):
        stylish_complex_values_view += f'{"  " * _margin}  {node}: {format_stylish(tree[node], _next_margin)}'
    else:
        stylish_complex_values_view += f'{"  " * _margin}  {node}: {tree[node]}\n'
    return stylish_complex_values_view


def get_stylish_node(tree, node, _margin):
    stylish_node_view = ''
    _next_margin = _margin + 2
    stylish_node_view += '{}  {}: {}'.format(
        "  " * _margin, node,
        format_stylish(get_children(tree[node]), _next_margin)
    )
    return stylish_node_view


def format_stylish(tree, _margin=1):

    _next_margin = _margin + 2
    stylish_view = '{\n'
    for node in sorted(tree.keys()):

        # Обработка конечных узлов:
        if is_leaf(tree[node]):
            # if get_status(tree[node]) == 'removed':
            #     stylish_view += f'{"  " * _margin}- {node}: '
            #     if has_complex_value(get_value(tree[node])):
            #         stylish_view += \
            #             f'{format_stylish(get_value(tree[node]), _next_margin)}'
            #     else:
            #         stylish_view += f'{get_value(tree[node])}\n'
            # elif get_status(tree[node]) == 'added':
            #     stylish_view += f'{"  " * _margin}+ {node}: '
            #     if has_complex_value(get_value(tree[node])):
            #         stylish_view +=\
            #             f'{format_stylish(get_value(tree[node]), _next_margin)}'
            #     else:
            #         stylish_view += f'{get_value(tree[node])}\n'
            # elif get_status(tree[node]) == 'updated':
            #     stylish_view += f'{"  " * _margin}- {node}: '
            #     if has_complex_value(get_old_value(tree[node])):
            #         stylish_view += '{}\n'.format(
            #             format_stylish(get_old_value(tree[node]), _next_margin))
            #     else:
            #         stylish_view += f'{get_old_value(tree[node])}\n'
            #     stylish_view += f'{"  " * _margin}+ {node}: '
            #     if has_complex_value(get_value(tree[node])):
            #         stylish_view +=\
            #             f'{format_stylish(tree[node], _next_margin)}\n'
            #     else:
            #         stylish_view += f'{get_value(tree[node])}\n'
            # else:
            #     stylish_view += \
            #         f'{"  " * _margin}  {node}: {get_value(tree[node])}\n'
            stylish_view += get_stylish_leaf(tree, node, _margin)

        # Обработка узлов с детьми:
        elif is_node(tree[node]):
            stylish_view += get_stylish_node(tree, node, _margin)

        # Обработка complex values:
        else:
            stylish_view += get_stylish_complex_values(tree, node, _margin)

    stylish_view += f'{"  " * (_margin - 1)}'
    stylish_view += '}\n'

    return stylish_view


def format_plain(diff):
    pass
