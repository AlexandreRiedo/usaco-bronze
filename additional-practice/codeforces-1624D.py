from collections import Counter

for _ in range(int(input())):
    _, k = map(int, input().split())
    string = input()
    p, s = 0, 0

    for count in Counter(string).values():
        p += count // 2
        s += count % 2

    p_per_string = p // k
    s += 2 * (p - (p_per_string * k))

    if s >= k:
        print(p_per_string * 2 + 1)
    else:
        print(p_per_string * 2)

"""
CLAUDE HINT 001

Your premise about simulation is wrong, 
and for a reason that also kills the sorting idea: 
you can swap same-colored letters an unlimited number of times, 
so the positions in s carry zero information. 
Two inputs with the same letter multiset always have the same answer. 
Counter is the whole parsing step, and the algorithm after it is O(26), 
not O(n log n). 
The nLog(n) in the constraints is just slack 
(also the reason binary search is in the tags: 
the answer is monotone, so you can binary search 
"is length L achievable", but you don't need to).

The real hint: stop thinking about strings and think about 
what a palindrome is made of. 
Any palindrome of length L decomposes into exactly L//2 mirrored pairs, 
plus one optional unpaired character sitting in the middle. 
Those are your only two resource types. 
So convert the whole input into resource counts:

P = how many mirrored pairs the letters can supply in total 
(per letter, count // 2)
S = how many letters are left over after that (per letter, count % 2)

Note that letters lose their identity here. 
A pair of a and a pair of z are interchangeable when you're building k 
independent palindromes, since each pair goes entirely inside one string.

Now the questions to answer yourself, in order:

Given P pairs shared across k strings, what length does every string 
reach if you only use pairs? (Even distribution, floor division.)

You'll have P % k pairs left over that can't be given to everyone. 
A leftover pair is not stuck as a pair. What else can you do with it, 
and how does that interact with S?

Under what condition can you add exactly one more character 
to every one of the k strings? And can you ever add two?
"""

"""
10
8 2
bxyaxzay
-> axybyzax
-> axybyax
-> aba xyyx
-> 3
OR
-> 

6 3
aaaaaa
-> aa aa aa
-> 2

6 1
abcdef
-> a/b/c/d/e/f
-> 1

6 6
abcdef
-> a b c d e f
-> 1

3 2
dxd
-> dd x
-> 1

11 2
abcabcabcac
-> abcab cabac c
-> abcba acbca c
-> 5
OR
-> aabaa ccbcc b

6 6
sipkic
-> s i p k i c
-> 1

7 2
eatoohd
-> e oao thd
-> 1

3 1
llw
-> lwl
-> 3

6 2
bfvfbv
-> fbf vbv
-> 3
"""
