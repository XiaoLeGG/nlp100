PROBLEM_DESCRIPTION = """
02. “shoe” + “cold” = “schooled”
Obtain the string “schooled” by concatenating the letters in “shoe” and “cold” one after the other from head to tail.
"""

if __name__ == "__main__":
    s1 = "shoe"
    s2 = "cold"
    s = "".join([s1[i] + s2[i] for i in range(len(s1))])
    print(s)