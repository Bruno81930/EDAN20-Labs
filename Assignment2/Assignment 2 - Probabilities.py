import sys
import regex as re
import math


def tokenize(text):
    text = re.sub('\s+',' ', text) 
    text = re.sub('\s*(\p{P})\s*',r'\1', text)
    text = re.sub('([\p{Lu}][0-9\p{L}\"\:,;\-\?\!\' ]+[\.])', '<s>' + r' \1 ' + '</s>\n', text).lower()
    text = re.sub('[^\P{P}\/]'," ", text)
    words = re.findall('[\p{L}\<\/\>]+', text)
    return words

def count_unigrams(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def count_bigrams(words):
    bigrams = [tuple(words[i:i+2]) for i in range(len(words) - 1)]
    
    frequency_bigrams = {}
    for bigram in bigrams:
        if bigram in frequency_bigrams:
            frequency_bigrams[bigram] += 1
        else:
            frequency_bigrams[bigram] = 1
    
    return frequency_bigrams
        

if __name__ == '__main__':
    text = sys.stdin.read()
    words = tokenize(text)
    frequency = count_unigrams(words)
    print("Unigram Model")
    print("=====================================================")
    print("wi C(wi) #words P(wi)")
    print("=====================================================")
    prob_unigram = 1
    entropy = 0
    for word in sys.argv[1:]:
        word = word.lower()
        prob = frequency[word]/len(words)
        prob_unigram *= prob
        entropy += math.log(prob,2)
        print(word, '\t', frequency[word], "\t", len(words), "\t", prob)
    opn_stc = "<s>"
    cls_stc = "</s>"
    prob_unigram *= frequency[cls_stc]/len(words)
    geo_prob = math.pow(prob_unigram, 1/(len(sys.argv)-1))
    print(cls_stc, '\t', frequency[cls_stc], "\t", len(words), "\t", frequency[cls_stc]/len(words))
    print("=====================================================")
    print("Prob. unigrams: " + str(prob_unigram))
    print("Geometric mean prob.: " + str(geo_prob))
    print("Entropy rate: " + str(-entropy/(len(sys.argv)-1)))
    print("Perplexity: " + str(math.pow(2, -entropy/(len(sys.argv)-1))))
    
    frequency_bigram = count_bigrams(words)
    print("\nBigram model")
    print("=====================================================")
    print("wi wi+1 Ci,i+1 C(i) P(wi+1|wi)")
    print("=====================================================")
    sentence = list()
    
    sentence.append(opn_stc)
    for pos in range(1, len(sys.argv)):
        sentence.append(sys.argv[pos].lower())
    sentence.append(cls_stc)
    
    prob_bigram = 1
    entropy = 0
    for pos in range(len(sentence) - 1):
        if((sentence[pos], sentence[pos + 1]) in frequency_bigram):
            ci_iplus1 = frequency_bigram[(sentence[pos], sentence[pos + 1])]
            ci = frequency[sentence[pos]]
            prob = ci_iplus1/ci            
            print(sentence[pos] + "\t" + sentence[pos + 1] + "\t" + str(ci_iplus1) + "\t" + str(ci) + "\t" + str(prob))
        else:
            prob = frequency[sentence[pos + 1]] / len(words)
            print(sentence[pos] + "\t" + sentence[pos + 1] + "\t" + "0" + "\t" + str(frequency[sentence[pos]]) + "\t" + "0.0 *backoff: " + str(prob))
        prob_bigram *= prob
        entropy += math.log(prob,2)
    
    geo_prob = math.pow(prob_bigram, 1/(len(sentence) - 1))
    
    print("=====================================================")
    print("Prob. bigrams: " + str(prob_bigram))
    print("Geometric mean prob.: " + str(geo_prob))
    print("Entropy rate: " + str(-entropy/len(sentence)))
    print("Perplexity: " + str(math.pow(2, -entropy/len(sentence))))
        