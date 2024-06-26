PROBLEM_DESCRIPTION = """
Implement a function cipher that converts a given string with the specification:
- Every alphabetical lowercase letter c is converted to a letter \
whose ASCII code is (219 - [the ASCII code of c])
- Keep other letters unchanged
Use this function to cipher and decipher an English message.
"""

def cipher(s : str):
    return "".join([chr(219 - ord(c)) if c.islower() else c for c in s])

if __name__ == "__main__":
    s = "I am an NLPer"
    s_ciphered = cipher(s)
    s_deciphered = cipher(s_ciphered)
    print(s_ciphered)
    print(s_deciphered)