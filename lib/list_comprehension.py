#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [evn for evn in num_list if evn % 2 == 0]
    return even_list

def make_exclamation(sentence_list):
    exclamated = [sentence+"!" for sentence in sentence_list]
    return exclamated