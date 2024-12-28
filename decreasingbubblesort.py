import random
def sorting(unsorted):
    for i in range(len(unsorted)):
        for j in range(len(unsorted)-1):
            if unsorted[j] < unsorted[j+1]:
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
    return unsorted

x = [int(i) for i in range(1, 25)]
unsorted = []
for i in range(25):
    e = random.choice(x)
    unsorted.append(e)

print(sorting(unsorted))
