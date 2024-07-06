# A doubly-linked list can traverse both directions

from typing import Any, Optional
from util import ListNode


class DoublyLL:
    head: Optional[ListNode]
    tail: Optional[ListNode]

    def __init__(self) -> None:
        self.head = self.tail = None

    def __str__(self) -> str:
        return f"DoublyLL[head: {self.head}, tail: {self.tail}]"

    def append(self, item: Any) -> None:
        """
        Append an item at the end of this linked list
        """
        n: ListNode = ListNode(item)

        if self.tail is None:
            self.head = n
        else:
            self.tail.next = n

        # Difference from singly: fix back pointer
        n.prev = self.tail
        self.tail = n

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

    def contains(self, item: Any) -> bool:
        """
        Returns whether the item exists in the linked list
        """
        return self.find(item) is not None

    def remove(self, item: Any) -> None:
        """
        Removes an item if it exists in the linked list.
        No effect if the item is not present.
        """

        cur: Optional[ListNode] = self.head
        prev: Optional[ListNode] = cur
        while cur:
            if cur.item == item:
                if cur == self.head:
                    self.head = cur.next
                elif prev:
                    prev.next = cur.next

                # Difference from singly: fix back pointer
                if cur.next:
                    cur.next.prev = prev
                break
            prev = cur
            cur = cur.next
