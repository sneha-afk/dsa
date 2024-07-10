# A singly-linked list traverses in one direction

from . import LLBase
from typing import Any, Optional
from util import ListNode


class SinglyLL(LLBase):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return f"SinglyLL[head: {self.head}, tail: {self.tail}]"

    def append(self, item: Any) -> None:
        n: ListNode = ListNode(item)

        if self.tail is None:
            self.head = n
        else:
            self.tail.next = n
        self.tail = n

    def insert(self, item: Any, index: int = 0) -> None:
        n: ListNode = ListNode(item)

        cur: Optional[ListNode] = self.head
        cur_i: int = 0
        prev: Optional[ListNode] = None
        while cur and cur_i < index:
            prev = cur
            cur = cur.next
            cur_i += 1

        n.next = cur
        if prev:
            prev.next = n
        else:
            if self.head is None:
                self.tail = n
            self.head = n

        if cur is None:
            if self.tail is None:
                self.head = n
            self.tail = n

    def remove(self, item: Any) -> None:
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
