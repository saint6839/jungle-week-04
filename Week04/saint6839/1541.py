import sys

inputs = sys.stdin.readline().rstrip().split('-')

numbers = []
for input in inputs:
    temp = 0
    positives = input.split('+')
    for p in positives:
        temp += int(p)

    numbers.append(temp)

result = numbers[0]
for i in range(1, len(numbers)):
    result -= numbers[i]

print(result)


