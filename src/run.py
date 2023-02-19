from converter import Converter
from trie import Trie
from generator import Generator
from lilypond import Lilypond


class Run:
    """Takes care of running the generator.
    """

    def __init__(self):
        """The constructor.
        """
        self.converter = Converter()
        self.trie = Trie()
        self.lilypond = Lilypond()

    def start(self):    # pragma: no cover
        """Allows user to start the generating process.
        """
        print('Welcome to Music Generator')
        order = int(input('Markov Chain Order: '))
        length = int(input('Length of the melody: '))
        input('Press enter to start generating :) ')
        notes = self.converter.read_file()
        note_seq = self.converter.sequence_maker(notes, order)
        self.store(note_seq)
        generator = Generator(self.trie)
        output = generator.generate(length, order)
        print(output)
        if output != 'Error':
            self.lilypond.write(output)

    def again(self):    # pragma: no cover
        """Allows user to start the generating process again.
        """
        answer = input('Press enter to generate another one or q for exit ')
        if answer == 'q':
            return False
        self.start()
        return True

    def store(self, melody):
        """Calls the function that inserts notes to trie.

        Args:
            melody: Three note sequences.
        """
        for i in melody:
            self.trie.insert(i)
