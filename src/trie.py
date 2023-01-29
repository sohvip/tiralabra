from trie_node import TrieNode
from random import choice
import copy

class Trie:
    """Creates a trie and stores all sequences from the reference music.
    """

    def __init__(self):
        """The constructor.
        """
        self.root = TrieNode('')
        self.convert_list = {'a': 1, 'a#': 2, 'b': 3, 'c': 4, 'c#': 5,
        'd': 6, 'd#': 7, 'e': 8, 'f': 9, 'f#': 10, 'g': 11, 'g#': 12}

    def insert_to_trie(self, notes):
        """Insert given music to trie as three note sequences.
        
        Args:
            notes: List of notes.
        """
        notes_as_numbers = self.char_to_int(notes)
        for i in range(len(notes_as_numbers)-2):
            node = self.root
            if notes_as_numbers[i] in node.children:
                node = node.children[notes_as_numbers[i]]
            else:
                new_node = TrieNode(notes_as_numbers[i])
                node.children[notes_as_numbers[i]] = new_node
                node = new_node
            if notes_as_numbers[i+1] in node.children:
                node = node.children[notes_as_numbers[i+1]]
            else:
                new_node = TrieNode(notes_as_numbers[i+1])
                node.children[notes_as_numbers[i+1]] = new_node
                node = new_node
            if notes_as_numbers[i+2] in node.children:
                node = node.children[notes_as_numbers[i+2]]
            else:
                new_node = TrieNode(notes_as_numbers[i+2])
                node.children[notes_as_numbers[i+2]] = new_node
                node = new_node
            node.counter += 1
    
    def next_note_possibilities(self, sequence):
        """Searches the notes (and their frequencies) that could follow the given sequence.

        Args:
            sequence: A sequence of notes.

        Returns:
            A list of possible notes and their frequencies or an empty list if there is no possibilities.
        """
        #notes = self.char_to_int(sequence)
        options = []
        node = self.root

        for note in sequence:
            if note in node.children:
                node = node.children[note]
            else:
                return []
        
        for child in node.children:
            for i in range(node.children[child].counter):
                options.append(node.children[child].note)
        
        return options
    
    def char_to_int(self, notes):
        """Converts notes to numbers:
            a -> 1
            a# -> 2
            b -> 3
            ...
            g# -> 12

        Args:
            notes: List of notes.

        Returns:
            A list of numbers that reference certain notes.
        """
        for i in range(len(notes)):
            notes[i] = self.convert_list[notes[i]]
        
        return notes    
    
    def compose(self, sequence):
        """Composes a melody based on the given starting sequence.
        
        Args:
            sequence: A sequence of notes.

        Returns:
            A list of notes or an error message.
        """
        notes = self.char_to_int(sequence)
        melody = copy.deepcopy(notes)
        for i in range(100):
            options = self.next_note_possibilities(notes)
            if options == []:
                return 'Try another sequence'
            next = choice(options)
            notes.pop(0)
            notes.append(next)
            melody.append(next)
        return melody

    
    

if __name__ == "__main__":
    trie = Trie()
    trie.insert_to_trie(['b', 'b', 'b', 'b', 'd', 'd', 'a', 'a', 'a', 'a', 'g', 'a', 'b', 'b', 'b', 'b', 'd', 'd', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'd', 'd', 'a', 'a', 'a', 'a', 'g', 'g', 'd', 'd', 'd', 'd', 'c', 'b', 'a', 'a', 'a', 'a', 'g', 'a', 'b', 'b', 'b', 'b', 'd', 'd', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'd', 'd', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'd', 'd', 'a', 'a', 'a', 'a', 'g', 'g', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'b', 'c', 'd', 'd', 'd', 'd', 'c', 'b', 'c', 'b', 'g', 'g', 'g', 'g', 'c', 'c', 'c', 'c', 'b', 'a', 'b', 'a', 'e', 'e', 'e', 'e', 'd', 'd', 'd', 'd', 'c', 'b', 'c', 'b', 'g', 'g', 'c', 'c', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'])
    trie.insert_to_trie(['e', 'e', 'e', 'e', 'e', 'e', 'a', 'a', 'e', 'e', 'a', 'a', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'g', 'g', 'f', 'f', 'f', 'f', 'f', 'f', 'e', 'e', 'd', 'd', 'd', 'd', 'd', 'd', 'c', 'c', 'e', 'e', 'e', 'e', 'd', 'd', 'e', 'e', 'f', 'f', 'e', 'e', 'd', 'd', 'f', 'f', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'])
    print(trie.compose(['d#', 'g']))
    print(trie.compose(['c', 'g']))

