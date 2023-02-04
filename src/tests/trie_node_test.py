import unittest
from trie_node import TrieNode


class TestTrieNode(unittest.TestCase):
    def setUp(self):
        self.trie_node = TrieNode(1)

    def test_note(self):
        self.assertEqual(self.trie_node.note, 1)

    def test_children(self):
        self.trie_node.children[2] = TrieNode(2)
        self.assertEqual(self.trie_node.children[2].note, 2)

    def test_counter(self):
        self.trie_node.counter += 1
        self.assertEqual(self.trie_node.counter, 1)
