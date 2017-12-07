# Assignment #1: Building an inverted index
## Objectives
The objectives of this assignment are to:

Write a program that collects all the words from a set of documents
Build an index from the words
Know what indexing is
Represent a document using the Tf.Idf value
Write a short report of 1 to 2 pages on the assignment
Read a short text on an industrial system

## Tasks
### Write a Python program.
Check the results and comment them briefly
Preparation
Download the Selma folder and uncompress it. It contains novels by Selma Lagerlöf.
Read the description of the tf-idf measure on Wikipedia (https://en.wikipedia.org/wiki/Tf-idf).
Programming the Indexer
Your program will take a corpus as input (here the Selma novels) and produce an index of all the words with their positions. you should be able to run it this way:

$ python indexer.py folder_name
Conceptually, the index will consist of rows with one word per row and and the list of files and positions, where this word occurs. Such a row is called a posting list. You will encode the position of a word by the number of characters from the start of the file.

```python
            word1: file_name pos1 pos2 pos3... file_name pos1 pos2 ...
            word2: file_name pos1 pos2 pos3... file_name pos1 pos2 ...
            ...
```

To make programming easier, you will split this exercise into three steps and you will use dictionaries to represent the postings.

### Indexing one file
Write a program that reads one document file_name.txt and outputs an index file: file_name.idx:

The index file will contain all the unique words in the document, where each word is associated with the list of its positions in the document.
You will represent this index as a dictionary where the keys will be the words and the values, the lists of positions
As words, you will consider all the strings of letters that you will set in lower case. You will not index the rest (i.e. numbers or symbols).
The word positions will correspond to the number of characters from the beginning of the file. (The word offset from the beginning)
You will use finditer() to find the positions of the words. This will return you match objects, where you will get the matches and the positions with the group() and start() methods.
You will use the pickle package to write your dictionary in an file, see https://wiki.python.org/moin/UsingPickle.
Below is an excerpt of the index of the bannlyst text for the words gjord, uppklarnande, and stjärnor. The data is stored in a dictionary:

```python
            {...
            'gjord': [8551, 183692, 220875],
            'uppklarnande': [8567],
            'stjärnor': [8590], ...
            }
```

The word gjord occurs three times in the text at positions 8551, 183692, and 220875, uppklarnande, once at position 8567, and stjärnor, once at position 8590.

### Reading the content of a folder
Write a function that reads all the files in a folder with a specific suffix (txt). You will need the Python os package, see https://docs.python.org/3/library/os.html. You will return the file names in a list.

You can reuse this function:

```python
            def get_files(dir, suffix):
            """
            Returns all the files in a folder ending with suffix
            :param dir:
            :param suffix:
            :return: the list of file names
            """
            files = []
            for file in os.listdir(dir):
            if file.endswith(suffix):
            files.append(file)
            return files
```

### Creating a master index
Complete your program with the creation of master index, where you will associate each word of the corpus with the files, where it occur and its positions. (a posting list)

Below is an except of the master index with the words samlar and ände:

```python
            'samlar':
            {'nils.txt': [53499, 120336],
            'gosta.txt': [317119, 414300, 543686],
            'osynliga.txt': [410995, 871322]},
            'ände':
            {'nils.txt': [3991],
            'kejsaren.txt': [51100],
            'marbacka.txt': [374231],
            'troll.txt': [39726],
            'osynliga.txt': [742747]},
```

The word samlar, for instance, occurs three times in the gosta text at positions 317119, 414300, and 543686.

### Representing Documents with tf-idf
Once you have created the index, you will represent each document in your corpus as a word vector. You will define the value of a word in a document with the tf-idf metric. Tf will be the relative frequency of the term in the document and idf, the logarithm base 10 of the inverse document frequency.

You have below the tf-idf values for a few words. In our example, the word gås has the value 0 in bannlyst.txt and the value 0.000101237 in nils.txt

```
            bannlyst.txt
            känna 0.0
            gås 0.0
            nils 0.0
            et 6.2846093167673765e-06
            gosta.txt
            känna 0.0
            gås 0.0
            nils 0.0
            et 0.0
            herrgard.txt
            känna 0.0
            gås 0.0
            nils 0.0
            et 0.0
            jerusalem.txt
            känna 0.0
            gås 0.0
            nils 4.778415355159037e-06
            et 0.0
            nils.txt
            känna 0.0
            gås 0.00010123719421964931
            nils 9.801209641132888e-05
            et 0.0
```

### Comparing Documents
Using the cosine similarity, compare all the pairs of documents with their tfidf representation and present your results in a matrix.

What are the two novels that are the most similar?

### Complement
Read the text Challenges in Building Large-Scale Information Retrieval Systems about the history of Google indexing by Jeff Dean. In your report, tell how your index encoding is related to what Google did.
