def program(fav, timetable):
    timetable = sorted([show.split(' ', 2) for show in timetable])
    total = 0
    for i, show in enumerate(timetable):
        schedule = [show]
        for next in timetable[i:]:
            if next[0] >= show[1]:
                schedule.append(next)
                show = next
        if len(schedule) > total and fav in [show[2] for show in schedule]:
            total = len(schedule)
            shows = [show[2] for show in schedule]
    return('\n'.join(shows))

if __name__ == "__main__":
    with open("input/input1.txt", "r") as file:
        fav, *timetable = file.read().splitlines()
    print(program(fav, timetable))