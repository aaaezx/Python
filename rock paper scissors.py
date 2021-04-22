import random
computer = random.choice(['가위', '바위', '보'])
user=input('사용자>>')
if user=='가위':
    if computer=='가위':
        print('컴퓨터 >> 가위')
        print('무승부')
    elif computer=='바위':
        print('컴퓨터 >> 바위')
        print('computer 승')
    else:
        print('컴퓨터 >> 보')
        print('user 승')
elif user=='바위':
    if computer=='가위':
        print('컴퓨터 >> 가위')
        print('user 승')
    elif computer=='바위':
        print('컴퓨터 >> 바위')
        print('무승부')
    else:
        print('컴퓨터 >> 보')
        print('computer 승')
elif user=='보':
    if computer=='가위':
        print('컴퓨터 >> 가위')
        print('computer 승')
    elif computer=='바위':
        print('컴퓨터 >> 바위')
        print('user 승')
    else:
        print('컴퓨터 >> 보')
        print('무승부')
