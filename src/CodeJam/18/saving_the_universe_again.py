import sys
import math


# Saving The Universe Again
# Problem
# An alien robot is threatening the universe, using a beam that will destroy all algorithms knowledge. We have to stop it!
#
# Fortunately, we understand how the robot works. It starts off with a beam with a strength of 1, and it will run a program that is a series of instructions, which will be executed one at a time, in left to right order. Each instruction is of one of the following two types:
#


def makeSwap(shield_power, input: str):
    min_dmg = input.count("S")
    if min_dmg > shield_power:
        return "IMPOSSIBLE"

    robot_dmg = 0
    power = 1

    for step in input:
        if step == 'S':
            robot_dmg += power
        else:
            power *= 2

    if robot_dmg <= shield_power:
        return 0

    s_so_far_dmg = 0
    swaps = 0

    # reduce the damage caused by robot in minimum swaps

    for e in reversed(input):
        if e == 'S':
            s_so_far_dmg += 1
        else:
            power //= 2
            tmp = s_so_far_dmg * power
            if robot_dmg - tmp > shield_power:
                swaps += s_so_far_dmg
                robot_dmg -= tmp
            else:
                swaps += abs(-(robot_dmg - shield_power) // power)
                break
    return swaps



if __name__ == '__main__':
    t = int(input())
    for x in range(1, t + 1):
        td, s = input().strip().split()
        answer = makeSwap(int(td), s)
        print('Case #{}: {}'.format(x, answer))