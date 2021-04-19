def test(n):
    if n<0:
        print('Negative')
    elif n==0:
        print('Zero')
    else:
        print('Positive')

num=int(input('>>'))
test(num)
