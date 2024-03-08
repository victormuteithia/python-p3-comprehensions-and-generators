#!/usr/bin/env python3

def return_evens(num_list):
    evens_list = [num for num in num_list if num % 2 == 0]

    return evens_list

def make_exclamation(sentence_list):
    added_exclamations = [s + "!" for s in sentence_list]

    return added_exclamations