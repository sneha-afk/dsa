from typing import Any


# Taken from LC #208
class TrieNode:
    chars: list[Any]

    def __init__(self, num_chars: int = 26) -> None:
        # 26 letters, assumed to be all lowercase
        self.chars = [None] * num_chars

        # Is this the last character?
        self.is_end = False

    def __str__(self) -> str:
        return f"TrieNode[isEnd: {self.is_end}]"
