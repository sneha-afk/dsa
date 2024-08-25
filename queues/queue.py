# A generic Queue that can hold heterogenous elements

from collections.abc import Sequence
from typing import Any


class Queue:
    items: list[Any]

    def __init__(self) -> None:
        self.items = list()

    def enqueue(self, item: Any) -> None:
        """
        Enqueue an element to the end of the queue.
        """
        self.items.append(item)

    def enqueue_multiple(self, items: Sequence[Any]) -> None:
        """
        Enqueue multiple elements to the queue.
        """
        for i in items:
            self.enqueue(i)

    def dequeue(self) -> Any:
        """
        Dequeue an element from the beginning of the queue.
        Returns None if the queue is empty.
        """
        if len(self.items) < 1:
            return None
        return self.items.pop(0)

    def size(self) -> int:
        """
        Get the size (current number of items) on the queue.
        """
        return len(self.items)

    def peek(self) -> Any:
        """
        Returns element at the beginning of the queue, or None if the queue is empty.
        """
        if len(self.items) < 1:
            return None
        return self.items[0]
