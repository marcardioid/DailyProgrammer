def decode(message, key):
    dictionary = dict(zip(key.split()[1::2], key.split()[::2]))
    decoded = ""
    word = ""
    for char in message:
        if char in "gG":
            word += char
            if word in dictionary:
                decoded += dictionary[word]
                word = ""
        else:
            decoded += char
    return decoded

def encode(message, keys):
    dictionary = dict(zip(key.split()[::2], key.split()[1::2]))
    encoded = ""
    for char in message:
        if char in dictionary:
            encoded += dictionary[char]
        else:
            encoded += char
    return encoded

if __name__ == "__main__":
    with open("inputs/input1.txt", "r") as file:
        key, message = file.read().splitlines()
    print(decode(message, key))
    print(encode("Hello, world!", key))
    print(decode(encode(message, key), key))