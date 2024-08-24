from typing import Any


class MinHeap:
    heap: list
    size: int

    def __init__(self) -> None:
        self.heap = []
        self.size = 0

    def insert(self, val: Any) -> None:
        """
        Insert an element into the heap and maintain the heap property.
        """
        self.heap.append(val)
        self.size += 1
        self._percolate_up(self.size - 1)

    def extract_min(self) -> Any:
        """
        Extracts the minimum element from the heap.
        """

        if self.size == 0:
            raise IndexError("MinHeap: is empty")
        min_val = self.heap[0]
        self.size -= 1

        # Move the last element to the root, then percolate down to fix
        self.heap[0] = self.heap.pop()
        self._percolate_down(0)
        return min_val

    def get_min(self) -> Any:
        """
        Returns the minimum element, without removing it from the heap.
        """

        if self.size == 0:
            raise IndexError("MinHeap: is empty")
        return self.heap[0]

    def get_size(self) -> int:
        return self.size

    def _percolate_up(self, index: int) -> None:
        """
        Continuously swaps upward until the heap property is met.
        That is, a parent node is larger than its children.
        """
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            self._percolate_up(parent)

    def _percolate_down(self, index: int) -> None:
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2
        smallest = index

        if left_child < self.size and self.heap[left_child] < self.heap[index]:
            smallest = left_child
        if right_child < self.size and self.heap[right_child] < self.heap[index]:
            smallest = right_child

        # Parent is not the largest, swap downwards
        if smallest != index:
            self._swap(index, smallest)
            self._percolate_down(smallest)

    def _swap(self, a: int, b: int) -> None:
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
