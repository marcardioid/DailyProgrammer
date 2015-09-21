def order(word):
    return "IN ORDER" if word == ''.join(sorted(word)) else "REVERSE ORDER" if word == ''.join(sorted(word, reverse=True)) else "NOT IN ORDER"

if __name__ == "__main__":
    words = ["almost", "cereal", "billowy", "biopsy", "chinos", "defaced", "chintz", "sponged", "bijoux", "abhors", "fiddle", "begins", "chimps", "wronged"]
    for word in words:
        print("{}\t->\t{}".format(word, order(word)))