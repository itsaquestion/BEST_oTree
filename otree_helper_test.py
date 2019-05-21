from otree_helper import *
from typing import List

print(shift([1, 2, 3, 4], 2) == [3, 4, 1, 2])

gs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(gs)
print(shuffle_in_groups(gs))
print(gs)

str_list = ["apple_1", "banana_2", "apple_3", "banana_4"]

str_1 = "apple"
str_2 = "banana"

print(str_list)
print(swap_str(str_list, str_1, str_2))
print(str_list)

print(11 in range(1, 11))

print("\n==========Test shuffle_by_role ================")


class Player:
    _role = ""

    def role(self):
        return self._role

    def __init__(self, i):
        self._i = i


g = [None] * 8
for i in range(0, 8):
    p = Player(i)
    # print(i)
    if (i % 2 == 0):
        p._role = "A"
    else:
        p._role = "B"
    g[i] = p

print("\nOld: ")
for p in g:
    print(p.role(), end=" ")
    print(p._i)

g = shuffle_by_role(g, "B")

print("\nNew:")

for p in g:
    print(p.role(), end=" ")
    print(p._i)


# string

print(', '.join(str(x) for x in [1,2,3]))
print(', '.join(str(x) for x in [1]))