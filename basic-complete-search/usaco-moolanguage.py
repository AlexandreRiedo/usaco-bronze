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
    num_sentences = num_periods + min(len(words["conjunction"]), num_periods)
    # rprint(f"{words=}")
    # rprint(f"{num_commas=} {num_periods=} {num_sentences=}")
    # rprint("")

    sentences = []
    word_count = 0
    while True:
        # Verify Breaking
        if not words["noun"]:
            # rprint("Broke at noun == 0")
            break
        if not words["intransitive-verb"] and (
            len(words["noun"]) <= 1 and len(words["transitive-verb"]) <= 1
        ):
            # rprint("Broke at the 2nd verb conditions")
            break
        if num_sentences == 0:
            # rprint("Broke at num_sentences == 0")
            break

        # Build transitive sentences
        if words["noun"] and words["transitive-verb"]:
            if sentences and sentences[-1] != ". ":
                if len(words["transitive-verb"]) == 1:
                    sentences.append(words["noun"].pop() + " ")
                    sentences.append(words["transitive-verb"].pop() + " ")
                    sentences.append(words["noun"].pop())
                    word_count += 3
                    while len(words["noun"]) + 1 > len(words["intransitive-verb"]):
                        sentences.append(", ")
                        sentences.append(words["noun"].pop())
                        word_count += 1
                    sentences.append(". ")
                    num_sentences -= 1
                else:
                    sentences.append(words["noun"].pop() + " ")
                    sentences.append(words["transitive-verb"].pop() + " ")
                    sentences.append(words["noun"].pop())
                    sentences.append(". ")
                    word_count += 3
                    num_sentences -= 1
            elif words["conjunction"] and len(words["noun"]) > 1:
                if len(words["transitive-verb"]) == 1:
                    sentences.append(words["noun"].pop() + " ")
                    sentences.append(words["transitive-verb"].pop() + " ")
                    sentences.append(words["noun"].pop())
                    word_count += 3
                    while len(words["noun"]) + 1 > len(words["intransitive-verb"]):
                        sentences.append(", ")
                        sentences.append(words["noun"].pop())
                        word_count += 1
                    sentences.append(" " + words["conjunction"].pop() + " ")
                    word_count += 1
                    num_sentences -= 1
                else:
                    sentences.append(words["noun"].pop() + " ")
                    sentences.append(words["transitive-verb"].pop() + " ")
                    sentences.append(words["noun"].pop() + " ")
                    sentences.append(words["conjunction"].pop() + " ")
                    word_count += 4
                    num_sentences -= 1
            else:
                if len(words["transitive-verb"]) == 1:
                    sentences.append(words["noun"].pop() + " ")
                    sentences.append(words["transitive-verb"].pop() + " ")
                    sentences.append(words["noun"].pop())
                    word_count += 3
                    while len(words["noun"]) + 1 > len(words["intransitive-verb"]):
                        sentences.append(", ")
                        sentences.append(words["noun"].pop())
                        word_count += 1
                    sentences.append(". ")
                    num_sentences -= 1
                else:
                    sentences.append(words["noun"].pop() + " ")
                    sentences.append(words["transitive-verb"].pop() + " ")
                    sentences.append(words["noun"].pop())
                    sentences.append(". ")
                    word_count += 3
                    num_sentences -= 1

        # Build intransitive sentences
        elif len(words["noun"]) <= len(words["intransitive-verb"]):
            if sentences and sentences[-1] != ". ":
                sentences.append(words["noun"].pop() + " ")
                sentences.append(words["intransitive-verb"].pop())
                sentences.append(". ")
                num_sentences -= 1
                word_count += 2
            elif words["conjunction"] and len(words["noun"]) > 1:
                sentences.append(words["noun"].pop() + " ")
                sentences.append(words["intransitive-verb"].pop() + " ")
                sentences.append(words["conjunction"].pop() + " ")
                num_sentences -= 1
                word_count += 3
            else:
                sentences.append(words["noun"].pop() + " ")
                sentences.append(words["intransitive-verb"].pop())
                sentences.append(". ")
                num_sentences -= 1
                word_count += 2

        # rprint("".join(sentences))

    print(word_count)
    print("".join(sentences).strip())
    # rprint("")


"""
# IDEA
- Build the biggest possible phrases first 
    (trans + use commas + conjunction + trans)
- num_sentences = num_periods + num_conjunctions

- Use up conjunctions as soon as possible.

- If num_nouns <= num_intrans <= num_sentences, then you must use up intransitive
- Else use transitive verbs
- Use up commas for the last transitive verb whilst num_noun > num_intrans.

# TEST REORGANIZATION
24 5 4
and conjunction
and conjunction
but conjunction

flew intransitive-verb
leaped intransitive-verb
mooed intransitive-verb
mooed intransitive-verb

impressed transitive-verb
impressed transitive-verb
pushed transitive-verb
taught transitive-verb # NOT USED!

bessie noun
bella noun
bob noun
buttercup noun
cow noun
elsie noun
elsie noun
envy noun
farmer noun
john noun
john noun
nhoj noun
nhoj noun


bella pushed elsie and buttercup flew. 
cow impressed bob and nhoj impressed john, farmer, elsie, bessie. 
envy mooed but john leaped.
nhoj mooed. 


# INFO
5 commas, 4 periods
7 sentences

13 nouns
3 conjunctions
4 transitive-verbs
4 intransitive-verbs

1 intrans sentence
1 trans combo + 1 trans
1 trans + 1 intrans
1 intrans + 1 intrans

4 intrans
3 trans


# EXPLORATION
    nouns left: 13
    sentences left: 7
nhoj impressed john, farmer, elsie, bessie and cow impressed bob.
    nouns left: 6
    sentences left: 5
bella pushed elsie and buttercup flew. 
    nouns left: 3
envy mooed but john leaped.
    nouns left: 1
nhoj mooed. 
    nouns left: 0
"""
