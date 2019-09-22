import heapq


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class customizable_heap(object):
    def __init__(self, data=None, comparator=lambda x: x):
        self.comparator = comparator
        self.cnt = 0
        if data:
            self._data = list()
            for val in data:
                self._data.append((self.comparator(val), self.cnt, val))
                self.cnt += 1
            heapq.heapify(self._data)
        else:
            self._data = list()

    def push(self, item):
        heapq.heappush(self._data, (self.comparator(item), self.cnt, item))
        self.cnt += 1

    def pop(self):
        if self._data:
            self.cnt -= 1
            return heapq.heappop(self._data)[2]
        else:
            return None

    def top(self):
        if self._data:
            return self._data[0][2]
        else:
            return None


def comparator(point):
    return point.x ** 2 + point.y ** 2


if __name__ == "__main__":
    customizable_heap_inst = customizable_heap(comparator=comparator)

    p1 = point(1, 2)
    p2 = point(2, 1)
    p3 = point(2, 3)
    p4 = point(3, 4)
    myHeapInst.push(p4)
    myHeapInst.push(p2)
    myHeapInst.push(p1)
    myHeapInst.push(p3)
    myHeapInst.pop()

    print(myHeapInst.top().x, myHeapInst.top().y)
    
