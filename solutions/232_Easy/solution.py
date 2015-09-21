def is_palindrome(data):
    if isinstance(data, list):
        data = ''.join(c.lower() for c in ''.join(data) if c.isalpha())
    if isinstance(data, str):
        return "Palindrome" if data == data[::-1] else "Not a palindrome"
    else:
        return "Invalid input"

if __name__ == "__main__":
    with open("input/input4.txt", "r") as file:
        num, *lines = file.read().splitlines()
    print(is_palindrome(lines))