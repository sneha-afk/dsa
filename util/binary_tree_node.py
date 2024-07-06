# Generic binary tree node structure

from typing import Any, Optional


class BTNode:
    item: Any
    parent: Optional["BTNode"]
    left: Optional["BTNode"]
    right: Optional["BTNode"]

    def __init__(
        self,
        item: Any,
        parent: Optional["BTNode"] = None,
        left: Optional["BTNode"] = None,
        right: Optional["BTNode"] = None,
    ) -> None:
        self.item = item
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"BTNode[value:{self.item},\
            hasParent: {True if self.parent else False},\
            hasLeft: {True if self.left else False},\
            hasRight: {True if self.right else False}]"
