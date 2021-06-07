def easyCrypto(str):
    tmp=''
    for i in str:
        if ord(i)%2==1:
            tmp += chr(ord(i) + 1)
        else:
            tmp += chr(ord(i) - 1)
    return tmp

s = input('>>')
print(easyCrypto(s))
