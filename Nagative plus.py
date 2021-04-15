def sum_n(n):
    s=0
    for i in range(n, 0):
        s=s+i
    return s

x=int(input(">>"))
print(sum_n(x))
