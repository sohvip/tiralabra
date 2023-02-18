from trie_node import TrieNode


class Trie:
    """Creates a trie and stores all sequences from the reference music.
    """

    def __init__(self):
        """The constructor.
        """
        self.root = TrieNode('')

    def insert(self, sequence):
        """Insert sequence of notes to trie.

        Args:
            sequence: List of tuples with the following structure:
            (note's number, note's name).
        """
        node = self.root
        for i in range(len(sequence)):
            if sequence[i][0] not in node.children:
                node.children[sequence[i][0]] = TrieNode(sequence[i][1])
            node = node.children[sequence[i][0]]
            node.frequency += 1
        node.is_terminal = True

    def next(self, sequence):
        """Searches the notes and their frequencies that could follow the given sequence.

        Args:
            sequence: A sequence of notes.

        Returns:
            Lists of possible notes and their frequencies or an empty list if there is
            no possibilities.
        """
        notes = []
        frequencies = []
        node = self.root
        for note in sequence:
            if note in node.children:
                node = node.children[note]
            else:
                return []

        for child in node.children:
            # if not child:
            #     return []
            notes.append(child)
            frequencies.append(node.children[child].frequency)

        return notes, frequencies

    def search(self, sequences):
        """Searches if the given sequences are in the trie.

        Args:
            sequences: A list of sequences.

        Returns:
            True if all the sequences can be found, False otherwise.
        """
        for sequence in sequences:
            node = self.root
            for note in sequence:
                if note in node.children:
                    node = node.children[note]
                else:
                    return False
        return True
