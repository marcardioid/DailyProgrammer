import re

def decolumnize(lines):
    pattern = re.compile(r"""(\|[^\|]*\+-*\+)|(\+-*\+)|(\|.*\|)""")
    maxlen = max([len(line) for line in lines])
    output = []
    for line in lines[1:]:
        match = pattern.findall(line)
        if match:
            line = pattern.sub('', line)
        line = line.strip()
        eoldash = False
        if line.endswith("-"):
            line = line[:-1]
            eoldash = True
        if 0 < len(line) < maxlen and not eoldash:
            line += ' '
        output.append(line)
    output = ''.join(output)
    output = output.strip()
    return output

if __name__ == "__main__":
    with open("input1.txt", "r") as file:
        lines = file.read().splitlines()
    print(decolumnize(lines))