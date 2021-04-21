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


def is_complex(element):
    return not is_leaf(element) and not is_node(element)


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


def get_added_keys_diff(tree1, tree2):
    """Return internal diff for added keys"""
    diff = []
    added_keys = tree2.keys() - tree1.keys()
    for key in added_keys:
        diff.append({"name": key,
                     "type": "leaf",
                     "status": "added",
                     "value": tree2[key]})
    return diff


def get_removed_keys_diff(tree1, tree2):
    """Return internal diff for removed keys"""
    diff = []
    removed_keys = tree1.keys() - tree2.keys()
    for key in removed_keys:
        diff.append({"name": key,
                     "type": "leaf",
                     "status": "removed",
                     "value": tree1[key]
                     })
    return diff


def get_common_keys_diff(tree1, tree2):
    """Return internal diff for common keys"""
    diff = []
    common_keys = tree2.keys() & tree1.keys()
    for key in common_keys:
        # Both keys are dictionaries:
        if has_children(tree1[key]) and has_children(tree2[key]):
            children = get_internal_diff(tree1[key], tree2[key])
            diff.append({"name": key,
                         "type": "node",
                         "children": children
                         })
        # One of key is dictionary, another isn't:
        elif has_children(tree1[key]) != has_children(tree2[key]):
            diff.append({"name": key,
                         "type": "leaf",
                         "status": "updated",
                         "old_value": tree1[key],
                         "value": tree2[key]
                         })
        # Both keys aren't dictionaries, there was NO update:
        elif tree1[key] == tree2[key]:
            diff.append({"name": key,
                         "type": "leaf",
                         "status": "not_updated",
                         "value": tree1[key]
                         })
        # Both keys aren't dictionaries, there was an update:
        else:
            diff.append({"name": key,
                         "type": "leaf",
                         "status": "updated",
                         "old_value": tree1[key],
                         "value": tree2[key]
                         })
    return diff


def get_internal_diff(tree1, tree2):
    """Return diff in internal view"""
    diff = []
    diff.extend(get_added_keys_diff(tree1, tree2))
    diff.extend(get_removed_keys_diff(tree1, tree2))
    diff.extend(get_common_keys_diff(tree1, tree2))
    # diff[0]['children'].append(get_added_keys_diff(tree1, tree2))
    # diff[0]['children'].append(get_removed_keys_diff(tree1, tree2))
    # diff[0]['children'].append(get_common_keys_diff(tree1, tree2))

    print('*******************INTERNAL DIFF************************')
    print(diff)
    # print(diff)
    # return {'name': '', 'type': 'node', 'children': [diff]}
    return diff
