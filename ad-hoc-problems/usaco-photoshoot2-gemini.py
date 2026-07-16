import sys


def solve():
    # Fast I/O: Read all standard input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])
    order = [int(x) for x in input_data[1:N+1]]
    goal = [int(x) for x in input_data[N+1:]]

    swap = 0

    for idx in range(N):
        if order[idx] != goal[idx]:
            # Find the current position of the required element
            target_idx = order.index(goal[idx], idx)
            
            # pop() and insert() shift the memory in-place
            val = order.pop(target_idx)
            order.insert(idx, val)
            
            swap += 1

    print(swap)

if __name__ == '__main__':
    solve()