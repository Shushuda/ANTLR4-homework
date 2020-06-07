#!/usr/bin/env python3

from knapsLexer import knapsLexer
from knapsParser import knapsParser
from antlr4 import FileStream, CommonTokenStream
import sys


class Item:
    def __init__(self, name, weight, value, dependencies, dep_value):
        self.name = name
        self.weight = weight
        self.value = value
        self.dependencies = dependencies
        self.dep_value = dep_value

    def get_context(self, bag):
        _bag = [item.name for item in bag]
        for dep in self.dependencies:
            if all(item in _bag for item in [dep]):
                return self.dep_value
        return self.value

    def __repr__(self):
        return self.name


class Knapsack:
    def __init__(self, items, _W):
        self.items = items
        self.W = _W

    def get_knapsack(self):
        # brute force method
        if len(self.items) == 0 or self.W == 0:
            return 0
        else:
            x = len(self.items)
            max_subset = {}
            for i in range(1, 1 << x):
                subset = [self.items[j] for j in range(x) if (i & (1 << j))]
                weight = sum([i.weight for i in subset])
                if weight < self.W:
                    _value = 0
                    for item in subset:
                        _value += item.get_context(subset)
                    subset_set = {
                        'items': subset,
                        'value': _value
                    }
                    if not max_subset:
                        max_subset = subset_set
                    else:
                        if subset_set['value'] > max_subset['value']:
                            max_subset = subset_set
            return max_subset


def main(argv):
    char_stream = FileStream(argv)
    lexer = knapsLexer(char_stream)
    tokens = CommonTokenStream(lexer)
    parser = knapsParser(tokens)

    tree = parser.we()

    data = tree.data
    capacity = tree.bag().value

    list_obj = []

    for key, value in data.items():
        list_obj.append(Item(key, value['weight'], value['value'],
                             value['dependencies'], value['dep_value']))

    print("Dane z pliku:")
    print(data)
    print("Pojemnosc plecaka:")
    print(capacity)

    print("--------------")

    knapsack = Knapsack(list_obj, capacity)

    result = knapsack.get_knapsack()

    print("Przedmioty w plecaku:")
    print(result.get('items'))
    print("Wartosc przedmiotow w plecaku:")
    print(result.get('value'))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Podaj plik z danymi.")
        exit(1)
