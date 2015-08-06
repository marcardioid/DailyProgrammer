def binarytoascii(binary):
    return ''.join([chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)])

if __name__ == "__main__":
    with open("input/input1.txt", "r") as file:
        input = file.read().replace('\n', '')
    print(binarytoascii(input))