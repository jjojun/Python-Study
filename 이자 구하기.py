monthly_salary = float(input("월급을 입력하세요: "))
saving_rate = float(input("적금 비율을 입력하세요 (소수로): "))
annual_interest_rate = float(input("적금 이율을 입력하세요 (연간 소수로): "))
principal = monthly_salary * saving_rate

for month in range(1, 13):
    monthly_interest = (principal * annual_interest_rate) / 12
    principal += monthly_interest

total_amount = principal
print("12개월 후 총 금액: {:.2f} 원".format(total_amount))
