PROBLEM_DESCRIPTION = """
09. Typoglycemia
Write a program with the specification:
- Receive a word sequence separated by space
- For each word in the sequence:
  - If the word is no longer than four letters, keep the word unchanged
  - Otherwise,
    - Keep the first and last letters unchanged
    - Shuffle other letters in other positions (in the middle of the word)
Observe the result by giving a sentence, e.g., “I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind “.
"""

import random
from typing import Union

random.seed(42)

def typoglycemia(sequence : Union[str, list]):
    assert(type(sequence) in [str, list])
    if type(sequence) == str:
        sequence = sequence.split(" ")
    def shuffle_word(word : str):
        if len(word) <= 4:
            return word
        else:
            letters = list(word[1:-1])
            random.shuffle(letters)
            return word[0] + "".join(letters) + word[-1]
    return " ".join([shuffle_word(word) for word in sequence])

if __name__ == "__main__":
    s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind "
    result = typoglycemia(s)
    print(result)