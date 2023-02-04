class TrieNode:
    """Stores information about a node in the trie.
    """

    def __init__(self, note):
        """The constructor.

        Args:
            note: A note from the reference music.
        """
        self.note = note
        self.frequency = 0
        self.children = {}
        self.is_terminal = False
