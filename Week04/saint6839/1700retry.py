import sys

N, K = map(int, sys.stdin.readline().split())
plugs = list(map(int, sys.stdin.readline().split()))

multitap = []
result = 0
for i in range(K):
    if plugs[i] in multitap:
        continue

    if len(multitap) != N:
        multitap.append(plugs[i])
        continue

    pop_plug = 0
    late_use_index = 0

    for plug in multitap:
        if plug not in plugs[i:]:
            pop_plug = plug
            break
        elif plugs[i:].index(plug) > late_use_index:
            late_use_index = plugs[i:].index(plug)
            pop_plug = plug
    result += 1
    multitap[multitap.index(pop_plug)] = plugs[i]

print(result)
