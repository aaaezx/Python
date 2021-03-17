number = 10313

year = number // 10000
month = (number % 10000) // 100
day = number % 100

print("주민번호 = 0"+str(number))

print("생년월일 = 200"+str(year)+"년 "+str(month)+"월"+str(day)+"일")
