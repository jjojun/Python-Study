num = int(input("숫자를 입력하세요: "))

is_prime = num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

result = "소수" if is_prime else "소수 아님"
print(result)
