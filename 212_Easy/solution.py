def encode(sentence):
    sentence_encoded = ""
    for c in sentence:
        if c.lower() in "aeiouåäö" or not c.isalnum():
            sentence_encoded += c
        else:
            sentence_encoded += c + 'o' + c.lower()
    return sentence_encoded

def decode(sentence):
    sentence_decoded = ""
    sentence_iter = iter(sentence)
    for c in sentence_iter:
        if c.lower() in "aeiouåäö" or not c.isalnum():
            sentence_decoded += c
        else:
            try:
                sentence_decoded += c
                next(sentence_iter, None)
                next(sentence_iter, None)
            except StopIteration:
                break
    return sentence_decoded