import csv 
import os


def write_csv(filename: str, dir_name: str, column_names: list) -> None:
        """
        Divides a CSV file into several files by columns
        """
        with open(f"{filename}.csv") as file:
                lst = []
                reader = csv.reader(file, delimiter = ";")
                for row in reader:
                        lst.append(row)

                try:
                        os.mkdir(dir_name)
                except:
                        pass
                
                for i in range(len(column_names)):
                        with open(f"{dir_name}\{column_names[i]}.csv", "w") as new_file:
                                writer = csv.writer(new_file, delimiter = ";", lineterminator="\r")
                                writer.writerows([[row[i]] for row in lst])


if __name__ == "__main__":
        write_csv("dataset", "task_1", ["X", "Y"])