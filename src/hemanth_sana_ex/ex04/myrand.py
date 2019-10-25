# -*- coding: utf-8 -*-

__author__ = 'Hemanth Sana'
__email__ = 'hesa@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed

    def rand(self):
        a = 16807
        m = 2 ** 31 - 1
        self.seed = a * self.seed % m
        return self.seed


class ListRand:
    def __init__(self, number_list):
        self.number_list = number_list
        self.index = -1

    def rand(self):
        self.index += 1
        if self.index < len(self.number_list):
            return self.number_list[self.index]
        else:
            raise RuntimeError()


if __name__ == "__main__":
    pass