# Assignment #4: Extraction of subject-verb-object triples
## Objectives
The objectives of this assignment are to:

Extract the subject–verb pairs from a parsed corpus
Extend the extraction to subject–verb–object triples
Understand how dependency parsing can help create a knowledge base
Write a short report of 1 to 2 pages on the assignment

## Tasks
This assignment is inspired by the Prismatic knowledge base used in the IBM Watson system. See this paper for details.

In this session, you will first use a parsed corpus of Swedish to extract the pairs and triples, and then apply it to other languages.

### Choosing a parsed corpus

#### In this part, you will use the CONLL-X Swedish corpus. Download the tar archives containing the training and test sets for Swedish and uncompress them: [data sets]. Local copies: [ training set] [ test set] [ test set with answers]. You will use the training set only.

#### Draw a graphical representation of the two first sentences of the training set.
#### Download What's wrong with my NLP and use it to check your representations.
#### Apply the dependency parser for Swedish of the Langforia pipelines to these sentences. Link to Lanforia pipelines: http://vilde.cs.lth.se:9000/

### Extracting the subject–verb pairs and subject–verb–object triples
You will extract all the subject–verb pairs and the subject–verb–object triples from the training corpus. To start the program, you can use the CoNLL-X reader available here. This program will enable you to read the other corpora. You can also reprogram one using the model of CoNLL 2000. You will find the description of the CoNLL-X format [here]. Archive here.

You can design the program you want. However, here are some hints on the results:

#### You will need to use Python's dictionaries. Be sure you understand them and note that you can use tuples as keys.
#### Extract all the subject-verb pairs in the corpus. The subject function uses the SS code in the Swedish corpus of CoNLL-X. In the extraction, do not check the part of speech of the verb in the pair.
#### Compute the total number of pairs. You should find 18885 pairs.
#### Sort your pairs by order of frequency and give the five most frequent pairs. Here are the frequencies you should find:
```
                    537
                    261
                    211
                    171
                    161
```

#### Extract all the subject–verb–object triples of the corpus. The object function uses the OO code. Compute the total number of triples. You should find 5844 triples.
#### Sort your triples by order of frequency and give the five most frequent pairs. Here are the frequencies you should find:
                    37
                    36
                    36
                    19
                    17

### Multilingual Corpora

Once your program is working on Swedish, you will apply it to all the other languages from this repository: Universal Dependencies. The address to download the corpora is here. You have a local version in the /usr/local/cs/EDAN20/ folder. You can read the training files from the folder using the CoNLL reader provided for the first part. You will need to adapt your program to CoNLL-U. See here.

Here are suggestions to carry out this task:

#### Some corpora expand some tokens into multiwords. This is the case in French, Spanish, and German. The table below shows examples of such expansions.
| French	    | Spanish	           | German        |
| ----------- | ------------------ | ------------- |
| du: de le   |	del: de el         |	zur: zu der  |
| des: de les |	vámonos: vamos nos |	im: in dem   |

In the corpora, you have the original tokens as well as the multiwords as with vámonos al mar.
```
                    1-2 vámonos _
                    1 vamos ir
                    2 nos nosotros
                    3-4 al _
                    3 a a
                    4 el el
                    5 mar mar
```

Read the format description for the details: [CoNLL-U format](http://universaldependencies.org/format.html).

#### If you represent the sentences as lists, the item indexes are not reliable: In the format description, the token at position 1 is vamos and not vámonos. You have two ways to cope with this:

##### Either remove all the lines that include a range in the id field.
##### or encode the sentences as dictionaries (preferable), where the keys are the id numbers. Here are the results for the second sentence of the Swedish CoNLL X corpus:
```python
{'5': {'pdeprel': '_', 'lemma': '_', 'postag': 'NN', 'phead': '_', 'feats': '_', 'form':
'dagens', 'id': '5', 'deprel': 'DT', 'cpostag': 'NN', 'head': '6'},
'7': {'pdeprel': '_', 'lemma': '_', 'postag': 'IP', 'phead': '_', 'feats': '_', 'form': '.',
'id': '7', 'deprel': 'IP', 'cpostag': 'IP', 'head': '1'},
'3': {'pdeprel': '_', 'lemma': '_', 'postag': 'TP', 'phead': '_', 'feats': '_', 'form':
'berättigad', 'id': '3', 'deprel': 'SP', 'cpostag': 'TP', 'head': '1'},
'1': {'pdeprel': '_', 'lemma': '_', 'postag': 'AV', 'phead': '_', 'feats': '_', 'form':
'Är', 'id': '1', 'deprel': 'ROOT', 'cpostag': 'AV', 'head': '0'},
'6': {'pdeprel': '_', 'lemma': '_', 'postag': 'NN', 'phead': '_', 'feats': '_', 'form':
'samhälle', 'id': '6', 'deprel': 'PA', 'cpostag': 'NN', 'head': '4'},
'2': {'pdeprel': '_', 'lemma': '_', 'postag': 'PO', 'phead': '_', 'feats': '_', 'form':
'den', 'id': '2', 'deprel': 'SS', 'cpostag': 'PO', 'head': '1'},
'0': {'pdeprel': 'ROOT', 'lemma': 'ROOT', 'postag': 'ROOT', 'phead': '0', 'feats': 'ROOT',
'form': 'ROOT', 'id': '0', 'deprel': 'ROOT', 'cpostag': 'ROOT', 'head': '0'},
 '4': {'pdeprel': '_', 'lemma': '_', 'postag': 'PR', 'phead': '_', 'feats': '_', 'form': 'i',
'id': '4', 'deprel': 'RA', 'cpostag': 'PR', 'head': '1'}}
```

#### Some corpora have sentence numbers. Here you solve it by discarding lines starting with a #. This is already done in the CoNLL reader.
#### All the corpora in the universal dependencies format use the same function names: nsubj and obj for the subject and direct object.
#### Report the five most frequent pairs and triples you obtained in three languages. Preferably, languages you can decipher so that you can check the tuples are relevant. Otherwise, use Google Translate.

### Solving coreferences (Optional)
In this part, you will resolve a simple anaphor involving the Swedish som ‘who’ pronoun.

Use What's wrong with my NLP to derive a simple rule to find the antecedent of som
Replace all the occurrences of som as a subject with its antecedent in your pairs and triples.
