def problem(word, offense):
    return ''.join([c for c in word if c in offense]) == offense

def problem_count(offense):
    with open("enable1.txt") as file:
        dictionary = set(file.read().splitlines())
    pc = sum(1 if problem(word, offense) else 0 for word in dictionary)
    return pc

if __name__ == "__main__":
    print(problem("synchronized", "snond"))
    print(problem("misfunctioned", "snond"))
    print(problem("mispronounced", "snond"))
    print(problem("shotgunned", "snond"))
    print(problem("snond", "snond"))
    print(problem_count("snond"))
    print(problem_count("rrizi"))