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

    # No Transitive Verbs Case
    if not words["transitive-verb"]:
        pass

"""
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

# CALCULATIONS
13nouns + 3conjunctions + 4intransitive + 3transitive = 23

4 intransitive + 8 nouns
"""
