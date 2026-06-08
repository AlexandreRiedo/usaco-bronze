num_texts = int(input())
conversation = list(input())


def count_score(conversation):
    score = 0
    for a, b in zip(range(len(conversation)), range(1, len(conversation))):
        char_a, char_b = conversation[a], conversation[b]
        if char_a == char_b and char_a != "F":  # guard
            score += 1
    return score


def rec_wrapper(conversation):
    scores = set()

    def rec(conversation, idx):
        if idx == len(conversation):
            scores.add(count_score(conversation))
            # rprint(f"Explored with score {count_score(conversation)}: {"".join(conversation)}")
        else:
            if conversation[idx] != "F":
                rec(conversation, idx + 1)
            else:
                conversation[idx] = "B"
                rec(conversation, idx + 1)
                conversation[idx] = "E"
                rec(conversation, idx + 1)
                conversation[idx] = "F"

    idx = 0
    rec(conversation, idx)

    return list(sorted(scores))


solutions = rec_wrapper(conversation)
print(len(solutions))
for ans in solutions:
    print(ans)
