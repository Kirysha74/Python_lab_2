import csv
from datetime import date


def get_value(day_date: date, filepath: str) -> float:
    try:
        if filepath.split("\\")[-1][-5] == "X" or filepath.split("\\")[-1][-5] == "Y":
            index = 0
            with open(filepath[:len(filepath) - 5] + "X.csv") as file:
                reader = csv.reader(file, delimiter = ",")
                for row in reader:
                    dat = row[0].split("-")
                    if (day_date == date(int(dat[0]), int(dat[1]), int(dat[2]))):
                        break
                    index += 1
                else:
                    return None

            with open(filepath[:len(filepath) - 5] + "Y.csv") as file:
                reader = csv.reader(file, delimiter = ",")
                for row in reader:
                    val = row[0]
                    index -= 1
                    if index == -1:
                        print()
                        return float(val)
            return None

        with open(filepath) as file:
            reader = csv.reader(file, delimiter = ",")
            for row in reader:
                dat = row[0].split("-")
                if (day_date == date(int(dat[0]), int(dat[1]), int(dat[2]))):
                    return float(row[1])  
        return None  
    except Exception as ex:
        print(ex)   
        return None 

if __name__ == "__main__":
    dat = date(2023, 10, 3)
    wrong_dat = date(2023, 10, 2)
    print(get_value(dat, "X.csv"))
    print(get_value(dat, "Y.csv"))
    print(get_value(dat, "dataset.csv"))