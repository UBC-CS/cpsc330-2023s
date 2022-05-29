from hashlib import sha1
import numpy as np
import pandas as pd
import re

def hasher(solution):
    return sha1(str(solution).encode("utf8")).hexdigest()

def ex1_2_1(solution):
    return hasher(solution) == "727b91d884db932a1f590bc99541feb131500226"

def ex1_2_2(solution):
    return hasher(solution) == "30eaac2448e15a0f225eb5cdce96060251011ce3"

def ex1_4_1(solution):
    return hasher(solution) == "0cf1aeac0372e10da230a32e74c9b6e68dca7342"

def ex1_4_2(solution):
    return hasher(solution) == "015b8dcbc023be1734f726ca9af614fbb5b87611"

def ex1_4_3(solution):
    return hasher(solution) == "3376819896e7bc81c98e38e5bc083bc8cd64a607"

def ex1_4_4(solution):
    return hasher(solution) == "f9abd2856543ce79bc0d47e89549f02d79e67684"

def ex1_4_5(solution):
    return hasher(solution) == "4c8989fced2c5bfccae6b51aade0bc32af9de155"

def ex1_4_6(solution):
    return hasher(solution) == "eacacf4c3bd3e66d2bf0ae6064676a9b8ccc1e3b"


def run_all_autograded_tests(tests, results):
    with open("lab1.ipynb", encoding="utf-8") as f:
        total_autogrades = re.findall("rubric={autograde:(\d).*}", f.read())
    print(f"Autograded questions passed: {sum(results)} / {len(total_autogrades)}")
    print(
        f" Autograded points achieved: {sum([int(digit) for r, digit in zip(results, total_autogrades) if r])} / {sum([int(digit) for digit in total_autogrades])}"
    )
    if sum(results) < len(total_autogrades):
        print("")
        [
            print(f"FAILED: {test}")
            for (test, result) in zip(tests, results)
            if not result
        ]
