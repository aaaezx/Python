star=input('string>>')

for i in range(0, len(star)):
    for j in range(0, i+1):
        ch = star[j]
        print(ch, end="")
    print()
