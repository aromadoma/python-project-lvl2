def is_node(element):
    """Return True, if element has type: node"""
    return element["type"] == "node"


def is_leaf(element):
    """Return True, if element has type: leaf"""
    return element["type"] == "leaf"


def get_status(element):
    """Return status of leaf element"""
    return element.get("status")


def get_value(element):
    """Return value of leaf element"""
    return element.get("value")


def get_old_value(element):
    """Return value of leaf element"""
    return element.get("old_value")


def format_stylish(diff):

    stylish_view = '{\n'

    for key in diff.keys():
        if is_leaf(diff[key]):
            if get_status(diff[key]) == 'removed':
                stylish_view += f'  - {key}: {get_value(diff[key])}\n'
            elif get_status(diff[key]) == 'added':
                stylish_view += f'  + {key}: {get_value(diff[key])}\n'
            elif get_status(diff[key]) == 'updated':
                stylish_view += f'  - {key}: {get_old_value(diff[key])}\n'
                stylish_view += f'  + {key}: {get_value(diff[key])}\n'
            else:
                stylish_view += f'    {key}: {get_value(diff[key])}\n'

    stylish_view += '}'

    return stylish_view


def format_plain(diff):
    pass
