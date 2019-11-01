# -*- coding: utf-8 -*-

__author__ = 'Hemanth Sana'
__email__ = 'hesa@nmbu.no'

import random


class Walker:
    def __init__(self, start, home):
        self.start = start
        self.home = home
        self.curr_pos = 0
        self.steps = 0

    def move(self):
        rand_gen = random.randint(0, 1)
        if rand_gen == 1:
            self.curr_pos += 1
        else:
            self.curr_pos -= 1
        self.steps += 1

    def is_at_home(self):
        return self.curr_pos == self.home

    def get_position(self):
        return self.curr_pos

    def get_steps(self):
        return self.steps

    def walking_process(self):
        while not self.is_at_home():
            self.move()


if __name__ == "__main__":
    for distance in [1, 2, 5, 10, 20, 50, 100]:
        path_length = []
        for i in range(5):
            walker = Walker(0, distance)
            walker.walking_process()
            path_length.append(walker.get_steps())
        print("Distance: ", distance, "->  Path lengths:", path_length, )
