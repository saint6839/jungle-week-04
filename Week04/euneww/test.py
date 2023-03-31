import sys
n = int(sys.stdin.readline().strip())
cases = list(map(int, [sys.stdin.readline().strip() for _ in range(n)]))
item =[1,2,3]
ls = []
result = []

def func(ls, goal):
    if sum(ls) == goal:
        if ls not in result:
            result.append(ls)
        return
    elif sum(ls) < goal:
        for i in range(len(check)):
            if not check[i] :
                check[i] = True
                func(ls+[item[i%3]], goal)
                check[i] = False

for case in cases:
    check = [0]*case
    func(ls, case)
    print(len(result))
