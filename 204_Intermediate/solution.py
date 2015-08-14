def hypbin(num):
    results = set()
    def add_hypbins(n, output, m):
        if n == 0:
            results.add(int(output))
            return
        elif n % (m*2) == 0:
            add_hypbins(n-m*2, '2'+output, m*2)
            add_hypbins(n, '0'+output, m*2)
        else:
            add_hypbins(n-m, '1'+output, m*2)
    add_hypbins(num, '', 1)
    return results

if __name__ == "__main__":
    for input in [18, 73, 128, 239]:
        print("BINARY {} \t-> \tHYPERBINARY {}".format(input, hypbin(input)))
    print("BINARY {} \t-> \t{} HYPERBINARY POSSIBILITIES".format(input, len(hypbin(12345678910))))