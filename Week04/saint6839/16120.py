import sys

inputs = list(sys.stdin.readline().rstrip())

stack = []

counts = {'P':0, 'A':0}

for i in range(len(inputs)):
    counts[inputs[i]] += 1

    if inputs[i] == 'P' and counts['P'] >= 3 and stack[-1] == 'A':
        stack.append(inputs[i])
        for i in range(3):
            popped = stack.pop()
            counts[popped] -= 1
        continue

    stack.append(inputs[i])

popped = stack.pop()
if popped == 'A':
    print('NP')
elif not stack:
    print('PPAP')
else:
    print('NP')


