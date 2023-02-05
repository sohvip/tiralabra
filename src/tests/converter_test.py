import unittest
from converter import Converter


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter = Converter()
    
    def test_converter(self):
        sequences = self.converter.read_file('src/music/test_piece.txt')
        self.assertEqual(sequences, [[(1,'A'), (2,'A#'), (1,'A')]])