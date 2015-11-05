import random

def generate_word(pattern):
    if not all(c in "cv" for c in pattern.lower()):
        raise ValueError("All characters in the pattern must be c, C, v or V!")
    def replace(c_old):
        c_new = random.choice("bcdfghjklmnpqrstvwxyz") if c_old == 'c' else random.choice("aeiou")
        return c_new if c_old.islower() else c_new.upper()
    return ''.join(replace(c) for c in pattern)

if __name__ == "__main__":
    inputs = ["cvcvcc", "CcvV", "cvcvcvcvcvcvcvcvcvcv"]
    for i in inputs:
        print(generate_word(i))