import simplejson as json

def find(element, search, path=[]):
    if isinstance(element, dict):
        for key in element:
            if type(element[key]) in (dict, list):
                if find(element[key], search):
                    path.append(key)
                    return path
            elif element[key] == search:
                path.append(search)
                return path
    elif isinstance(element, list):
        for item in element:
            if type(item) in (dict, list):
                if find(item, search):
                    path.append(element.index(item))
                    return path
            elif item == search:
                path.append(element.index(search))
                return path

if __name__ == "__main__":
    print(" -> ".join(map(str, find(json.load(open("input/input3.txt", "r")), "dailyprogrammer")[::-1])))