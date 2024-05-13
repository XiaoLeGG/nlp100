PROBLEM_DESCRIPTION = """
03. Pi
Split the sentence “Now I need a drink, alcoholic of course, \
after the heavy lectures involving quantum mechanics”. \
into words, and create a list whose element presents \
the number of alphabetical letters \
in the corresponding word.
"""

if __name__ == "__main__":
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"
    s = s.replace(",", "").replace(".", "")
    words = s.split(" ")
    result = [len(word) for word in words]
    print(result)