import sys

sys.stdin = open("censor.in", "r")
sys.stdout = open("censor.out", "w")

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()


while True:
    prev = s
    s = s.replace(t, "", 1)
    if len(prev) == len(s):
        break

sys.stdout.write(f"{s}\n")
