def date_to_iso_8601(date):
    date = date.replace('/', ' ').replace('-', ' ')
    if all([1 if d.isnumeric() else 0 for d in date[0:4]]):
        return date[0:4] + '-' + date[5:7].strip().zfill(2) + '-' + date[7:10].strip().zfill(2)
    else:
        return (date[5:] if len(date[6:]) > 2 else "20" + date[5:]) + '-' + date[0:2].strip().zfill(2) + '-' + date[2:5].strip().zfill(2)

if __name__ == "__main__":
    inputs = ["2/13/15", "1-31-10", "5 10 2015", "2012 3 17", "2001-01-01", "2008/01/07"]
    for date in inputs:
        print("{} => {}".format(date, date_to_iso_8601(date)))