import unittest
from trie_node import TrieNode


class TestTrieNode(unittest.TestCase):
    def setUp(self):
        self.trie_node = TrieNode('a')

    def test_note(self):
        self.assertEqual(self.trie_node.note, 'a')

    def test_children(self):
        self.trie_node.children[1] = TrieNode('A')
        self.assertEqual(self.trie_node.children[1].note, 'A')

    def test_frequency(self):
        self.trie_node.frequency += 1
        self.assertEqual(self.trie_node.frequency, 1)
