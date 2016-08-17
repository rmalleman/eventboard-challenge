#!/usr/bin/env python

import re
import time
import argparse


def count_words_in_a_file(file_name):
    """
    Counts the number of words in a file

    :param file_name:
    :return: a dict containing the word as a key and the corresponding count as the value
    """
    with open(file_name) as f:
        string = f.read()

    return word_count(string)


def word_count(string):
    """
    count the number of words in a string and return a dict with the word as the key and the corresponding count as
    a value

    :param string: string to be processed
    :return: a dict containing the word as a key and the corresponding count as the value
    """
    words = string.split()
    #regex for everything that is not a word
    pattern = re.compile('[\W_]+')
    output = {}
    for word in words:
        word = pattern.sub('', word.lower())
        #we don't want to count blank strings
        if word == '':
            continue
        if word in output:
            output[word] += 1
        else:
            output[word] = 1
    return output


def main():
    parser = argparse.ArgumentParser(description='Utility to count words')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--file', help="process a file")
    group.add_argument('--string', help="process a string")
    args = parser.parse_args()

    now = time.time()
    if args.file:
        print(count_words_in_a_file(args.file))
    elif args.string:
        print(word_count(args.string    ))
    else:
        parser.print_help()

    print("Processed in {} seconds".format(time.time() - now))


if __name__ == '__main__':
    main()