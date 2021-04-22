def indexes(s, f_s):
    lst=[]
    for r in range(len(s)):
        if s[r]==f_s:
            lst.append(r)
    return lst

string=input('str>>')
char=input('find string>>')
print(indexes(string, char))
