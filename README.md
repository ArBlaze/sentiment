# IMDB Sentiment Analysis

### Introduction

A sentiment analysis done on dataset provided by Stanford University. Source: https://ai.stanford.edu/~amaas/data/sentiment/
Data are organized as individual text files with each text file containing one link.

### Tools and purposes

* Various sklearn modules for feature extraction, classification, and metrics algorithims.
* os imports to read in directories
* random imports to randomize data after reading in data
* Collections imports to analyze word frequency to assist in creating a custom Stopwords list.
* nltk library to provide a list of commonly used Stopwords.

### Results so far

* Obtained an initial mean score accuracy of 87%, and F1 scores of 87% and 88% for classifying positive, and negative reviews
* Removed punctuation, introduced stopwords, used TF-IDF to provide weighs to words
* Improved mean accuracy scores, and F1 scores by 2%.

### TODO:

* Further improve score accuracy, with the current tools we're working with.

### References
Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, and Christopher Potts. (2011). Learning Word Vectors for Sentiment Analysis. The 49th Annual Meeting of the Association for Computational Linguistics (ACL 2011).
