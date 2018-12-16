from collections import defaultdict


class union_find(object):

    def __init__(self, num_elements):
        self.parents = list(range(num_elements))
        self.size_component = [1] * num_elements
        self.num_elements = num_elements
        self.num_components = num_elements

    def find(self, idx):
        # find its root first
        root = idx
        while root != self.parents[root]:
            root = self.parents[root]

        # path compression
        while idx != root:
            idx_next = self.parents[idx]
            self.parents[idx] = root
            idx = idx_next

        # return the root
        return root

    def union(self, i1, i2):
        root1 = self.find(i1)
        root2 = self.find(i2)
        if root1 == root2: return

        if self.size_component[root1] < self.size_component[root2]:
            self.size_component[root2] += self.size_component[root1]
            self.parents[root1] = root2
        else:
            self.size_component[root1] += self.size_component[root2]
            self.parents[root2] = root1

        self.num_components -= 1

    def print_clusters(self):
        clusters = defaultdict(list)
        for i in range(self.num_elements):
            root = self.find(i)
            clusters[root].append(i)

        for root, children in clusters.items():
            print(children)

        print("Number of components = {}".format(self.num_components))


if __name__ == "__main__":
    union_find_inst = union_find(10)
    union_find_inst.union(0, 2)
    union_find_inst.union(0, 4)
    union_find_inst.union(4, 8)
    union_find_inst.union(9, 7)
    union_find_inst.union(3, 5)
    union_find_inst.print_clusters()
