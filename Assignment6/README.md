# Assignment #6: Dependency parsing using machine learning techniques
## Objectives
The objectives of this assignment are to:

Extract feature vectors and train a classifier
Write a statistical dependency parser
Understand how to design parameter sets
Write a short report on your results

## Programming
This assignment is inspired by the shared task of the Tenth conference on computational natural language learning, CONLL-X, and uses similar data. The conference site contains a description of multilingual dependency parsing, reference papers, training and test sets for a variety of languages, as well as evaluation programs. See also CONLL 2007, on the same topic.

Please note that the original CoNLL-X site is down. To access the pages, use the Archive.org site: https://web.archive.org/web/20161105025307/http://ilk.uvt.nl/conll/ and to download the data sets, use the local copies.

In this session, you will implement and test a dependency parser for Swedish using machine learning techniques.

## Choosing a training and a test sets
### The CONLL-X annotated corpora and annotation scheme are available here. The Swedish corpus called Talbanken was originally collected and annotated in Lund and modified by Joakim Nivre. Read details on the corpus and references here.

### In this assignment, you will use the CONLL-X Swedish corpus. Download the tar archives containing the training and test sets for Swedish and uncompress them: [data sets](http://ilk.uvt.nl/conll/free_data.html). Local copies: [training set](http://fileadmin.cs.lth.se/cs/Education/EDAN20/corpus/conllx/sv/swedish_talbanken05_train.conll) [test set](http://fileadmin.cs.lth.se/cs/Education/EDAN20/corpus/conllx/sv/swedish_talbanken05_test_blind.conll) [test set with answers](http://fileadmin.cs.lth.se/cs/Education/EDAN20/corpus/conllx/sv/swedish_talbanken05_test.conll).

## Training the classifiers
If you have not done it in the previous assignment, for each data set you have generated, fit a corresponding model using logistic regression (or another classifier if you want) and save it.

## Parsing the corpus and evaluating the results
Once you have generated your models, you will embed them in Nivre's parser and compute their respective efficiencies.

Your parser will proceed, sentence by sentence, and word by word. For a certain state, it will predict the next action using your classifier. You will then execute the corresponding action: la, ra, re, or sh. If an action is not possible, you will carry out a shift.

You are free to implement it the way you want. Here are some suggestions:

### The loop will basically have this structure:
```python
while queue:
    features.extract()
    trans_nr = classifier.predict()
    stack, queue, graph, trans = parse_ml(stack, queue, graph, trans)
```

### The parsing function, parse_ml(), takes the the stack, queue, graph, and the transition predicted by the classifier, and carries out the transition. You can use this model and complete it:
```python
def parse_ml(stack, queue, graph, trans):
    if stack and trans[:2] == 'ra':
        stack, queue, graph = transition.right_arc(stack, queue, graph, trans[3:])
        return stack, queue, graph, 'ra'
    ...
```

where trans is either ra.deprel, la.deprel, re, or sh.

### You will then use the partial graph to write the values of the heads and functions to the words.

### Finally, you will save the sentences in an output file.

### Once you have parsed the test set, you will measure the accuracy of your parser using the CoNLL evaluation script [3]. Local copy: [eval.pl](http://fileadmin.cs.lth.se/cs/Education/EDAN20/corpus/conllx/eval.txt). You will run this script using the command:perl eval.pl -g gold_standard_file -s system_output -q, where -q stands for quiet.

### You will run the parser with the three feature sets described in the fifth assignment to carry out a labelled dependency parsing.

### You need to reach a labelled attachment score of 75 to pass this lab.

## Complement (Optional)
Read the text Labeled Pseudo-Projective Dependency Parsing with Support Vector Machines by Joakim Nivre et al. (2006) [pdf](http://w3.msi.vxu.se/~nivre/papers/malt_shared.pdf). Read the slides [here](http://ilk.uvt.nl/conll/slides/Nivre.pdf).
