import itertools
from typing import NamedTuple


class Configuration(NamedTuple):
    W: int
    t1: int
    t2: int
    J: int
    M: int


num_tests = int(input())

for _ in range(num_tests):
    num_words, num_commas, num_periods = map(int, input().split())

    words = {
        "noun": [],
        "transitive-verb": [],
        "intransitive-verb": [],
        "conjunction": [],
    }
    for _ in range(num_words):
        word, type = input().split()
        words[type].append(word)

    configurations = [Configuration(0, 0, 0, 0, 0)]
    for t1 in range(len(words["intransitive-verb"]) + 1):
        for t2 in range(len(words["transitive-verb"]) + 1):
            if t1 == 0 and t2 == 0:
                continue

            if not (t1 + 2 * t2 <= len(words["noun"])):
                break

            J = min(len(words["conjunction"]), (t1 + t2) // 2)
            if not ((t1 + t2) - J <= num_periods):
                break

            if t2 > 0:
                M = min(len(words["noun"]) - (t1 + 2 * t2), num_commas)
            else:
                M = 0

            W = 2 * t1 + 3 * t2 + J + M

            configurations.append(Configuration(W, t1, t2, J, M))

    best_configuration = max(configurations)
    W, t1, t2, J, M = best_configuration

    intrans_phrases = []
    for i in range(t1):
        intrans_phrase = []
        intrans_phrase.append(words["noun"].pop() + " ")
        intrans_phrase.append(words["intransitive-verb"].pop())

        intrans_phrases.append(intrans_phrase)

    trans_phrases = []
    for i in range(t2):
        trans_phrase = []
        trans_phrase.append(words["noun"].pop() + " ")
        trans_phrase.append(words["transitive-verb"].pop() + " ")
        trans_phrase.append(words["noun"].pop())

        if i == t2 - 1:
            for _ in range(M):
                trans_phrase.append(", ")
                trans_phrase.append(words["noun"].pop())

        trans_phrases.append(trans_phrase)

    sentence = []
    idx = 0
    for trans_phrase in trans_phrases:
        sentence.append(trans_phrase)
        if J > 0 and idx % 2 == 0:
            sentence.append(" " + words["conjunction"].pop() + " ")
            J -= 1
        else:
            sentence.append(". ")

        idx += 1

    for intrans_phrase in intrans_phrases:
        sentence.append(intrans_phrase)
        if J > 0 and idx % 2 == 0:
            sentence.append(" " + words["conjunction"].pop() + " ")
            J -= 1
        else:
            sentence.append(". ")

        idx += 1

    print(W)
    print("".join(itertools.chain.from_iterable(sentence)).strip())
