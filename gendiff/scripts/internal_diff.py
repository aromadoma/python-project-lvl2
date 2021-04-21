def get_children(tree):
    return tree.keys()


def get_children_set(tree1, tree2):
    children_set = set(get_children(tree1))
    children_set.update(set(get_children(tree2)))
    return children_set


def get_value(tree, child):
    return tree[child]


def get_common_children(tree1, tree2):
    return get_children(tree1) & get_children(tree2)


def get_removed_children(tree1, tree2):
    return get_children(tree1) - get_children(tree2)


def get_added_children(tree1, tree2):
    return get_children(tree2) - get_children(tree1)


def make_node(name, children):
    return {"name": name, "type": "node", "children": children}


def make_leaf_added(name, value):
    return {"name": name, "type": "leaf", "status": "added", "value": value}


def make_leaf_removed(name, value):
    return {"name": name, "type": "leaf", "status": "removed", "value": value}


def make_leaf_common(tree1, tree2, child):
    value1 = get_value(tree1, child)
    value2 = get_value(tree2, child)
    if isinstance(value1, dict) and isinstance(value2, dict):
        return {"name": child,
                "type": "node",
                "children": make_diff(value1, value2)
                }
    elif value1 == value2:
        return {"name": child,
                "type": "leaf",
                "status": "not_updated",
                "value": value1
                }
    else:
        return {"name": child,
                "type": "leaf",
                "status": "updated",
                "old_value": value1,
                "value": value2
                }


def make_diff(tree1, tree2):
    children = get_children_set(tree1, tree2)
    common_children = get_common_children(tree1, tree2)
    removed_children = get_removed_children(tree1, tree2)
    added_children = get_added_children(tree1, tree2)

    diff = []

    for child in children:
        if child in removed_children:
            value = get_value(tree1, child)
            diff.append(make_leaf_removed(child, value))
        elif child in added_children:
            value = get_value(tree2, child)
            diff.append(make_leaf_removed(child, value))
        elif child in common_children:
            diff.append(make_leaf_common(tree1, tree2, child))

    return diff


def get_internal_diff(tree1, tree2):
    """Return diff in internal view"""
    return make_node('', make_diff(tree1, tree2))
