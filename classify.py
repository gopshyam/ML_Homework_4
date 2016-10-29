#!/ usr/bin/env python

import pickle
from create_vocabulary import find_prior, find_stop_words

test_data_file = "hw4data/testdata.txt"
test_label_file = "hw4data/testlabels.txt"
vocabulary_file = "vocabulary"

def predict(sentence, vocabulary):
    #returns the probability of a sentence being 1 or 0
    zero_prob = 0
    one_prob = 0
    M = len(vocabulary)
    zero_count = sum([vocabulary[x][0] for x in vocabulary])
    one_count = sum([vocabulary[x][1] for x in vocabulary])
    total_count = zero_count + one_count
    zero_prior, one_prior = find_prior()
    stop_words = find_stop_words()

    for word in sentence.split(' '):
        if word in stop_words:
            continue
        if word in vocabulary:
            zero_likelihood = vocabulary[word][0] + 1 / float(zero_count + M)
            one_likelihood = vocabulary[word][1] + 1 / float(one_count + M)
            evidence = sum(vocabulary[word]) / float(total_count)
        else:
            zero_likelihood = 1 / float(zero_count + M)
            one_likelihood = 1 / float(one_count + M)
            evidence = 2 / float(total_count)

        zero_prob += (zero_likelihood * zero_prior) / float(evidence)
        one_prob += (one_likelihood * one_prior) / float(evidence)

    return zero_prob, one_prob
             
        


def main():
    
    sentences = list()
    labels = list()
    vocabulary = dict()

    with open(test_data_file, 'r') as f:
        sentences = [x.strip() for x in f.readlines()]

    with open(test_label_file, 'r') as f:
        labels = [int(x.strip()) for x in f.readlines()]

    with open(vocabulary_file, 'r') as f:
        vocabulary = pickle.load(f)

    for sentence, label in zip(sentences, labels):
        zero_prob, one_prob = predict(sentence, vocabulary)
        print sentence, zero_prob, one_prob
        if zero_prob > one_prob:
            if label == 0:
                print "SUCCESS"
            else:
                print "ERROR"
        else:
            if label == 1:
                print "SUCCESS"
            else:
                print "ERROR"


if __name__=="__main__":
    main()
