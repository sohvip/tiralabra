import unittest
from trie import Trie
from generator import Generator


class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.generator = Generator(self.trie)

    def test_generating_error(self):
        error = self.generator.generate(100, 2)
        self.assertEqual(error, 'error')

    def test_generating_error_2(self):
        self.trie.insert([(1, 'A'), (2, 'A#')])
        error = self.generator.generate(100, 2)
        self.assertEqual(error, 'error')
