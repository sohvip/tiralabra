class Converter:
    def __init__(self):
        self.convert_list = {'A': 1, 'A#': 2, 'B': 3, 'C': 4, 'C#': 5,
        'D': 6, 'D#': 7, 'E': 8, 'F': 9, 'F#': 10, 'G': 11, 'G#': 12,
        'a': 13, 'a#': 14, 'b': 15, 'c': 16, 'c#': 17, 'd': 18,
        'd#': 19, 'e': 20, 'f': 21, 'f#': 22, 'g': 23, 'g#': 24}
        self.convert_list_2 = dict([(value, key) for key, value in self.convert_list.items()])
    
    def read_file(self):
        """Reads the reference.txt file that stores the reference data.
        
        Returns:
            A call to another method that converts the reference data to a usable form.
        """
        list = []
        music = open('reference.txt','r')
        music_2 = music.read()
        for i in range(len(music_2)):
            if music_2[i] == '#':
                list.pop()
                list.append(f'{music_2[i-1]}#')
            else:
                list.append(music_2[i])
        music.close()
        return self.char_to_int(list)

    def char_to_int(self, notes):
        """Converts notes to numbers:
            a -> 1
            a# -> 2
            b -> 3
            ...
            g# -> 12

        Args:
            notes: List of notes.

        Returns:
            A call to a method that makes three note long sequences.
        """
        for i in range(len(notes)):
            notes[i] = (self.convert_list[notes[i]], notes[i])
        
        return self.sequence_maker(notes)
    
    def sequence_maker(self, melody):
        """Makes three note long sequences out of the given melody.

        Args:
            melody: A sequence of notes.

        Returns:
            Three notes long sequences in a list.
        """
        sequences = []
        for i in range(len(melody)-2):
            sequences.append([melody[i], melody[i+1], melody[i+2]])
        return sequences