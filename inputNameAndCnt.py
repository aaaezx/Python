def names():
    couters={}
    while True:
        name=input('Enter next name : ')
        if name=='':
            break
        else:
            if name in couters:
                couters[name]+=1
            else:
                couters[name]=1
    for i in couters:
        if couters[i]==1:
            print('There is {} student named {}'.format(couters[i], i))
        else:
            print('There are {} student named {}'.format(couters[i], i))

names()
