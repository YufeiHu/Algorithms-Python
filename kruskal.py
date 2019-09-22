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


"""
1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. 
   If cycle is not formed, include this edge. Else, discard it.
3. Repeat step#2 until there are (V-1) edges in the spanning tree.
Only undirected graph is supported!
"""
def kruskal(edges):
    # get the number of vertices
    vertices = set()
    for v1, v2, weight in edges:
        vertices.add(v1)
        vertices.add(v2)
    num_vertices = len(vertices)

    # step 1: sort all edges in non-decreasing order of their weight
    edges = sorted(edges, key=lambda x : x[2])
    ans = list()
    union_find_inst = union_find(num_vertices)

    # step 2: pick the smallest-weight edge each time
    for edge in edges:
        if len(ans) >= num_vertices - 1:
            break

        v1, v2, weight = edge
        parent_v1 = union_find_inst.find(v1)
        parent_v2 = union_find_inst.find(v2)

        # when no cycle is found, pick the current edge
        if parent_v1 != parent_v2:
            ans.append([v1, v2, weight])
            union_find_inst.union(parent_v1, parent_v2)

    return ans


if __name__ == "__main__":
    edges = [(0, 1, 10),
             (0, 2, 6),
             (0, 3, 5),
             (1, 3, 15),
             (2, 3, 4)]

    ans = kruskal(edges)

    for v1, v2, weight in ans:
        print("{} -> {} with cost of {}".format(v1, v2, weight))
