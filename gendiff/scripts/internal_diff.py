def get_value(tree, child):
    """Return a dictionary's key value"""
    return tree[child]


def get_children(tree):
    """Return 'dict_keys' object"""
    return tree.keys()


def get_all_children(tree1, tree2):
    """Return all unique children names from both trees"""
    children = set(get_children(tree1))
    children.update(set(get_children(tree2)))
    return children


def common_children(tree1, tree2):
    """Return a list with children that both of trees have"""
    return get_children(tree1) & get_children(tree2)


def removed_children(tree1, tree2):
    """Return a list with children that only the first tree has"""
    return get_children(tree1) - get_children(tree2)


def added_children(tree1, tree2):
    """Return a list with children that only the second tree has"""
    return get_children(tree2) - get_children(tree1)


def make_node(name, type=None, status=None, old_value=None, value=None, children=[]):
    """Return dictionary with node data"""
    return {"name": name, "type": type,
            "status": status,
            "old_value": old_value,
            "value": value,
            "children": children}


def make_common_node(tree1, tree2, child):
    value1 = get_value(tree1, child)
    value2 = get_value(tree2, child)
    # Значения - словари:
    if isinstance(value1, dict) and isinstance(value2, dict):
        return make_node(child,
                         type='node',
                         children=make_diff(value1, value2))
    # Значение - не словарь и оно не было изменено:
    elif value1 == value2:
        return make_node(child,
                         type='leaf',
                         status='not_updated',
                         value=value1)
    # Значения были изменены:
    else:
        return make_node(child,
                         type='leaf',
                         status='updated',
                         old_value=value1,
                         value=value2)


def make_diff(tree1, tree2):
    """Return diff between two trees"""
    children = get_all_children(tree1, tree2)
    diff = []

    for child in children:
        if child in removed_children(tree1, tree2):
            value = get_value(tree1, child)
            diff.append(make_node(child, type='leaf', status='removed', value=value))
        elif child in added_children(tree1, tree2):
            value = get_value(tree2, child)
            diff.append(make_node(child, type='leaf', status='added', value=value))
        elif child in common_children(tree1, tree2):
            diff.append(make_common_node(tree1, tree2, child))

    return diff


def get_internal_diff(tree1, tree2):
    """Return diff in internal view"""
    return make_node('', children=make_diff(tree1, tree2))
