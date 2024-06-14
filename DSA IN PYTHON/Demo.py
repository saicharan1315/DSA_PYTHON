def fun(l, i):
    if (i == len(l) // 2):
        return l
    l[i], l[-1 - i] = l[-1 - i], l[i]
    return fun(l, i + 1)

k=[10,11,16,13,17,20,19]
print(fun(k, i=0))