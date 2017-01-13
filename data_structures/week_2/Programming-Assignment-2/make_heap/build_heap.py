# python3


class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def read_data(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def write_response(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def l_child_index(self, index):
        l_child_index = 2 * index + 1
        if l_child_index >= len(self._data):
            return -1
        return l_child_index

    def r_child_index(self, index):
        r_child_index = 2 * index + 2
        if r_child_index >= len(self._data):
            return -1
        return r_child_index

    def shift_down(self, i):
        min_index = i
        left = self.l_child_index(i)
        right = self.r_child_index(i)

        if left != -1 and self._data[left] < self._data[min_index]:
            min_index = left

        if right != -1 and self._data[right] < self._data[min_index]:
            min_index = right

        if i != min_index:
            self._swaps.append((i, min_index))
            self._data[i], self._data[min_index] = self._data[min_index], self._data[i]
            self.shift_down(min_index)

    def generate_swaps(self):
        for i in range(len(self._data) // 2, -1, -1):
            self.shift_down(i)

    def solve(self):
        self.read_data()
        self.generate_swaps()
        self.write_response()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.solve()
