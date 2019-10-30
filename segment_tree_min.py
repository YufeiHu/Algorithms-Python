class segment_tree_min(object):
    def __init__(self, N):
        self.N = N
        self.low = [0] * (4 * N + 1)
        self.high = [0] * (4 * N + 1)
        self.mins = [0] * (4 * N + 1)
        self.delta = [0] * (4 * N + 1)
        self._initialize(1, 0, N - 1)

    def _initialize(self, idx, left, right):
        self.low[idx] = left
        self.high[idx] = right
        if left != right:
            mid = (left + right) // 2
            self._initialize(2 * idx, left, mid)
            self._initialize(2 * idx + 1, mid + 1, right)

    def increment(self, left, right, val):
        self._increment(1, left, right, val)

    def _increment(self, idx, left, right, val):
        if right < self.low[idx] or self.high[idx] < left:
            return
        elif left <= self.low[idx] and self.high[idx] <= right:
            self.delta[idx] += val
        else:
            self._lazy_propogate(idx)
            self._increment(2 * idx, left, right, val)
            self._increment(2 * idx + 1, left, right, val)
            self._update(idx)

    def _update(self, idx):
        self.mins[idx] = min(self.mins[2 * idx] + self.delta[2 * idx],
                             self.mins[2 * idx + 1] + self.delta[2 * idx + 1])

    def _lazy_propogate(self, idx):
        self.delta[2 * idx] += self.delta[idx]
        self.delta[2 * idx + 1] += self.delta[idx]
        self.delta[idx] = 0

    def minimum(self, left, right):
        return self._minimum(1, left, right)

    def _minimum(self, idx, left, right):
        if right < self.low[idx] or self.high[idx] < left:
            return float('inf')
        elif left <= self.low[idx] and self.high[idx] <= right:
            return self.mins[idx] + self.delta[idx]
        else:
            self._lazy_propogate(idx)
            min_left = self._minimum(2 * idx, left, right)
            min_right = self._minimum(2 * idx + 1, left, right)
            self._update(idx)
            return min(min_left, min_right)


if __name__ == "__main__":
    segment_tree_min_inst = segment_tree_min(10)
    segment_tree_min_inst.increment(0, 3, 2)
    segment_tree_min_inst.increment(0, 7, 1)
    segment_tree_min_inst.increment(4, 7, 10)
    segment_tree_min_inst.increment(2, 5, 7)
    print(segment_tree_min_inst.minimum(0, 7))
    print(segment_tree_min_inst.minimum(1, 4))
    print(segment_tree_min_inst.minimum(2, 5))
    print(segment_tree_min_inst.minimum(0, 0))
    print(segment_tree_min_inst.minimum(1, 1))
    print(segment_tree_min_inst.minimum(2, 2))
    print(segment_tree_min_inst.minimum(3, 3))
    print(segment_tree_min_inst.minimum(4, 4))
    print(segment_tree_min_inst.minimum(5, 5))
