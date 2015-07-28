import re

if __name__ == "__main__":
    with open("input3.txt", "r") as file:
        lines = file.read().splitlines()
    output = []
    pattern = re.compile(r"""(\+-*\+ | \|.*\|)
                          """, re.VERBOSE | re.IGNORECASE)
    p2 = re.compile(r"""\|.*\+-*\+""")
    avglen = max([len(line) for line in lines])
    for line in lines[1:]:
        match = pattern.findall(line)
        if match:
            if line.count('|') % 2 == 0:
                line = pattern.sub('', line)
            else:
                line = p2.sub('', line)
        line = line.strip()
        marked = False
        if line.endswith("-"):
            line = line[:-1]
            marked = True
        if line.endswith("I"):
            line += ' '
        if len(line) < avglen and not marked and not len(line) == 0:
            line += ' '
        output.append(line)
    print(''.join(output))
    #print("This is an example piece of text. This is an example piece of text. This is an example piece of text. This is an example piece of text. This is a sample for a challenge. Lorum ipsum dolor sit amet and other words. The proper word for a layout like this would be typesetting, or so I would imagine, but for now let's carry on calling it an example piece of text. Hold up - the end of the paragraph is approaching - notice the double line break for a paragraph. And so begins the start of the second paragraph but as you can see it's only marginally better than the other one so you've not really gained much - sorry. I am certainly not a budding author as you can see from this example input. Perhaps I need to work on my writing skills.")
    #print("One hundred and fifty quadrillion, seventy-two trillion, six hundred and twenty-six billion, eight hundred and fourty million, three hundred and thirteen thousand subtract one is a rather large prime number which equals one to five if calculated modulo two to six respectively. However, one other rather more interesting number is two hundred and twenty-one quadrillion, eight hundred and six trillion, four hundred and thirty-four billion, five hundred and thirty-seven milmillion, nine hundred and seventy-eight thousand, six hundred and seventy nine, which isn't prime but is the 83rd Lucas number.")
    #print("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex. Duis aute irure dolor in repre-henderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")