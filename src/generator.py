from random import choices
from converter import Converter


class Generator:
    """Generates a new melody based on the reference music.
    """

    def __init__(self, trie):
        """The constructor.

        Args:
            trie: Trie object that contains trie data structure.
        """
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
        follower = choices(notes, weights=frequencies, k=1)
        return follower

    def generate(self, length, order):
        """Generates a new melody based on the values stored in trie.

        Args:
            length: Wanted length of the generated melody.
            order: Order of the Markov Chain.

        Returns:
            New melody in a form of list.
        """
        previous = []
        melody = []
        for _ in range(order):
            lists = self.trie.next(previous)
            if [] in lists:
                return 'error'
            follower = self.calculate(lists[0], lists[1])
            previous.append(follower[0])
            melody.append(self.convert[follower[0]])
        for _ in range(length-order):
            lists = self.trie.next(previous)
            if [] in lists:
                return 'error'
            if len(lists) <= 1:   # pragma: no cover
                return 'error'
            follower = self.calculate(lists[0], lists[1])
            previous.pop(0)
            previous.append(follower[0])
            melody.append(self.convert[follower[0]])
        return melody
