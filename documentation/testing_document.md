# Testing Document

The program is tested with unit testing that has been implemented using Python's unittest module.

## Unit Testing

**`TestTrie`**  
  
Tested class: `Trie`  
  
What it tests: 
- sequences that have been stored to the trie can be found
- calculating next possible note from a sequence gives correct options
     
**`TestTrieNode`**
  
Tested class: `TrieNode`  
  
What it tests:
- information inside the node is stored correctly

**`TestConverter`**  
  
Tested class: `Converter`  
  
What it tests:
- when a file that contains reference music is read, the converter outputs correct information
- right-sized sequences are made out of the given music

**`TestGenerator`**  
  
Tested class: `Generator`  
  
What it tests:
- generating process leads to error when there are no possible melodies that could be generated

**`TestRun`**  
  
Tested class: `Generator`, `Run`
  
What it tests:
- when a new melody is generated, all three-sized (because the test generates with 2nd order Markov chain) sequences can be found from the trie
  
## Test coverage
![image](https://user-images.githubusercontent.com/95978191/218305292-14cc6a5f-d028-479d-bfae-1ba84c9ded22.png)
