from converter import Converter
from trie import Trie
from generator import Generator

class Run:
    def __init__(self):
        self.converter = Converter()
        self.trie = Trie()

    def start(self):
        """Allows user to start the generating process.
        """
        print('Welcome to Music Generator')
        input('Press enter to start generating :) ')
        note_seq = self.converter.read_file()
        self.store(note_seq)
        generator = Generator(self.trie)
        output = generator.generate(100)
        print(output)
    
    def again(self):
        answer = input('Press enter to generate another one or q for exiting ')
        if answer == 'q':
            return False
        else:
            self.start()
            return True
    
    def store(self, melody):
        """Calls the function that inserts notes to trie.

        Args:
            melody: Three note sequences.
        """
        for i in melody:
            self.trie.insert(i)
