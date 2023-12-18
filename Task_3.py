import csv
from datetime import date


def write_weeks(filepath: str) -> None:
    """
    splits the original csv file into several files, where each individual file will correspond to one week
    """

    with open(filepath) as file:
        lst = []
        reader = csv.reader(file, delimiter = ",")
        for row in reader:
            lst.append(row)
    weeks = []
    past_day = date(int(lst[0][0][:4]), int(lst[0][0][5:7]), int(lst[0][0][8:]))
    for row in lst[1:]:
        day = date(int(row[0][:4]), int(row[0][5:7]), int(row[0][8:]))
        if (day.weekday() < past_day.weekday()):
            weeks.append(row)
            past_day = day 
        else:
                with open(weeks[0][0].replace("-", "") + "_" + weeks[-1][0].replace("-", "") + ".csv", "w") as file:
                    writer = csv.writer(file, delimiter = ",")
                    writer.writerows(weeks)
                weeks = [row]
                past_day = day

if __name__ == "__main__":
    write_weeks("dataset.csv")