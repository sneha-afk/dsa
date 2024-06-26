# A generic Stack that can hold heterogenous elements

from collections.abc import Sequence
from typing import Any


class Stack:
    items: list[Any]

    def __init__(self) -> None:
        self.items = list()

    def push(self, item: Any) -> None:
        """
        Push an element onto the stack.
        """
        self.items.append(item)

    def push_multiple(self, items: Sequence[Any]):
        """
        Push multiple elements onto the stack.
        """

        for i in items:
            self.items.append(i)

    def pop(self) -> Any:
        """
        Pop and return an element from the stack.
        If the stack is empty, returns None.
        """

        if len(self.items) <= 0:
            return None

        return self.items.pop()

    def size(self) -> int:
        """
        Get the size (current number of items) on the stack.
        """

        return len(self.items)
