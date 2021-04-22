def is_leaf(element):
    """Return True, if element has type: leaf"""
    try:
        return element.get("type") == "leaf"
    except AttributeError:
        return None


def is_node(element):
    """Return True, if element has type: node"""
    try:
        return element.get("type") == "node"
    except AttributeError:
        return None


def get_name(element):
    """Return name of node"""
    return element.get("name")


def get_status(element):
    """Return status of leaf"""
    return element.get("status")


def get_value(element):
    """Return value of leaf"""
    return element.get("value")


def get_old_value(element):
    """Return old value of leaf"""
    return element.get("old_value")


def get_children(element):
    """Return children of node"""
    return element.get("children")


def has_complex_value(element):
    """Return True, if value (element) is dictionary"""
    try:
        return isinstance(element, dict)
    except AttributeError:
        return None


def get_path(element):
    """Return path of node"""
    return element.get('path').lstrip('.')


def flatten(tree):
    """Return flatten list"""
    result = []

    def walk(subtree):
        for item in subtree:
            if isinstance(item, list):
                walk(item)
            else:
                result.append(item)
    walk(tree)
    return result
