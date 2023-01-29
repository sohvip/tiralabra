import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
    
    def test_insert_to_trie(self):
        self.trie.insert_to_trie(['a', 'b', 'c'])
        self.assertEqual(self.trie.root.children[1].note, 1)
    
    def test_char_to_int(self):
        list = self.trie.char_to_int(['a', 'b', 'c'])
        self.assertEqual(list, [1, 3, 4])
    
    def test_no_melody(self):
        self.trie.insert_to_trie(['a', 'b', 'c'])
        melody = self.trie.compose(['a#', 'b'])
        self.assertEqual(melody, 'Try another sequence')