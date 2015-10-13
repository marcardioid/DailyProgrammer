import random

def piece_generator(pieces):
    pieces = list(pieces) if not isinstance(pieces, list) else pieces
    bag = pieces[:]
    while True:
        piece = random.choice(bag)
        bag.remove(piece)
        yield piece
        if len(bag) == 0:
            bag = pieces[:]

if __name__ == "__main__":
    pieces = piece_generator("OISZLJT")
    print(''.join(next(pieces) for _ in range(50)))
    pieces.close()