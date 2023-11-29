import random

numbers = [random.randint(1, 1000) for _ in range(500)]
sum_of_multiples_of_3 = sum(x for x in numbers if x % 3 == 0)
sum_of_multiples_of_7 = sum(x for x in numbers if x % 7 == 0)

print("3의 배수의 합:", sum_of_multiples_of_3)
print("7의 배수의 합:", sum_of_multiples_of_7)
