#!/usr/bin/env python3

###
# Softmax Activation Function Implementation (easy)
# Write a Python function that computes the softmax activation for a given list of scores. The function should return the softmax values as a list, each rounded to four decimal places.

# Example
# Example:
#         input: scores = [1, 2, 3]
#         output: [0.0900, 0.2447, 0.6652]
#         reasoning: The softmax function converts a list of values into a probability distribution. The probabilities are proportional to the exponential of each element divided by the sum of the exponentials of all elements in the list.
###

import math

def softmax(scores: list[float]) -> list[float]:
    probabilities = []
    expos = []
    sum = 0
    for score in scores:
        exp = math.exp(score)
        expos.append(exp)
        sum += exp
    for e in expos:
        probabilities.append(round(e/sum, 4))
    return probabilities

assert softmax([1, 2, 3]) == [0.0900, 0.2447, 0.6652]
print("PASSED")