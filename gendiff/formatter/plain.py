from gendiff.formatter.tools import is_leaf, get_name, get_status, \
    get_value, get_old_value, get_children, has_complex_value, get_path, flatten


def format_value(value):
    """Return formatted value of leaf for plain view"""
    if has_complex_value(value):
        return '[complex value]'
    elif isinstance(value, str):
        return "'" + value + "'"
    else:
        return value


def get_diff(tree):
    def walk(subnode, path):
        path += get_name(subnode)
        if is_leaf(subnode):
            if get_status(subnode) == 'not_updated':
                return []
            return {'path': path,
                    'status': get_status(subnode),
                    'old_value': get_old_value(subnode),
                    'value': get_value(subnode)
                    }
        children = get_children(subnode)
        diff = [*map(lambda child: walk(child, path + '.'), children)]
        return diff

    return flatten(walk(tree, ''))


def format_plain(tree):
    """Return diff in plain view"""
    plain_view = ''
    diff = sorted(get_diff(tree), key=lambda k: k['path'])
    for node in diff:

        path = get_path(node)
        status = get_status(node)
        value = format_value(get_value(node))
        old_value = format_value(get_old_value(node))

        plain_view += f'Property {path} was {status}'
        if status == 'added':
            plain_view += f' with value {value}.\n'
        elif status == 'updated':
            plain_view += f'. From value {old_value} to {value}.\n'
        else:
            plain_view += '.\n'

    return plain_view
