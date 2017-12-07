# Assignment #3: Extracting noun groups using machine learning techniques
## Objectives
The objectives of this assignment are to:

Write a program to detect partial syntactic structures
Understand the principles of supervised machine learning techniques applied to language processing
Use a popular machine learning toolkit: scikit-learn
Write a short report of 1 to 2 pages on the assignment

## Tasks
### Choosing a training and a test sets
As annotated data and annotation scheme, you will use the data available from CoNLL 2000.
Download both the training and test sets (the same as in the previous assignment) and decompress them.
(Local copies available here: [train.txt] [test.txt].)
Be sure that you have the scikit-learn package: Start it by typing import sklearn in Python.
### Baseline
Most statistical algorithms for language processing start with a so-called baseline. The baseline figure corresponds to the application of a minimal technique that is used to assess the difficulty of a task and for comparison with further programs.

#### Read the baseline proposed by the organizers of the CoNLL 2000 shared task (In the Results Sect.). What do you think of it?
#### Implement this baseline program. You may either create a completely new program or start from an existing program that you will modify [ Program folder ].
##### Complete the train function so that it computes the chunk distribution for each part of speech. You will use the train file to derive your distribution and you will store the results in a dictionary. Below, you have an excerpt of the expected results:
```python
  {'JJR':
  {'I-ADVP': 17, 'I-ADJP': 45, 'I-NP': 204, 'B-ADVP': 63,
  'B-PP': 2, 'B-ADJP': 111, 'B-NP': 382, 'B-VP': 2,
  'I-VP': 11, 'O': 16},
  'CC':
  {'B-ADVP': 3, 'O': 3676, 'I-VP': 104, 'B-CONJP': 6,
  'I-ADVP': 30, 'I-UCP': 2, 'I-PP': 24, 'I-ADJP': 26,
  'I-NP': 1409, 'B-ADJP': 2, 'B-NP': 18, 'B-PP': 70,
  'I-PRT': 1, 'B-VP': 1},
  'NN':
  {'B-LST': 2, 'I-INTJ': 2, 'B-ADVP': 38, 'O': 37,
  'I-ADVP': 11, 'B-INTJ': 1, 'I-UCP': 2, 'B-UCP': 2,
  'I-VP': 77, 'B-PRT': 2, 'I-ADJP': 41, 'I-NP': 24456,
  'B-ADJP': 44, 'B-NP': 5160, 'B-PP': 15, 'B-VP': 257},
  ...
```
##### For each part of speech, select the most frequent chunk. In the example above, you will have (NN, I-NP)
##### Using the resulting associations, apply your chunker to the test file.
##### You will store your results in an output file that has four columns. The three first columns will be the input columns from the test file: word, part of speech, and gold-standard chunk. You will append the predicted chunk as the 4th column. Your output file should look like the excerpt below. Here the gold-standard chunks and the predicted chunks are exactly the same:
```
Rockwell NNP B-NP B-NP
International NNP I-NP I-NP
Corp. NNP I-NP I-NP
's POS B-NP B-NP
Tulsa NNP I-NP I-NP
unit NN I-NP I-NP
said VBD B-VP B-VP
it PRP B-NP B-NP
```

The CoNLL 2000 evaluation script will use these two last columns, chunk and predicted chunk, to compute the performance.

#### Measure the performance of the system. Use the conlleval.txt evaluation program used by the CoNLL 2000 shared task.
##### conlleval.txt is the official CoNLL Perl script. It expects the two last columns of the test set to be the manually assigned chunk (gold standard) and the predicted chunk.
##### Start it like this:
```
                            $ conlleval.txt <out
```

where the out file contains both the gold and predicted chunk tags. conlleval.txt is a Perl script.
##### Perl is installed on most Unix distributions. If it is not installed on your machine, you need to install it. Make also sure that you have the execution rights. Otherwise change them with:
                            $ chmod +x conlleval.txt

##### The conlleval.txt script expects the new lines to be \n as in Unix. If you run your Python program on Windows, your new lines will be \r\n. To have the correct new lines, add this parameter to open(): newline='\n’ like this:
                            f_out = open('out', ‘w’, newline='\n’)

##### The complete description of the CoNLL 2000 evaluation script is available here: https://www.clips.uantwerpen.be/conll2000/chunking/output.html.

### Using Machine Learning
In this exercise, you will apply and extend the ml_chunker.py program. You will start from the original program you downloaded and modify it so that you understand how to improve the performance of your chunker. You will not add new features to the feature vector.

The program that won the CoNLL 2000 shared task (Kudoh and Matsumoto, 2000) used a window of five words around the chunk tag to identify, c i . They built a feature vector consisting of:

The values of the five words in this window: w i-2 , w i-1 , w i , w i+1 , w i+2
The values of the five parts of speech in this window: t i-2 , t i-1 , t i , t i+1 , t i+2
The values of the two previous chunk tags in the first part of the window: c i-2 , c i-1
The two last parameters are said to be dynamic because the program computes them at run-time. Kudoh and Matsumoto trained a classifier based on support vector machines. Read Kudoh and Matsumoto's paper and the Yamcha software site.

What is the feature vector that corresponds to the program? Is it the same Kudoh and Matsumoto used in their experiment?
What is the performance of the chunker?
Remove the lexical features (the words) from the feature vector and measure the performance. You should observe a decrease.
What is the classifier used in the program? Try two other classifiers and measure their performance: decision trees, perceptron, support vector machines, etc.. Be aware that support vector machines take a long time to train: up to one hour.

### Improving the Chunker
Implement one of these two options, the first one being easier.

Complement the feature vector used in the previous section with the two dynamic features, c i-2 , c i-1 , and train a new model. You will need to modify the extract_features_sent and predict functions. Be aware that when you predict the test set, you do not know the dynamic features in advance and you must not read them from the test file. You need to reuse the two previous chunk tags that you have predicted.
If you know what beam search is, apply it using the probability output of logistic regression or the score if you use support vector machines.
You need to reach a global F1 score of 92 to pass this laboratory.
