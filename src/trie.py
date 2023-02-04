from trie_node import TrieNode
from random import choices
import copy

class Trie:
    """Creates a trie and stores all sequences from the reference music.
    """

    def __init__(self):
        """The constructor.
        """
        self.root = TrieNode('')
        self.convert_list = {'A': 1, 'A#': 2, 'B': 3, 'C': 4, 'C#': 5,
        'D': 6, 'D#': 7, 'E': 8, 'F': 9, 'F#': 10, 'G': 11, 'G#': 12,
        'a': 13, 'a#': 14, 'b': 15, 'c': 16, 'c#': 17, 'd': 18,
        'd#': 19, 'e': 20, 'f': 21, 'f#': 22, 'g': 23, 'g#': 24}
        self.convert_list_2 = dict([(value, key) for key, value in self.convert_list.items()])
    
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
            Lists of possible notes and their frequencies or an empty list if there is no possibilities.
        """
        notes = []
        frequencies = []
        node = self.root
        for note in sequence:
            if note == '':
                pass
            elif note in node.children:
                node = node.children[note]
            else:
                return []
        
        for child in node.children:
            notes.append(child)
            frequencies.append(node.children[child].frequency)
        
        return notes, frequencies
