def binarytoascii(binary):
    output = []
    for i in range(0, len(binary), 8):
        digits = binary[i:i+8]
        num = int(digits, 2)
        char = chr(num)
        output.append(char)
    return ''.join(output)

if __name__ == "__main__":
    with open("input/input1.txt", "r") as file:
        input = file.read().replace('\n', '')
    print(binarytoascii(input))