import json

from gendiff.formatter.tools import is_leaf, get_name, get_status, \
    get_value, get_old_value, get_children, has_complex_value


def make_json_node(node):
    if is_leaf(node):
        status = get_status(node)
        if status == 'updated':
            return {"status": status,
                    "old_value": get_old_value(node),
                    "value": get_value(node)}
        elif status == 'not_updated':
            return get_value(node)
        return {"status": status,
                "value": get_value(node)}

    return get_diff(node)


def get_diff(tree):
    json_view = {}
    for child in get_children(tree):
        json_view[get_name(child)] = make_json_node(child)
    return json_view


def format_json(tree):
    return json.dumps(get_diff(tree), sort_keys=True, indent=2)

