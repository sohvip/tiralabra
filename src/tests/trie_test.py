import unittest
from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert(self):
        self.trie.insert([(13, 'a'), (15, 'b'), (16, 'c')])
        self.assertEqual(self.trie.root.children[13].note, 'a')
        self.assertEqual(self.trie.root.children[13].is_terminal, False)
        node = self.trie.root.children[13]
        self.assertEqual(node.children[15].note, 'b')
        self.assertEqual(node.children[15].is_terminal, False)
        node = node.children[15]
        self.assertEqual(node.children[16].note, 'c')
        self.assertEqual(node.children[16].is_terminal, True)

    def test_next_with_empty_sequence(self):
        self.trie.insert([(13, 'a')])
        self.trie.insert([(13, 'a')])
        possibilities = self.trie.next([])
        self.assertEqual(possibilities, ([13], [2]))

    def test_next_with_sequence(self):
        self.trie.insert([(13, 'a'), (15, 'b'), (16, 'c')])
        self.trie.insert([(13, 'a'), (12, 'G#'), (11, 'G')])
        possibilities = self.trie.next([13, 12])
        self.assertEqual(possibilities, ([11], [1]))

    def test_next_with_impossible_sequence(self):
        self.trie.insert([(13, 'a'), (15, 'b'), (16, 'c')])
        self.trie.insert([(13, 'a'), (12, 'G#'), (11, 'G')])
        possibilities = self.trie.next([13, 11])
        self.assertEqual(possibilities, [])

    def test_root(self):
        self.assertEqual(self.trie.root.note, '')

    def test_search(self):
        self.trie.insert([(13, 'a'), (15, 'b'), (16, 'c')])
        self.assertEqual(self.trie.search([[13, 15, 17]]), False)

    def test_search_2(self):
        self.trie.insert([(13, 'a'), (15, 'b'), (16, 'c')])
        self.trie.insert([(13, 'a'), (15, 'b'), (16, 'c'),
                         (13, 'a'), (15, 'b'), (16, 'c')])
        self.trie.insert([(13, 'a'), (12, 'G#'), (11, 'G')])
        self.trie.insert([(13, 'a'), (14, 'a#'), (16, 'c')])
        self.assertEqual(self.trie.search([[13, 12, 11]]), True)
        self.assertEqual(self.trie.search([[13, 15, 16, 13]]), True)
        self.assertEqual(self.trie.search([[13]]), True)
