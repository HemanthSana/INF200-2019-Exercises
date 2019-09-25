from random import randint as rand

__author__ = 'Hemanth Sana'
__email__ = 'hesa@nmbu.no'


def guess_number():
    num = 0
    while num < 1:
        num = int(input('Your guess: '))
    return num


def random_addition():
    return rand(1, 6) + rand(1, 6)


if __name__ == '__main__':
    chance = 3
    rand_sum = random_addition()
    while chance > 0:
        guessed_number = guess_number()
        if rand_sum != guessed_number:
            print('Wrong, try again!')
            chance -= 1
    if chance > 0:
        print('You won {} points.'.format(chance))
    else:
        print('You lost. Correct answer: {}.'.format(rand_sum))
