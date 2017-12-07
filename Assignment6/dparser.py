
# coding: utf-8

# In[2]:

import time
import transition
import conll
import features
from sklearn.feature_extraction import DictVectorizer
from sklearn import linear_model

def reference(stack, queue, graph):
    """
    Gold standard parsing
    Produces a sequence of transitions from a manually-annotated corpus:
    sh, re, ra.deprel, la.deprel
    :param stack: The stack
    :param queue: The input list
    :param graph: The set of relations already parsed
    :return: the transition and the grammatical function (deprel) in the
    form of transition.deprel
    """
    # Right arc
    if stack and stack[0]['id'] == queue[0]['head']:
        #print('ra', queue[0]['deprel'], stack[0]['cpostag'], queue[0]['cpostag'])
        deprel = '.' + queue[0]['deprel']
        stack, queue, graph = transition.right_arc(stack, queue, graph)
        return stack, queue, graph, 'ra'+ deprel
    # Left arc
    if stack and queue[0]['id'] == stack[0]['head']:
        #print('la', stack[0]['deprel'], stack[0]['cpostag'], queue[0]['cpostag'])
        deprel = '.' + stack[0]['deprel']
        stack, queue, graph = transition.left_arc(stack, queue, graph)
        return stack, queue, graph, 'la' + deprel
    # Reduce
    if stack and transition.can_reduce(stack, graph):
        for word in stack:
            if (word['id'] == queue[0]['head'] or
                        word['head'] == queue[0]['id']):
                # print('re', stack[0]['cpostag'], queue[0]['cpostag'])
                stack, queue, graph = transition.reduce(stack, queue, graph)
                return stack, queue, graph, 're'
    # Shift
    # print('sh', [], queue[0]['cpostag'])
    stack, queue, graph = transition.shift(stack, queue, graph)
    return stack, queue, graph, 'sh'

def extract(stack, queue, graph, feature_names, sentence):
    X = []
    X.append(transition.can_leftarc(stack, graph))
    X.append(transition.can_reduce(stack, graph))
    try:
        X.append(stack[0]['postag'])
        X.append(stack[0]['form'])
    except:
        X.append("nil")
        X.append("nil")
    try:
        X.append(stack[1]['postag'])
        X.append(stack[1]['form'])
    except:
        X.append("nil")
        X.append("nil")
    X1 = X
    try:
        X.append(queue[0]['postag'])
        X.append(queue[0]['form'])
    except:
        X.append("nil")
        X.append("nil")
    try:
        X.append(queue[1]['postag'])
        X.append(queue[1]['form'])
    except:
        X.append("nil")
        X.append("nil")
    X2 = X
    try:
        for i in range(len(sentence)):
            if sentence[i]['form'] == stack[0]['form']:
                X.append(sentence[i+1]['postag'])
                X.append(sentence[i+1]['form'])
    except:
        X.append("nil")
        X.append("nil")
        
    try:
        X.append(sentence[int(stack[1]['head'])]['postag'])
        X.append(sentence[int(stack[1]['head'])]['form'])
    except:
        X.append("nil")
        X.append("nil")
    X3 = X
    X1 = dict(zip(feature_names[:6], X1))
    X2 = dict(zip(feature_names[:10], X2))
    X3 = dict(zip(feature_names, X3))
    return X1, X2, X3

def encode_classes(y_symbols):
    
    # We extract the chunk names
    classes = sorted(list(set(y_symbols)))
    
    # We assign each name a number
    dict_classes = dict(enumerate(classes))

    # We build an inverted dictionary
    inv_dict_classes = {v: k for k, v in dict_classes.items()}

    # We convert y_symbols into a numerical vector
    y = [inv_dict_classes[i] for i in y_symbols]
    
    return y, dict_classes, inv_dict_classes

if __name__ == '__main__':
    train_file = './swedish_talbanken05_train.conll'
    test_file = './swedish_talbanken05_test_blind.conll'
    column_names_2006 = ['id', 'form', 'lemma', 'cpostag', 'postag', 'feats', 'head', 'deprel', 'phead', 'pdeprel']
    column_names_2006_test = ['id', 'form', 'lemma', 'cpostag', 'postag', 'feats']
    feature_names = ['can-la', 'can-re','stack0_POS', 'stack0_word', 'stack1_POS', 'stack1_word', 'queue0_POS', 'queue0_word', 'queue1_POS', 'queue1_word', 'stack0fw_POS', 'stack0fw_word','stack1h_POS','stack1h_word']

    sentences = conll.read_sentences(train_file)
    formatted_corpus = conll.split_rows(sentences, column_names_2006)
    
    sent_cnt = 0
    X1_dict = []
    X2_dict = []
    X3_dict = []
    Y = []
    print("Extracting the features...")
    for sentence in formatted_corpus:
        sent_cnt += 1
        if sent_cnt % 1000 == 0:
            print(sent_cnt, 'sentences on', len(formatted_corpus), flush=True)
        stack = []
        queue = list(sentence)
        graph = {}
        graph['heads'] = {}
        graph['heads']['0'] = '0'
        graph['deprels'] = {}
        graph['deprels']['0'] = 'ROOT'
        while queue:
            x1, x2, x3 = extract(stack, queue, graph, feature_names, sentence)
            X1_dict.append(x1)
            X2_dict.append(x2)
            X3_dict.append(x3)
            stack, queue, graph, trans = reference(stack, queue, graph)
            Y.append(trans)
        stack, graph = transition.empty_stack(stack, graph)
        #print('Equal graphs:', transition.equal_graphs(sentence, graph))

        # Poorman's projectivization to have well-formed graphs.
        for word in sentence:
            word['head'] = graph['heads'][word['id']]
        
    print("Encoding the features and classes...")
    # Vectorize the feature matrix and carry out a one-hot encoding
    vec = DictVectorizer(sparse=True)
    X1 = vec.fit_transform(X1_dict)
    X2 = vec.fit_transform(X2_dict)
    X3 = vec.fit_transform(X3_dict)
    y, dict_classes, inv_dict_classes = encode_classes(Y)
    
    print(X1)
    '''print("Training the models...")
    classifier = linear_model.LogisticRegression(penalty='l2', dual=True, solver='liblinear')
    print("Training the first model...")
    model1_train_time = time.clock() 
    model1 = classifier.fit(X1, y)
    print("Model 1 training time = " + str((time.clock() - model1_train_time)/60))
    print("Training the second model...")
    model2_train_time = time.clock()
    model2 = classifier.fit(X2, y)
    print("Model 2 training time = " + str((time.clock() - model2_train_time)/60))
    print("Training the third model...")
    model3_train_time = time.clock()
    model3 = classifier.fit(X3, y)
    print("Model 3 training time = " + str((time.clock() - model2_train_time)/60))'''
    
    
    


# In[ ]:



