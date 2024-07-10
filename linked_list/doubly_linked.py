# A doubly-linked list can traverse both directions

from typing import Any, Optional
from . import LLBase
from util import ListNode


class DoublyLL(LLBase):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return f"DoublyLL[head: {self.head}, tail: {self.tail}]"

    def append(self, item: Any) -> None:
        n: ListNode = ListNode(item)

        if self.tail is None:
            self.head = n
        else:
            self.tail.next = n

        # Difference from singly: fix back pointer
        n.prev = self.tail
        self.tail = n

    def insert(self, item: Any, index: int = -1) -> None:
        cur: Optional[ListNode] = self.head
        cur_i: int = 0
        prev: Optional[ListNode] = cur
        while cur and cur_i < index:
            prev = cur
            cur = cur.next
            cur_i += 1

        n: ListNode = ListNode(item, prev, cur)

        if cur_i == 0:
            if self.head is None:
                self.tail = n
            self.head = n

        if cur is None:
            if self.tail is None:
                self.head = n
            self.tail = n

        if prev is not None:
            prev.next = n

    def remove(self, item: Any) -> None:
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
