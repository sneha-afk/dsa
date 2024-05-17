from typing import Any


# Taken from LC #208
class TrieNode:
    chars: list[Any]

    def __init__(self) -> None:
        # 26 letters, assumed to be all lowercase
        self.chars = [None] * 26

        # Is this the last character?
        self.is_end = False


class Trie:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode()

    # "void insert(String word) Inserts the string word into the trie"
    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            ch_num = ord(ch) - ord("a")

            # Add the letter if it doesn't exist yet
            if not curr.chars[ch_num]:
                curr.chars[ch_num] = TrieNode()

            # Move to current character's node
            curr = curr.chars[ch_num]

        # Finished a word
        curr.is_end = True

    # "boolean search(String word) Returns true if the string word
    # is in the trie (i.e., was inserted before), and false otherwise"
    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            ch_num = ord(ch) - ord("a")

            # Does the character exist?
            if not curr.chars[ch_num]:
                return False

            curr = curr.chars[ch_num]

        # Does the word end?
        return curr.is_end

    # "boolean startsWith(String prefix) Returns true if there is a previously
    # inserted string word that has the prefix prefix, and false otherwise"
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            ch_num = ord(ch) - ord("a")

            # Does the character exist?
            if not curr.chars[ch_num]:
                return False

            curr = curr.chars[ch_num]

        # All characters accounted for?
        return True
