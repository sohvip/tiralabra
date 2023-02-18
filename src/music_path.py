import os

dirname = os.path.dirname(__file__)

REFERENCE_FILENAME = 'reference.txt'
REFERENCE_FILE_PATH = os.path.join(dirname, 'music', REFERENCE_FILENAME)

TEST_FILENAME = 'test_piece.txt'
TEST_FILE_PATH = os.path.join(dirname, 'music', TEST_FILENAME)

LILYPOND_FILENAME = 'lilypond.ly'
LILYPOND_FILE_PATH = os.path.join(dirname, 'music', LILYPOND_FILENAME)
