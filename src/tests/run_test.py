import unittest
from generator import Generator
from run import Run
from music_path import BOTW_FILE_PATH


class TestRun(unittest.TestCase):
    def setUp(self):
        self.run = Run()

    def test_generating_1st_order(self):
        sequences = self.run.converter.read_file(BOTW_FILE_PATH)
        note_seq = self.run.converter.sequence_maker(sequences, 1)
        self.run.store(note_seq)
        generator = Generator(self.run.trie)
        output = 'error'
        while output == 'error':
            output = generator.generate(200, 1)
        output = self.run.converter.char_to_int_2(output)
        check = self.run.converter.sequence_maker(output, 1)
        self.assertEqual(self.run.trie.search(check), True)
    
    def test_generating_2nd_order(self):
        sequences = self.run.converter.read_file(BOTW_FILE_PATH)
        note_seq = self.run.converter.sequence_maker(sequences, 2)
        self.run.store(note_seq)
        generator = Generator(self.run.trie)
        output = 'error'
        while output == 'error':
            output = generator.generate(200, 2)
        output = self.run.converter.char_to_int_2(output)
        check = self.run.converter.sequence_maker(output, 2)
        self.assertEqual(self.run.trie.search(check), True)
    
    def test_generating_3rd_order(self):
        sequences = self.run.converter.read_file(BOTW_FILE_PATH)
        note_seq = self.run.converter.sequence_maker(sequences, 3)
        self.run.store(note_seq)
        generator = Generator(self.run.trie)
        output = 'error'
        while output == 'error':
            output = generator.generate(200, 3)
        output = self.run.converter.char_to_int_2(output)
        check = self.run.converter.sequence_maker(output, 3)
        self.assertEqual(self.run.trie.search(check), True)
