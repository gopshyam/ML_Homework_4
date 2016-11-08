#!/ usr/bin/env python

import pickle
from create_vocabulary import find_prior, find_stop_words

test_data_file = "hw4data/testdata.txt"
test_label_file = "hw4data/testlabels.txt"
vocabulary_file = "vocabulary"

def predict(sentence, vocabulary):
    #returns the probability of a sentence being 1 or 0
    zero_prob = 1
    one_prob = 1
    M = len(vocabulary)
    zero_count = sum([vocabulary[x][0] for x in vocabulary])
    one_count = sum([vocabulary[x][1] for x in vocabulary])
    total_count = zero_count + one_count
    zero_count, one_count, zero_prior, one_prior = find_prior()
    stop_words = find_stop_words()

    for word in sentence.split(' '):
        if word in stop_words:
            continue
        if word in vocabulary:
            zero_likelihood = (vocabulary[word][0] + 1) / float(zero_count + 2)
            one_likelihood = (vocabulary[word][1] + 1) / float(one_count + 2)
#            print word, zero_likelihood, one_likelihood
        else:
            zero_likelihood = 1 / float(zero_count + 2)
            one_likelihood = 1 / float(one_count + 2)

        zero_prob *= (zero_likelihood)
        one_prob *= (one_likelihood)

    return (zero_prob * zero_prior), (one_prob * one_prior)
             
        


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

    successes = 0
    for sentence, label in zip(sentences, labels):
        zero_prob, one_prob = predict(sentence, vocabulary)
#        print sentence, zero_prob, one_prob
        if zero_prob > one_prob:
            if label == 0:
                print "SUCCESS"
                successes += 1
            else:
                print "ERROR"
        else:
            if label == 1:
                print "SUCCESS"
                successes += 1
            else:
                print "ERROR"

    print "Accuracy = " + str(successes * 100/float(len(sentences)))


if __name__=="__main__":
    main()
    test_data_file = "hw4data/traindata.txt"
    test_label_file = "hw4data/trainlabels.txt"
    vocabulary_file = "vocabulary"
    main()


