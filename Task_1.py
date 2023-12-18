import csv 


def write_csv(filepath: str, column_names: list) -> None:
        """
        Divides a CSV file into several files by columns
        """
        with open(filepath) as file:
                lst = []
                reader = csv.reader(file, delimiter = ",")
                for row in reader:
                        lst.append(row)                
                for i in range(len(column_names)):
                        with open(f"{column_names[i]}.csv", "w") as new_file:
                                writer = csv.writer(new_file, delimiter = ",", lineterminator="\r")
                                writer.writerows([[row[i]] for row in lst])


if __name__ == "__main__":
        write_csv("dataset.csv", ["X", "Y"])