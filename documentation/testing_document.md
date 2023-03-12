# Testing Document

The program is tested with unit testing that has been implemented using Python's unittest module.

## Main Functionality Testing
#### **`TestRun`**  
  
What it tests:
- the generated melody is possible based on the given reference music
- covers 1st, 2nd, and 3rd order Markov chain generating

## Unit Testing

#### **`TestTrie`**  
  
Tested class: `Trie`  
  
What it tests: 
- sequences that have been stored to the trie can be found
- calculating next possible note from a sequence gives correct options
     
#### **`TestTrieNode`**
  
Tested class: `TrieNode`  
  
What it tests:
- information inside the node is stored correctly

#### **`TestConverter`**  
  
Tested class: `Converter`  
  
What it tests:
- when a file that contains reference music is read, the converter outputs correct information
- right-sized sequences are made out of the given music

#### **`TestGenerator`**  
  
Tested class: `Generator`  
  
What it tests:
- generating process leads to error when there are no possible melodies that could be generated

#### **`TestLilypond`**  
  
Tested class: `Lilypond`  
  
What it tests:
- melody is correctly converted to lilypond syntax
  
## Test coverage
![image](https://user-images.githubusercontent.com/95978191/224540337-7d5b328e-87cb-49f4-851d-acdb2a9ded24.png)

