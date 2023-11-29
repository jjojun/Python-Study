year = int(input("연도를 입력하세요: "))

result = "윤년" if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else "평년"

print(result)
