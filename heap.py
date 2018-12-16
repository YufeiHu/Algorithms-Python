class heap(object):

    def __init__(self):
        self.heap = list()

    def heapify_up(self, idx):
        while idx > 0:
            parent = idx // 2
            if self.heap[parent] <= self.heap[idx]:
                return
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            idx = parent

    def heapify_down(self, idx):
        if len(self.heap) == 1: return
        while 2 * idx < len(self.heap):
            child = 2 * idx
            if child + 1 < len(self.heap) and (self.heap[child + 1] <= self.heap[child]):
                child += 1
            if self.heap[idx] <= self.heap[child]:
                return
            self.heap[idx], self.heap[child] = self.heap[child], self.heap[idx]
            idx = child

    def del_min(self):
        element_back = self.heap.pop()
        if not self.heap:
            return element_back
        element_front = self.heap[0]
        self.heap[0] = element_back
        self.heapify_down(0)
        return element_front

    def find_min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def add(self, element):
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)


if __name__ == "__main__":
    heap_inst = heap()

    heap_inst.add(1)
    heap_inst.add(9)
    heap_inst.add(6)
    heap_inst.add(2)
    heap_inst.add(3)
    heap_inst.del_min()

    print(heap_inst.find_min())
