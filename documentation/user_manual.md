# User Manual
The program starts with the command `poetry run invoke start`. After inputting the order of the Markov chain and the length of the melody
(i.e. how many notes will be generated), the program generates a melody based on the music that is
in the reference.txt file. The file is located in root/src/music-folder.
Generated melody is stored into lilypond.ly which is in the same root/src/music-folder.
Lilypond.ly can be converted into pdf and midi files using a LilyPond program that needs to be downloaded separately.

[Download LilyPond](http://lilypond.org/download.html)  
[LilyPond Manual](https://lilypond.org/doc/v2.22/Documentation/web/manuals.html)
