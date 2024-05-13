PROBLEM_DESCRIPTION = """
06. Set
Let the sets of letter bi-grams from the words “paraparaparadise” and “paragraph” \
$X$ and $Y$, respectively. Obtain the union, intersection, difference of the two sets. \
In addition, check whether the bigram “se” is included in the sets $X$ and $Y$
"""

from typing import Union

def letter_n_grams(sequence : Union[str, list], n : int):
    assert(type(sequence) in [str, list])
    return set(zip(*[sequence[i:] for i in range(n)]))

if __name__ == "__main__":
    s1 = "paraparaparadise"
    s2 = "paragraph"
    X = letter_n_grams(s1, 2)
    Y = letter_n_grams(s2, 2)
    print(f"1. X({len(X)}): {X}")
    print(f"2. Y({len(Y)}): {Y}")
    print(f"3. Union({len(X | Y)}): {X | Y}")
    print(f"4. Intersection({len(X & Y)}): {X & Y}")
    print(f"5. Difference({len(X - Y)}): {X - Y}")
    print(f"6. '(s, e)' in X: {('s', 'e') in X}")
    print(f"7. '(s, e)' in Y: {('s', 'e') in Y}")