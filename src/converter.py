class Converter:
    """Converts the reference music to a form that can be inserted to the data structure.
    """

    def __init__(self):
        """The constructor.
        """
        self.convert_list = {'A': 1, 'A#': 2, 'B': 3, 'C': 4, 'C#': 5,
                             'D': 6, 'D#': 7, 'E': 8, 'F': 9, 'F#': 10, 'G': 11, 'G#': 12,
                             'a': 13, 'a#': 14, 'b': 15, 'c': 16, 'c#': 17, 'd': 18,
                             'd#': 19, 'e': 20, 'f': 21, 'f#': 22, 'g': 23, 'g#': 24}
        self.convert_list_2 = {value: key for key, value in self.convert_list.items()}

    def read_file(self, reference):
        """Reads the reference.txt file that stores the reference data.

        Returns:
            A call to another method that converts the reference data to a usable form.
        """
        raw_list = []
        with open(reference, 'r', encoding='utf-8') as file:
            music_2 = file.read()
            for i, note in enumerate(music_2):
                if note == '#':
                    raw_list.pop()
                    raw_list.append(f'{music_2[i-1]}#')
                else:
                    raw_list.append(note)
            file.close()
            return self.char_to_int(raw_list)

    def char_to_int(self, notes):
        """Converts notes to tuples that contain the number corresponding
        to the note and the name of the note itself.

        Args:
            notes: List of notes.

        Returns:
            The converted list.
        """
        for i, note in enumerate(notes):
            notes[i] = (self.convert_list[note], note)

        return notes

    def char_to_int_2(self, notes):
        """Converts notes to the numbers corresponding to the notes.
        (This method is for test use only.)
        Args:
            notes: List of notes.

        Returns:
            The converted list.
        """
        for i, note in enumerate(notes):
            notes[i] = self.convert_list[note]

        return notes

    def sequence_maker(self, melody, order):
        """Makes certain length sequences out of the given melody.

        Args:
            melody: A sequence of notes.
            order: Order of the Markov Chain.
                (determines how long sequences are needed)

        Returns:
            Note sequences in a list.
        """
        sequences = []
        for i in range(len(melody)-order):
            sequences.append([melody[i]])
            for j in range(1, order+1):
                sequences[i].append(melody[i+j])
        return sequences
