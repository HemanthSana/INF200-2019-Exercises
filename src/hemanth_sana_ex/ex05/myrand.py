# -*- coding: utf-8 -*-

__author__ = 'Hemanth Sana'
__email__ = 'hesa@nmbu.no'


class LCGRand:
    slope = 7 ** 5
    congruence_class = 2 ** 31 - 1

    def __init__(self, seed):
        self._hidden_state = seed

    def rand(self):
        self._hidden_state *= self.slope
        self._hidden_state %= self.congruence_class

        return self._hidden_state

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        while True:
            yield self.rand()


class RandIter:
    def __init__(self, random_number_generator, length):
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        if self.num_generated_numbers is not None:
            raise RuntimeError()
        self.num_generated_numbers = 0
        return self

    def __next__(self):
        if self.num_generated_numbers is None:
            raise RuntimeError('Cannot call __next__ before __iter__')
        if self.num_generated_numbers == self.length:
            raise StopIteration

        num_generated = self.generator.rand()
        self.num_generated_numbers += 1
        return num_generated


if __name__ == "__main__":
    random_num_generator = LCGRand(1)
    for rand in random_num_generator.random_sequence(10):
        print(rand)

    for i, rand in enumerate(
            random_num_generator.infinite_random_sequence()):
        print(f'The {i}-th random number is {rand}')
        if i > 100:
            break

