import unittest
from converter import Converter
from music_path import TEST_FILE_PATH


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter = Converter()
    
    def test_converter(self):
        sequences = self.converter.read_file(TEST_FILE_PATH)
        self.assertEqual(sequences, [(1,'A'), (3,'B'), (4,'C'), (6,'D'), (1,'A')])
    
    def test_sequence_maker(self):
        sequences = self.converter.read_file(TEST_FILE_PATH)
        sequences_2 = self.converter.sequence_maker(sequences, 2)
        sequences_3 = self.converter.sequence_maker(sequences, 3)
        self.assertEqual(sequences_2, [[(1,'A'), (3,'B'), (4,'C')],[(3,'B'), (4,'C'), (6,'D')],[(4,'C'), (6,'D'), (1,'A')]])
        self.assertEqual(sequences_3, [[(1,'A'), (3,'B'), (4,'C'), (6,'D')],[(3,'B'), (4,'C'), (6,'D'), (1,'A')]])
