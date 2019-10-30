# -*- coding: utf-8 -*-

__author__ = 'Hemanth Sana'
__email__ = 'hesa@nmbu.no'

import random


class Walker:
    def __init__(self, start, home):
        self.start = start
        self.home = home
        self.curr_pos = start
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
        self.start = start
        self.home = home
        random.seed(seed)

    def single_walk(self):
        walker = Walker(self.start, self.home)
        while not walker.is_at_home():
            walker.move()
        return walker.get_steps()

    def run_simulation(self, num_walks):
        return [self.single_walk() for _ in range(num_walks)]


if __name__ == "__main__":
    walks_num = 20
    simulation_1 = Simulation(0, 10, 12345)
    steps_1 = simulation_1.run_simulation(walks_num)
    print(steps_1)
    simulation_2 = Simulation(0, 10, 54321)
    simulation_3 = Simulation(10, 0, 12345)
    simulation_4 = Simulation(10, 0, 54321)


