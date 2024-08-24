from typing import Any


class MaxHeap:
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

    def extract_max(self) -> Any:
        """
        Extracts the maximum element from the heap.
        """

        if self.size == 0:
            raise IndexError("MaxHeap: is empty")
        max_val = self.heap[0]
        self.size -= 1

        # Move the last element to the root, then percolate down to fix
        self.heap[0] = self.heap.pop()
        self._percolate_down(0)
        return max_val

    def get_max(self) -> Any:
        """
        Returns the maximum element, without removing it from the heap.
        """

        if self.size == 0:
            raise IndexError("MaxHeap: is empty")
        return self.heap[0]

    def get_size(self) -> int:
        return self.size

    def _percolate_up(self, index: int) -> None:
        """
        Continuously swaps upward until the heap property is met.
        That is, a parent node is larger than its children.
        """
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            self._percolate_up(parent)

    def _percolate_down(self, index: int) -> None:
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2
        largest = index

        if left_child < self.size and self.heap[left_child] > self.heap[index]:
            largest = left_child
        if right_child < self.size and self.heap[right_child] > self.heap[index]:
            largest = right_child

        # Parent is not the largest, swap downwards
        if largest != index:
            self._swap(index, largest)
            self._percolate_down(largest)

    def _swap(self, a: int, b: int) -> None:
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
