PROBLEM_DESCRIPTION = """
05. n-gram
Implement a function that obtains n-grams from a given sequence object (e.g., string and list). \
Use this function to obtain word bi-grams and letter bi-grams from the sentence “I am an NLPer”
"""

from typing import Union

def n_grams(sequence : Union[str, list], n : int):
    assert(type(sequence) in [str, list])
    if type(sequence) == str:
        sequence = sequence.replace(",", "").replace(".", "")
        sequence = sequence.split(" ")
    # tricky way to get n-grams, using the idea of shifting
    # I didn't get this at first XD
    return list(zip(*[sequence[i:] for i in range(n)]))

if __name__ == "__main__":
    s = "I am an NLPer"
    print(n_grams(s, 2))