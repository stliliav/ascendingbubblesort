x = []
flag = 1
while flag!=0:
    s = input('Input the stroke. Press 0 to stop\n')
    x.append(s)
    if s == '0':
        flag = 0
print(x)
def sorting(unsorted):
    for i in range(len(unsorted)):
        for j in range(len(unsorted)-1):
            if len(unsorted[j]) > len(unsorted[j+1]):
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
    return unsorted
print(sorting(x))
