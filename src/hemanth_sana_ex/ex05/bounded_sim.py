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


class Simulation:
    def __init__(self, start, home, seed):
        self.current_position = start
        self.home = home
        self.seed = seed

    def single_walk(self):
        walker = Walker(self.current_position, self.home)
        if not walker.is_at_home():
            walker.move()
        return walker.get_steps()

    def run_simulation(self, num_walks):
        return [self.single_walk() for walk in range(num_walks)]


class BoundedWalker:
    def __init__(self, start, home, left_limit, right_limit):
        self.start = start
        self.home = home
        self.left_limit = left_limit
        self.right_limit = right_limit


class BoundedSimulation:
    def __init__(self, start, home, seed, left_limit, right_limit):
        self.start = start
        self.home = home
        random.seed(seed)
        self.left_limit = left_limit
        self.right_limit = right_limit

