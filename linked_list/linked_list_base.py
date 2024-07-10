import abc
from typing import Any, Optional, Sequence

from util.list_node import ListNode


class LLBase(abc.ABC):
    head: Optional[ListNode]
    tail: Optional[ListNode]
    cur_iter_node: Optional[ListNode]

    def __init__(self) -> None:
        self.head = self.tail = None

    def __iter__(self):
        self.cur_iter_node = self.head
        return self

    def __next__(self):
        if not self.cur_iter_node:
            raise StopIteration

        item: Any = self.cur_iter_node.item
        self.cur_iter_node = self.cur_iter_node.next
        return item

    @abc.abstractmethod
    def append(self, item: Any) -> None:
        """
        Append a new item to the end of this linked list.
        """
        ...

    @abc.abstractmethod
    def insert(self, item: Any, index: int = -1) -> None:
        """
        Insert at a specified index. If there are less than (index + 1) elements,
        appends to the end of the list. Negative indices default to appending at the
        beginning of the list.
        """
        ...

    @abc.abstractmethod
    def remove(self, item: Any) -> None:
        """
        Removes an item if it exists in the linked list.
        No effect if the item is not present.
        """
        ...

    def find(self, item: Any) -> Optional[ListNode]:
        """
        Returns the node containing the item or None if not present
        """
        cur: Optional[ListNode] = self.head
        while cur:
            if cur.item == item:
                return cur
            cur = cur.next
        return None

    def append_multiple(self, items: Sequence[Any]) -> None:
        """
        Appends multiple items to the end of this linked list
        """
        for i in items:
            self.append(i)

    def contains(self, item: Any) -> bool:
        """
        Returns whether the item exists in the linked list
        """
        return self.find(item) is not None
