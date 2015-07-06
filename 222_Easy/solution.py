def balance(word):
    weight = lambda char: "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(char) + 1
    for pos, char in enumerate(word):
        lscore = sum((pos - i) * weight(c.upper()) for i, c in enumerate(word[:pos]))
        rscore = sum((i - pos) * weight(c.upper()) for i, c in enumerate(word[pos+1:], pos+1))
        if lscore == rscore:
            return "{} {} {} - {}".format(word[:pos], word[pos], word[pos+1:], lscore)
    return "{} DOES NOT BALANCE".format(word)

if __name__ == "__main__":
    print(balance("STEAD"))