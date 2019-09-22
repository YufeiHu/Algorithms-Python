class tree_node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class binary_search_tree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = tree_node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val <= node.val:
            if node.left:
                self._insert(node.left, val)
            else:
                node.left = tree_node(val)
        else:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = tree_node(val)

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node: return None

        if node.val > val:
            node.left = self._delete(node.left, val)
            return node
        elif node.val < val:
            node.right = self._delete(node.right, val)
            return node
        else:
            if not node.left: return node.right
            if not node.right: return node.left
            node_left = self._find_left_most(node.right)
            node_left.left = node.left
            return node.right

    def _find_left_most(self, root):
        while root.left:
            root = root.left
        return root

    def find(self, val):
        return self._find(self.root, val)

    def _find(self, node, val):
        if not node: return False

        if val == node.val:
            return True
        elif val < node.val:
            return self._find(node.left, val)
        else:
            return self._find(node.right, val)

    def print_tree(self):
        ans = list()
        self._print(self.root, ans)
        print(", ".join(ans))

    def _print(self, node, ans):
        if not node: return
        self._print(node.left, ans)
        ans.append(str(node.val))
        self._print(node.right, ans)


if __name__ == "__main__":
    binary_search_tree_inst = binary_search_tree()

    binary_search_tree_inst.insert(5)
    binary_search_tree_inst.insert(1)
    binary_search_tree_inst.insert(6)
    binary_search_tree_inst.insert(2)
    binary_search_tree_inst.insert(2)
    binary_search_tree_inst.insert(0)
    binary_search_tree_inst.print_tree()

    binary_search_tree_inst.delete(2)
    binary_search_tree_inst.delete(5)
    binary_search_tree_inst.delete(6)
    binary_search_tree_inst.print_tree()
