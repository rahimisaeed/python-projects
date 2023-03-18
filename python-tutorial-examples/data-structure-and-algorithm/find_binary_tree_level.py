from build_binary_tree import build_bst


def depth(tree_node):
    # queue = [tree]
    # level = len(queue)
    if tree_node is None:
        return 0
    else:
        left_depth = depth(tree_node["left_child"])
        right_depth = depth(tree_node["right_child"])
        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1


# build binary trees to test the level finder algorithm
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

# test binary trees
print(depth(tree_level_1) == 1)
print(depth(tree_level_2) == 2)
print(depth(tree_level_4) == 4)
