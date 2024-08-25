# heaps

A [heap]("https://en.wikipedia.org/wiki/Heap_(data_structure)") is a "tree-based data structure" that satisfies a heap property (either max or min): a parent node is either the largest or smallest amongst all its children, recursively.

A binary heap is a complete binary tree: all levels are filled except possibly the last, which is filled left to right.

## Complexity

| Category        | Complexity   |
|-----------------|--------------|
| Search time     | $O(n)$       |
| Space           | $O(n)$       |
| Insert          | $O(\log n)$  |
| Removal         | $O(\log n)$, getting the maximum or minimum element |

## Uses
- Underlying structure for priority queues
