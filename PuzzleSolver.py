# Run with `python PuzzleSolver.py`

import twl

letter_list = []

print('Next Letter')

while len(set(letter_list)) < 7:
    new_letter = input().lower()
    if new_letter.isalpha() and len(new_letter) == 1:
        if new_letter not in letter_list:
            letter_list.append(new_letter)
        else:
            print('Letter already in list')
    else:
        print('Inputs must be letters')


print('Center Letter?')
center_letter = input()

print('Max Length? (O^n time complexity)')
desired_length = int(input())

print('Min Length?')
min_length = int(input())

print('Word Start (Press enter if none)')
word_start = str(input())



def is_word(word):
    new_word = ((str(word)).lower())
    
    return (twl.check(new_word)) 

def generate_combinations(letter_list, current_combination, desired_length, combinations):
    """
    Recursively generates combinations of numbers of a selectable length.

    Args:
    letter_list (list): List of characters to form combinations from.
    current_combination (str): Current combination being formed.
    desired_length (int): The desired length of each combination.
    combinations (list): Accumulator for storing all generated combinations.
    """
    # Base case: if the current combination's length equals the desired length
    if len(current_combination) == desired_length:
        combinations.append(current_combination)
        return

    for letter in letter_list:
        # Generate the next combination and recurse
        generate_combinations(letter_list, current_combination + letter, desired_length, combinations)

combinations = []

current_length = min_length

while current_length <= desired_length:
    generate_combinations(letter_list, '', current_length, combinations)
    current_length += 1

working_words = []



def word_list_maker(combos):
    legal_word_list = []
    for w in combos:
        if center_letter in w:
            if w[0:(len(word_start))] == word_start:
                if is_word(w.lower()):
                    working_words.append(w)
    
    for i in working_words:
        legal_word_list.append(i.upper())
    print(legal_word_list)

import timeit
statement = 'word_list_maker(combinations)'
setup_code = '''
from __main__ import word_list_maker, combinations
'''
execution_time = timeit.timeit(stmt=statement, setup=setup_code, number=1)
print(f"{execution_time} seconds")

# word_list_maker(combinations)

