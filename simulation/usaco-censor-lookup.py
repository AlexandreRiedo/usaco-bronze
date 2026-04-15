import sys

sys.stdin = open("censor.in", "r")
sys.stdout = open("censor.out", "w")

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

censored = ""
for char in s:
    censored += char
    if censored[-len(t) :] == t:
        censored = censored[: -len(t)]

sys.stdout.write(f"{censored}\n")
