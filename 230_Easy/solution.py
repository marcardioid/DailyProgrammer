import simplejson as json

def find(element, search, path=[]):
    for key, value in element.items() if isinstance(element, dict) else enumerate(element):
        if isinstance(value, (dict, list)):
            if find(value, search, path):
                path.append(key)
                return path
        elif value == search:
            path.append(key)
            return path

if __name__ == "__main__":
    with open("input/input3.txt", "r") as file:
        print(" -> ".join(map(str, find(json.load(file), "dailyprogrammer")[::-1])))