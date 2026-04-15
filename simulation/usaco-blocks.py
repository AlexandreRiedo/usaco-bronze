import string
import sys
from collections import Counter

sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")

num_boards = int(input())
boards = [tuple(input().split()) for _ in range(num_boards)]

result = Counter({letter: 0 for letter in string.ascii_lowercase})
for i in range(num_boards):
    upside = Counter(boards[i][0])
    downside = Counter(boards[i][1])

    for letter in string.ascii_lowercase:
        result[letter] += max(upside[letter], downside[letter])

    # result.update(upside)

    # for char, count in downside.items():
    #     if char not in upside:
    #         result[char] += count
        # else:
        #     result[char] += max(count, upside[char])

TEST_VALUES = {
    "a": 5,
    "b": 1,
    "c": 3,
    "d": 1,
    "e": 5,
    "f": 0,
    "g": 0,
    "h": 2,
    "i": 3,
    "j": 0,
    "k": 0,
    "l": 3,
    "m": 1,
    "n": 2,
    "o": 1,
    "p": 1,
    "q": 1,
    "r": 3,
    "s": 3,
    "t": 3,
    "u": 1,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 1,
    "z": 0,
}
for letter in string.ascii_lowercase:
    # print(
    #     f"{letter}: {result[letter]} {'BUG: ' + str(TEST_VALUES[letter]) if TEST_VALUES[letter] != result[letter] else ''}"
    # )
    print(result[letter])

"""
(box was before)

dwad
trooxx
"""

# EXPLORATION
"""
3
resilient cascade
telescope ephemeral
labyrinth quasar

resilient   telescope   labyrinth
resilient   telescope   quasar
resilient   ephemeral   labyrinth
resilient   ephemeral   quasar
cascade     telescope   labyrinth    
cascade     telescope   quasar
cascade     ephemeral   labyrinth
cascade     ephemeral   quasar

LINE 1
[('a', 1), ('b', 1), ('c', 1), ('e', 5), ('h', 1), 
('i', 3), ('l', 3), ('n', 2), ('o', 1), ('p', 1), 
('r', 2), ('s', 2), ('t', 3), ('y', 1)]

LINE 8
[('a', 5), ('c', 2), ('d', 1), ('e', 4), ('h', 1), 
('l', 1), ('m', 1), ('p', 1), ('q', 1), 
('r', 2), ('s', 2), ('u', 1)]

# a:5 IS THE BUG AREA!
VALID:
a: 5 
b: 1
c: 3
d: 1
e: 5
f: 0
g: 0
h: 2
i: 3
j: 0
j: 0
l: 3
m: 1
n: 2
o: 1
p: 1
q: 1
r: 3
s: 3
t: 3
u: 1
v: 0
w: 0
x: 0
y: 1
z: 0
"""
