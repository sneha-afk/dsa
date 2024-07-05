# linked-list

A [linked list]("https://en.wikipedia.org/wiki/Linked_list") is a linear data structure that does not allow for random memory access but has simple operations for insertion and removal. A singly-linked list only has pointers in one direction, while a doubly-linked list has pointers in two directions.

A circular linked list has the head and tail pointers connected, so no reference is `None`.

## Complexity

| Category        | Complexity |
|-----------------|------------|
| Search time     | $O(n)$     |
| Space           | $O(n)$     |
| Insert (at end) | $O(1)$     |
| Insert (middle) | $O(n)$     |
| Removal         | $O(n)$^    |

^Can be $O(1)$ if the structure stores pointers to the head and tail to perform a check when the item to remove is one of them

## Uses
Tracing a path or sequence, keeping a history log.
