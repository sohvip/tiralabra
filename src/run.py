from converter import Converter
from trie import Trie
from generator import Generator
from lilypond import Lilypond
from music_path import BOTW_FILE_PATH, AUTUMN_FILE_PATH



class Run:
    """Takes care of running the generator.
    """

    def __init__(self):
        """The constructor.
        """
        self.converter = Converter()
        self.trie = Trie()
        self.lilypond = Lilypond()

    def start(self, start=True, song=0):    # pragma: no cover
        """Allows user to start the generating process.

        Args:
            start: True if it is the first time that the function is called,
            otherwise False.
            song: Number of the song the user wants to use as a reference.

        Returns:
            song: Number of the song the user has chosen.
        """
        if start:
            print()
            print('welcome to MUSIC GENERATOR')
            print()
            print('[1] breath of the wild main theme')
            print('[2] autumn mountain')
            print()
            song = 0
            while song not in [1, 2]:
                try:
                    song = int(input('choose a song for reference: '))
                except ValueError:
                    pass
        print()
        order = 0
        while order < 1:
            try:
                order = int(input('markov chain order: '))
            except ValueError:
                pass
        print()
        length = 0
        while length < order:
            try:
                length = int(input('length of the melody: '))
            except ValueError:
                pass
        print()
        input('press enter to GENERATE ')
        print()
        if song == 1:
            notes = self.converter.read_file(BOTW_FILE_PATH)
        else:
            notes = self.converter.read_file(AUTUMN_FILE_PATH)
        note_seq = self.converter.sequence_maker(notes, order)
        self.store(note_seq)
        generator = Generator(self.trie)
        output = generator.generate(length, order)
        if output != 'error':
            print('melody saved as lilypond.ly')
            print()
            self.lilypond.write(output)
        else:
            print('Generating melody failed. Try again or change the parameters.')
            print()
        return song

    def again(self, song):    # pragma: no cover
        """Allows user to start the generating process again.

        Args:
            song: Number of the song the user has chosen.
        """
        answer = input('generate again? y/n ')
        print()
        if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
            self.start(False, song)
            return True
        return False

    def store(self, melody):
        """Calls the function that inserts notes to trie.

        Args:
            melody: Three note sequences.
        """
        for i in melody:
            self.trie.insert(i)
