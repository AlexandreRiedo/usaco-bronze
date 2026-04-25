s = input()
perms = []
char_count = [0] * 26


def search(curr: str = ""):
    # we've finished creating a permutation
    if len(curr) == len(s):
        perms.append(curr)
        return
    for i in range(26):
        # For all available characters
        if char_count[i] > 0:
            # Add it to the current string and continue the search
            char_count[i] -= 1
            search(curr + chr(ord("a") + i))
            char_count[i] += 1


for c in s:
    char_count[ord(c) - ord("a")] += 1

search()

print(len(perms))
for perm in perms:
    print(perm)
