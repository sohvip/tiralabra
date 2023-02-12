class Lilypond:
    """Creates a lilypond-readable file out of the generated music.
    """

    def __init__(self):
        """The constructor.
        """

        self.notation = {'A': 'a', 'A#': 'ais', 'B': 'b', 'C': "c'", 'C#': "cis'",
                             'D': "d'", 'D#': "dis'", 'E': "e'", 'F': "f'", 'F#': "fis'", 'G': "g'", 'G#': "gis'",
                             'a': "a'", 'a#': "ais'", 'b': "b'", 'c': "c''", 'c#': "cis''", 'd': "d''",
                             'd#': "dis''", 'e': "e''", 'f': "f''", 'f#': "fis''", 'g': "g''", 'g#': "g''"}
        
    def write(self, melody):
        """Writes the melody to to a file in a lilypond syntax.

        Args:
            melody: The melody that the generator made.
        """

        melody = self.convert(melody)
        with open('music/lilypond.ly', 'w') as file:
            version = 'version "2.24.1"\n'
            version = version.replace('version', '\\version')
            file.write(version)
            file.write('{\n')
            for note in melody:
                file.write(f"{note} ")
            file.write('\n}')
            file.close()
    
    def convert(self, melody):
        """Converts melody to lilypond-notation.

        Args:
            melody: The melody that the generator made.

        Returns:
            Melody in lilypond-syntax.
        """
        for i in range(len(melody)):
            melody[i] = self.notation[melody[i]]
        return melody

if __name__ == "__main__":
    lilypond = Lilypond()
    lilypond.write(['a#', 'b', 'c'])