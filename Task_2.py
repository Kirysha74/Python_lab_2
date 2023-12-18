import csv


def write_years(filepath: str) -> None:
    """
    splits the original csv file into several files, where each individual file will correspond to one year
    """
    lst = []
    with open(filepath) as file:
        reader = csv.reader(file, delimiter = ",")
        for row in reader:
            lst.append(row)
    year = [lst[0]]
    for row in lst[1:]:
        if year[-1][0][:4] == row[0][:4]:
            year.append(row)
        else:
            with open(year[0][0].replace("-", "") + "_" + year[-1][0].replace("-", "") + ".csv", "w") as file:
                writer = csv.writer(file, delimiter = ",", lineterminator = "\r")
                writer.writerows(year)
            year = [row]

if __name__ == "__main__":
    write_years("dataset.csv")