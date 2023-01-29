class TrieNode:
    """Stores information about a node in the trie.
    """

    def __init__(self, note):
        """The constructor.

        Args:
            note: A note from the reference music.
        """
        self.note = note
        self.counter = 0
        self.children = {}
