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


def get_name(element):
    """Return name of element"""
    return element.get("name")


def get_status(element):
    """Return status of leaf element"""
    return element.get("status")


def get_value(element):
    """Return value of leaf element"""
    return element.get("value")


def get_old_value(element):
    """Return value of leaf element"""
    return element.get("old_value")


def format_value(value):
    if has_complex_value(value):
        return '[complex value]'
    elif isinstance(value, str):
        return "'" + value + "'"
    else:
        return value


def get_path(element):
    return element.get('path').lstrip('.')


def get_children(element):
    """Return children of node element"""
    return element.get("children")


def has_complex_value(element):
    """Return True, if value (element) is dictionary"""
    try:
        return isinstance(element, dict)
    except AttributeError:
        return None


def has_children(element):
    """Return True, if element has children (is dictionary)"""
    return isinstance(element, dict)


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
