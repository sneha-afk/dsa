# Generic node structure

# Optional typing hint: union of a type and None
from typing import Any, Optional


class Node:
    item: Any
    prev: Optional["Node"]
    next: Optional["Node"]

    def __init__(
        self,
        item: Any,
        prev: Optional["Node"] = None,
        next: Optional["Node"] = None,
    ) -> None:
        self.item = item
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return f"Node[value:{self.item},\
            hasPrev: {True if self.prev else False},\
            hasNext: {True if self.next else False}]"
