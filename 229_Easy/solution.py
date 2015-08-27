from math import cos

def dottie(x):
    while not x == cos(x):
        x = cos(x)
    return x

if __name__ == "__main__":
    print(dottie(2))