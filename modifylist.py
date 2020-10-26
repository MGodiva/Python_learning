lst = [10, 5, 8, ]
def modify_list(l):
    lst = []
    for el in l:
        if el % 2 == 0:
            lst.append(el//2)
    l[:] = lst
modifylist(l)
print(l)
modifylist(l)
print(l)
