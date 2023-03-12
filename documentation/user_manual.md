# User Manual
- Start the program with `poetry run invoke start`.
- Input the number of the song you want to use.
- Give the order of the Markov chain and the length of the melody (i.e. how many notes will be generated).
- Press enter and wait for the program to generate some music.
- The music is saved as a file named lilypond.ly which is located in root/src/music.
- Lilypond.ly can be converted into pdf and midi files using LilyPond that needs to be downloaded separately.
- Sometimes the generating process will fail due to the fact that there are no follower candidates for the present sequence. In this case one should either try again with the same inputs or change them and then try again.

[Download LilyPond](http://lilypond.org/download.html)  
[LilyPond Manual](https://lilypond.org/doc/v2.22/Documentation/web/manuals.html)
