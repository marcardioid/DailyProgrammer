def find_stable_marriages(preferences):
    bachelors, bachelorettes, couples = [], [], {}
    for person in preferences.keys():
        bachelors.append(person) if person.isupper() else bachelorettes.append(person)
    while bachelors:
        man = bachelors[0]
        woman = preferences[man].pop(0)
        if woman in bachelorettes:
            bachelorettes.remove(woman)
            bachelors.remove(man)
            couples[woman] = man
        else:
            rival = couples[woman]
            if preferences[woman].index(man) < preferences[woman].index(rival):
                bachelors.append(rival)
                bachelors.remove(man)
                couples[woman] = man
    return couples

if __name__ == "__main__":
    preferences = {}
    with open("input/input2.txt", "r") as file:
        for line in file.read().splitlines():
            person, *options = line.split(', ')
            preferences[person] = options
    for couple in sorted([(v, k) for k, v in find_stable_marriages(preferences).items()]):
        print("({}; {})".format(couple[0], couple[1]))