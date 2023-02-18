import unittest
from generator import Generator
from run import Run
from music_path import REFERENCE_FILE_PATH


class TestRun(unittest.TestCase):
    def setUp(self):
        self.run = Run()
    
    def test_generating(self):
        sequences = self.run.converter.read_file(REFERENCE_FILE_PATH)
        note_seq = self.run.converter.sequence_maker(sequences, 2)
        self.run.store(note_seq)
        generator = Generator(self.run.trie)
        output = generator.generate(20, 2)
        output = self.run.converter.char_to_int_2(output)
        check = self.run.converter.sequence_maker(output, 2)
        self.assertEqual(self.run.trie.search(check), True)
