from typing import NamedTuple


class Cow(NamedTuple):
	pos: int
	statement: str
	
n = int(input())
cows = []
for _ in range(n):
	statement, pos = input().split()
	cows.append(Cow(int(pos), statement))
	
cows.sort(key=lambda c: (c.pos, c.statement))

# lying_left[i] stores the number of cows to the left of cow i
# that must be lying given that Bessie is at the position of cow i.
lying_left = [0 for _ in range(n)]
for i in range(1, n):
	# Add up all the cows that are lying to the left of our position.
	lying_left[i] += lying_left[i - 1]

	if cows[i - 1].statement == "L":
		# If the cow before says our position is to the left
		# but their position is strictly less than or equal to our position, they're lying.
		lying_left[i] += 1

# lying_right stores the same thing, but does it so for the cows
# to the *right* of i.
lying_right = [0 for _ in range(n)]
# Fill it up in much the same way.
for i in range(n - 2, -1, -1):
	lying_right[i] += lying_right[i + 1]

	if cows[i + 1].statement == "G":
		lying_right[i] += 1

min_liars = n
for i in range(n):
	min_liars = min(min_liars, lying_left[i] + lying_right[i])

print(min_liars)
