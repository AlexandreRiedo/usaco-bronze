import re
import sys


def calc_section(section):
    x, y = None, None

    if section[0] == section[-1]:
        if len(section) % 2 == 0:
            x = 1
            y = len(section) - 1
        else:
            x = 0
            y = len(section) - 1
    else:
        if len(section) % 2 == 0:
            x = 0
            y = len(section) - 2
        else:
            x = 1
            y = len(section) - 2

    return (x, y)


def check_incr_in_two(conversation):
    return not (conversation[0] == "F" or conversation[-1] == "F")


def count_edges(conversation):
    if "E" not in conversation and "B" not in conversation:
        return len(conversation) - 1

    start_count = 0
    while conversation[start_count] == "F":
        start_count += 1

    i = len(conversation) - 1
    end_count = 0
    while conversation[i] == "F":
        end_count += 1
        i -= 1

    return start_count + end_count


num_texts = int(sys.stdin.readline().strip())
conversation = sys.stdin.readline().strip()

sections = re.finditer(r"(?=([BE]F*[BE]))", conversation)
total_min = 0
total_max = 0


for section in sections:
    local_min, local_max = calc_section(section.group(1))
    total_min += local_min
    total_max += local_max

incr = 2 if check_incr_in_two(conversation) else 1

total_max += count_edges(conversation)

answers = [i for i in range(total_min, total_max + 1, incr)]

sys.stdout.write(f"{len(answers)}\n")
for answer in answers:
    sys.stdout.write(f"{answer}\n")
