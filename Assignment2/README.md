# Assignment #2: Language models
## Objectives
The objectives of this assignment are to:

Write a program to find n-gram statistics
Compute the probability of a sentence
Know what a language model is
Write a short report of 1 to 2 pages on the assignment
Optionally read a short article on the importance of corpora

## Tasks

### Collecting a corpus
Collect a corpus of at least 750,000 words. You will check the number of words using the Unix command wc -w.
Alternatively, you can retrieve a corpus of novels by Selma Lagerlöf from this URL: http://fileadmin.cs.lth.se/cs/Education/EDAN20/corpus/Selma.txt .
Run the [concordance program](https://github.com/pnugues/ilppp/tree/master/programs/ch02/python) to print the lines containing a specific word, for instance Nils.
Run the [tokenization program](https://github.com/pnugues/ilppp/tree/master/programs/ch05/python) on your corpus and count the words using the Unix sort and uniq commands.

### Normalizing a corpus
Write a program to insert `<s> and </s>` tags to delimit sentences. You can start from the tokenization and modify it. Use a simple heuristics such as: a sentence starts with a capital letter and ends with a period. Estimate roughly the accuracy of your program.
Modify your program to remove the punctuation signs and set all the text in lower case letters.
The result should be a normalized text without punctuation signs where all the sentences are delimited with `<s> and </s>` tags.
The five last lines of the text should look like this:

```
<s> hon hade fått större kärlek av sina föräldrar än någon annan han visste och sådan kärlek måste vändas i välsignelse </s>
<s> när prästen sa detta kom alla människor att se bort mot klara gulla och de förundrade sig över vad de såg </s>
<s> prästens ord tycktes redan ha gått i uppfyllelse </s>
<s> där stod klara fina gulleborg ifrån skrolycka hon som var uppkallad efter själva solen vid sina föräldrars grav och lyste som en förklarad </s>
<s> hon var likaså vacker som den söndagen då hon gick till kyrkan i den röda klänningen om inte vackrare </s>
```

### Counting unigrams and bigrams
Read and try programs to compute the frequency of unigrams and bigrams of the training set: [Program folder](https://github.com/pnugues/ilppp/tree/master/programs/ch05/python).
What is the possible number of bigrams and their real number? Explain why such a difference. What would be the possible number of 4-grams.
Propose a solution to cope with bigrams unseen in the corpus. This topic will be discussed during the lab session.

### Computing the likelihood of a sentence
Write a program to compute a sentence's probability using unigrams. You may find useful the dictionaries that we saw in the mutual information program: [Program folder](https://github.com/pnugues/ilppp/tree/master/programs/ch05/python).
Write a program to compute the sentence probability using bigrams.
Select five sentences in your test set and run your programs on them.
Tabulate your results as in the examples below with the sentence Det var en gång en katt som hette Nils:

```
Unigram model
=====================================================
wi C(wi) #words P(wi)
=====================================================
det 22086 1086836 0.02032137323386417
var 12852 1086836 0.011825151172762036
en 13921 1086836 0.012808740233117047
gång 1332 1086836 0.0012255758918548888
en 13921 1086836 0.012808740233117047
katt 15 1086836 1.3801530313681181e-05
som 16790 1086836 0.015448512931113802
hette 107 1086836 9.845091623759242e-05
nils 84 1086836 7.728856975661462e-05
</s> 62283 1086836 0.057306714168467
=====================================================
Prob. unigrams:   4.4922846219128876e-27
Geometric mean prob.: 0.0023187115559242404
Entropy rate:   8.752460922513437
Perplexity:   431.2739967353978


Bigram model
=====================================================
wi wi+1 Ci,i+1 C(i) P(wi+1|wi)
=====================================================
<s> det 5913 62283 0.09493762342854391
det var 4023 22086 0.1821515892420538
var en 753 12852 0.05859010270774977
en gång 695 13921 0.04992457438402414
gång en 23 1332 0.017267267267267267
en katt 5 13921 0.0003591695998850657
katt som 2 15 0.13333333333333333
som hette 50 16790 0.0029779630732578916
hette nils 0 107 0.0 *backoff: 7.728856975661462e-05
nils </s> 2 84 0.023809523809523808
=====================================================
Prob. bigrams: 2.292224542392586e-19
Geometric mean prob.: 0.013678098151101147
Entropy rate: 6.191988542790593
Perplexity: 73.10957919390972

```

### Reading
As an application of n-grams, execute the Jupyter notebook by Peter Norvig [here](http://nbviewer.jupyter.org/url/norvig.com/ipython/How%20to%20Do%20Things%20with%20Words.ipynb) (just run all the cells). You will find the data here.

### Complement
As a complement, you can read a paper by Church and Hanks, [Word Association Norms, Mutual Information, and Lexicography](http://www.aclweb.org/anthology/J/J90/J90-1003.pdf), Computational Linguistics, 16(1):22-29, 1990, as well as another one on backoff by Brants et al. (2007) [Large language models in machine translation](http://www.aclweb.org/anthology/D07-1090.pdf).
