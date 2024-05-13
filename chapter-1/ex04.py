PROBLEM_DESCRIPTION = """
04. Atomic symbols
Split the sentence “Hi He Lied Because Boron Could Not Oxidize Fluorine. \
New Nations Might Also Sign Peace Security Clause. Arthur King Can”. \
into words, and extract the first letter from the 1st, 5th, 6th, 7th, \
8th, 9th, 15th, 16th, 19th words and the first two letters from the other \
words. Create an associative array (dictionary object or mapping object) that \
maps from the extracted string to the position (offset in the sentence) of the corresponding word.
"""

# The problem seems ambiguous at some points:
# The more accurate description for "(offset in the sentence)" should be "(index of the words list)"
# Because in Japanese "(先頭から何番目の単語か)"

if __name__ == "__main__":
    s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    words = s.split(" ")
    extract_indices = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    extract_indices = [i - 1 for i in extract_indices]
    result = {}
    for i, word in enumerate(words):
        if i in extract_indices:
            result[word[0]] = i
        else:
            result[word[:2]] = i
    print(result)