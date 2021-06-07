alpha='abcdefghijklmnopqrstuvwxyz'
def hexASCII():
    for i in alpha:
        print('{:2}:{:2x}'.format(i, ord(i)), end=' ')
        if i=='m':
            print()

hexASCII()
