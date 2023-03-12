# Implementation Document
### Structure
`Trie` class is responsible for building the trie data structure that is used for storing and searching for note sequences. `Generator` class creates a new melody using the Markov chain. `Run` class operates the user interface and receives user inputs.

### Time & Space Complexity
Searching and inserting algorithms in the trie data structure have the time complexity of O(n).  
The space complexity is also O(n).

### Suggestions For Further Development
- user can input their own reference music in predefined format
- support for a wider range of notes
- polyphonic generating
- different note durations in generated music

### Sources
[Trie (Wikipedia)](https://en.wikipedia.org/wiki/Trie)
