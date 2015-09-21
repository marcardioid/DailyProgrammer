def mangle(sentence):
    words = []
    for word in sentence.split():
        capitals_indices = [word.index(c) for c in word if c.isupper()]
        punctuation_data = [(i, c) for i, c in enumerate(word) if not c.isalnum()]
        for i, c in punctuation_data:
            word = word.replace(c, '')
        word = sorted(word.lower())
        for i, c in punctuation_data:
            word.insert(i, c)
        word = [c.upper() if i in capitals_indices else c for i, c in enumerate(word)]
        words.append("".join(word))
    sentence = " ".join(words)
    return sentence