import pathlib
import pickle


class Number:
    def __init__(self, number):
        self.number = number


n = Number(16)

file = pathlib.Path('number.txt')

with file.open('wb') as fd:
    dump = pickle.dump(n, fd)

with file.open('rb') as fd:
    data = pickle.load(fd)
    print(data.number)
