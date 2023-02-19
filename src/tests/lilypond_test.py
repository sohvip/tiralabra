import unittest
from lilypond import Lilypond


class TestRun(unittest.TestCase):
    def setUp(self):
        self.lilypond = Lilypond()
    
    def test_convert(self):
        melody = self.lilypond.convert(['a#', 'b', 'c', 'A', 'F#', 'a'])
        self.assertEqual(melody, ["ais'", "b'", "c''", "a", "fis'", "a'"])