# A singly-linked list traverses in one direction

from typing import Any, Optional
from util import ListNode


class SinglyLL:
    head: Optional[ListNode]
    tail: Optional[ListNode]

    def __init__(self) -> None:
        self.head = self.tail = None

    def __str__(self) -> str:
        return f"SinglyLL[head: {self.head}, tail: {self.tail}]"

    def append(self, item: Any) -> None:
        """
        Append an item at the end of this linked list
        """
        n: ListNode = ListNode(item)

        if self.tail is None:
            self.head = n
        else:
            self.tail.next = n
        self.tail = n

    def insert(self, item: Any, index: int = -1) -> None:
        """
        Insert at a specified index. If there are less than (index + 1) elements,
        appends to the end of the list. Negative indices default to appending at the
        beginning of the list.
        """

        cur: Optional[ListNode] = self.head
        cur_i: int = 0
        prev: Optional[ListNode] = cur
        while cur and cur_i < index:
            prev = cur
            cur = cur.next
            cur_i += 1

        n: ListNode = ListNode(item, prev)

        if cur_i == 0:
            if self.head is None:
                self.tail = n
            self.head = n
        if cur is None:
            if self.tail is None:
                self.head = n
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
                break
            prev = cur
            cur = cur.next
