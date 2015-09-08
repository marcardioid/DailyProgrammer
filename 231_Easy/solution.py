def simulate(generation, lifetime):
    gen_curr = [0] + [int(x) for x in generation] + [0]
    for i in range(lifetime+1):
        print(''.join(['X' if n == 1 else ' ' for n in gen_curr[1:-1]]))
        gen_next = [gen_curr[i-1] ^ gen_curr[i+1] for i in range(1, len(gen_curr)-1)]
        gen_curr = [0] + gen_next + [0]
        if all(n == 0 for n in gen_curr):
            break

if __name__ == "__main__":
    for generation in ["1101010", "00000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000"]:
        simulate(generation, 25)