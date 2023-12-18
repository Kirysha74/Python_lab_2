import csv


def read_csv(filepath: str) -> list:
    lst = []
    with open("dataset.csv") as file:
        reader = csv.reader(file, delimiter = ",")
        for row in reader:
            lst.append(row)
    return lst

class DataIterator:
    def __init__(self, filepath: str):
        self.lst = read_csv(filepath)
        self.counter = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter < len(self.lst) - 1:
            self.counter += 1
            return tuple(self.lst[self.counter])
        else:
            raise StopIteration
        
if __name__ == "__main__":
    s_iter1 = DataIterator("dataset.csv")

    for val in s_iter1:
        print(val)