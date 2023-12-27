"""
There must be some debugging coding exercise where I suppose to find
some easy bugs. Did a CodeSignal problem instead.
"""

"""
TODO:
Given an array of integers, find the pair of adjacent elements 
that has the largest product and return that product.

Example
For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.
"""

from typing import List

def solution(inputArray: List[int]) -> int:
    products = [inputArray[i] * inputArray[i + 1] for i in range(len(inputArray) - 1)]
    return max(products)