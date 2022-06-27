class FlatIterator:

    def __init__(self, list_lists: list):
        self.list_lists = list_lists
        self.rez = []
        self.item = -1
        for list_1 in self.list_lists:
            self.rez.extend(list_1)

    def __iter__(self):
        return self

    def __next__(self):
        self.item += 1
        if self.item > len(self.rez) - 1:
            raise StopIteration
        return self.rez[self.item]


class FlatIteratorImproved(FlatIterator):

    def __init__(self, list_lists: list):
        self.list_lists = list_lists
        self.rez = list(flat_generator_improved(self.list_lists))
        self.item = -1


def flat_generator(list_lists: list):
    for list_1 in list_lists:
        for list_2 in list_1:
            yield list_2


def flat_generator_improved(list_lists: list):
    for list_1 in list_lists:
        if type(list_1) == list:
            yield from flat_generator_improved(list_1)
        else:
            yield list_1


if __name__ == '__main__':

    # Task 1
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    print("Итератор")
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    # Task2
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]
    print("\nГенератор")
    for item in flat_generator(nested_list):
        print(item)
    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)

    nested_lists = ['a', [1, ['b'], 1], False, ['a', 'b'], [4, 5, ['d', 7]], [['a', 'c'], [11, 12, [[13, 14], None]]]]

    # Task 3
    print("\nИтератор улучшенный")
    for item in FlatIteratorImproved(nested_lists):
        print(item)

    # Task 4
    print("\nГенератор улучшенный")
    for item in flat_generator_improved(nested_lists):
        print(item)
