# -*- coding: utf-8 -*-

__author__ = 'Hemanth Sana'
__email__ = 'hesa@nmbu.no'


from walker_sim import Walker, Simulation


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        super().__init__(start, home)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def bounded_move(self):
        super().move()
        if self.curr_pos < self.left_limit:
            self.curr_pos = self.left_limit
        elif self.curr_pos > self.right_limit:
            self.curr_pos = self.right_limit


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        super().__init__(start, home, seed)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def single_walk(self):
        walker = BoundedWalker(self.start, self.home,
                               self.left_limit, self.right_limit)
        num_steps = 0
        while not walker.is_at_home():
            walker.bounded_move()
            num_steps += 1
        return num_steps


if __name__ == "__main__":
    for left_boundary in [0, -10, -100, -1000, -10000]:
        steps = BoundedSimulation(0, 20, 1,
                                  left_boundary, 20).run_simulation(20)
        print('Left Boundary: {:8d} : {}'.format(left_boundary, steps))
