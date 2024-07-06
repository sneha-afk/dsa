# Generic list node structure

# Optional typing hint: union of a type and None
from typing import Any, Optional


class ListNode:
    item: Any
    prev: Optional["ListNode"]
    next: Optional["ListNode"]

    def __init__(
        self,
        item: Any,
        prev: Optional["ListNode"] = None,
        next: Optional["ListNode"] = None,
    ) -> None:
        self.item = item
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return f"ListNode[value:{self.item},\
            hasPrev: {True if self.prev else False},\
            hasNext: {True if self.next else False}]"
