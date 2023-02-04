from random import choices
from converter import Converter

class Generator:
    def __init__(self, trie):
        self.trie = trie
        self.converter = Converter()
        self.convert = self.converter.convert_list_2

    def calculate(self, notes, frequencies):
        """Draws a note from the given options.
        
        Args:
            notes: A list of notes.
            frequencies: A list of frequencies of the notes.

        Returns:
            A note that got picked.
        """
        next = choices(notes, weights=frequencies, k=1)
        return next
    
    def generate(self, length):
        """Generates a new melody based on the values stored in trie.

        Args:
            length: Wanted length of the generated melody.
        Returns:
            New melody in a form of list.
        """
        previous = []
        melody = []
        for i in range(2):
            lists = self.trie.next(previous)
            if lists == []:
                return 'Error'
            n = self.calculate(lists[0], lists[1])
            previous.append(n[0])
            melody.append(self.convert[n[0]])
        for i in range(length):
            lists = self.trie.next(previous)
            if lists == []:
                return 'Error'
            n = self.calculate(lists[0], lists[1])
            previous.pop(0)
            previous.append(n[0])
            melody.append(self.convert[n[0]])
        return melody