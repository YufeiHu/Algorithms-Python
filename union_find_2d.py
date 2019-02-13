from collections import defaultdict

class union_find_2d(object):
    def __init__(self, height, width):
        self.parents = dict()
        self.size_component = dict()
        for y in range(height):
            for x in range(width):
                self.parents[(y, x)] = (-1, -1)
                self.size_component[(y, x)] = 0
        self.num_islands = 0
        self.area_max = 0
        self.height = height
        self.width = width

    def find(self, pos):
        if self.parents[pos] == (-1, -1):
            return (-1, -1)

        root = pos
        while root != self.parents[root]:
            root = self.parents[root]

        while pos != root:
            pos_next = self.parents[pos]
            self.parents[pos] = root
            pos = pos_next
        return root

    def union(self, pos1, pos2):
        if pos1 == pos2:
            root = self.parents[pos1]
            if root == (-1, -1):
                self.parents[pos1] = pos1
                self.size_component[pos1] = 1
                self.num_islands += 1
                self.area_max = max(self.area_max, 1)
            return

        root1 = self.find(pos1)
        if root1 == (-1, -1):
            self.parents[pos1] = pos1
            self.size_component[pos1] = 1
            root1 = pos1
            self.num_islands += 1

        root2 = self.find(pos2)
        if root2 == (-1, -1):
            self.parents[pos2] = pos2
            self.size_component[pos2] = 1
            root2 = pos2
            self.num_islands += 1

        if root1 == root2: return

        if self.size_component[root1] < self.size_component[root2]:
            self.size_component[root2] += self.size_component[root1]
            self.area_max = max(self.area_max, self.size_component[root2])
            self.parents[root1] = root2
        else:
            self.size_component[root1] += self.size_component[root2]
            self.area_max = max(self.area_max, self.size_component[root1])
            self.parents[root2] = root1

        self.num_islands -= 1

    def print_clusters(self):
        clusters = defaultdict(list)
        for y in range(self.height):
            for x in range(self.width):
                root = self.find((y, x))
                if root != (-1, -1):
                    clusters[root].append((y, x))

        for root, children in clusters.items():
            print(children)

        print("Number of islands = {}".format(self.num_islands))
        print("Max area = {}".format(self.area_max))

if __name__ == "__main__":
    union_find_inst = union_find_2d(height=3, width=3)
    union_find_inst.union((0, 0), (0, 0))
    union_find_inst.union((0, 0), (0, 1))
    union_find_inst.union((1, 1), (0, 1))
    union_find_inst.union((1, 1), (1, 2))
    union_find_inst.union((2, 2), (1, 2))
    union_find_inst.union((2, 1), (2, 2))
    union_find_inst.print_clusters()
