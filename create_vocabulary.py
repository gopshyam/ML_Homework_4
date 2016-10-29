#! /user/bin/env python

import pickle

train_data_file = "hw4data/traindata.txt"
stop_words_file = "hw4data/stoplist.txt"
train_label_file = "hw4data/trainlabels.txt"

def find_prior():
    with open(train_label_file, 'r') as f: 
        train_labels = [int(x.strip()) for x in f.readlines()]

    return train_labels.count(0)/float(len(train_labels)), train_labels.count(1)/float(len(train_labels))


def main():
    
    sentences = list()
    vocabulary = dict()
    stop_words = list()

    with open(stop_words_file, 'r') as f:
        stop_words = [x.strip() for x in f.readlines()]

    with open(train_label_file, 'r') as f:
        train_labels = [int(x.strip()) for x in f.readlines()]

    with open(train_data_file, 'r') as f:
        sentences = f.readlines()

    for sentence, label in zip(sentences, train_labels):
        words = sentence.strip().split(' ')
        for word in words:
            if word not in stop_words:
                if word in vocabulary:
                    vocabulary[word][label] += 1
                else:
                    val = [0,0]
                    val[label] += 1
                    vocabulary[word] = val

    with open('vocabulary', 'w') as f:
        pickle.dump(vocabulary, f)

if __name__ == "__main__":
    main()
                
