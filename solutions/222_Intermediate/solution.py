def LCG(seed):
    m, a, c = 32, 1664525, 1013904223
    while True:
        seed = (seed * a + c) % m
        yield seed

def encrypt(plaintext, key):
    rng = LCG(key)
    output = [chr(ord(c) ^ next(rng)) for c in plaintext]
    return "".join(output)

def decrypt(ciphertext, key):
    return encrypt(ciphertext, key)

if __name__ == "__main__":
    message, key = "Attack at dawn", 1337
    ciphertext = encrypt(message, key)
    plaintext = decrypt(ciphertext, key)

    print("Message:\t{}".format(message))
    print("Encrypted:\t{}".format(ciphertext))
    print("Decrypted:\t{}".format(plaintext))