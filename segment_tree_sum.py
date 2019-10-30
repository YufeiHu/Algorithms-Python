class Node:
    def __init__(self, i_l, i_r):
        self.i_l = i_l
        self.i_r = i_r
        self.total = 0
        self.ptr_l = None
        self.ptr_r = None


class segment_tree_sum:
    def __init__(self, nums):
        def createTree(nums, i_l, i_r):
            if i_l > i_r:
                return None

            if i_l == i_r:
                node = Node(i_l, i_r)
                node.total = nums[i_l]
                return node

            i_m = (i_l + i_r) // 2
            node_l = createTree(nums, i_l, i_m)
            node_r = createTree(nums, i_m + 1, i_r)
            node = Node(i_l, i_r)
            node.total = node_l.total + node_r.total
            node.ptr_l = node_l
            node.ptr_r = node_r
            return node

        self.root = createTree(nums, 0, len(nums) - 1)


    def update(self, i, val):
        def updateTree(node, i, val):
            if node.i_l == node.i_r:
                node.total = val
                return

            i_m = (node.i_l + node.i_r) // 2
            if i <= i_m:
                updateTree(node.ptr_l, i, val)
            elif i >= i_m + 1:
                updateTree(node.ptr_r, i, val)

            node.total = node.ptr_l.total + node.ptr_r.total

        updateTree(self.root, i, val)


    def sumRange(self, i, j):
        def sumTree(node, j_l, j_r):
            if node.i_l == j_l and node.i_r == j_r:
                return node.total

            i_m = (node.i_l + node.i_r) // 2
            if j_r <= i_m:
                return sumTree(node.ptr_l, j_l, j_r)
            elif j_l >= i_m + 1:
                return sumTree(node.ptr_r, j_l, j_r)
            else:
                return sumTree(node.ptr_l, j_l, i_m) + sumTree(node.ptr_r, i_m + 1, j_r)

        return sumTree(self.root, i, j)


if __name__ == "__main__":
    segment_tree_sum_inst = segment_tree_sum([1, 3, 5])
    print(segment_tree_sum_inst.sumRange(0, 2))
    segment_tree_sum_inst.update(1, 2)
    print(segment_tree_sum_inst.sumRange(0, 2))
    
