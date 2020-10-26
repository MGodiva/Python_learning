lst = [10, 5, 8, ]
def modifylist(lst):
    l = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            l.append(int(lst[i]/2))
    lst[:] = l
modifylist(lst)
print(lst)
modifylist(lst)
print(lst)
