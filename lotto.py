import random

def generate_lotto_numbers():
    return sorted(random.sample(range(1, 46), 6))

def check_lotto_rank(user_numbers, winning_numbers):
    matched_numbers = set(user_numbers) & set(winning_numbers)
    
    if len(matched_numbers) == 6:
        return "1등"
    elif len(matched_numbers) == 5 and 45 in user_numbers:
        return "2등"
    elif len(matched_numbers) == 5:
        return "3등"
    elif len(matched_numbers) == 4:
        return "4등"
    elif len(matched_numbers) == 3:
        return "5등"
    else:
        return "꽝"

def main():
    max_draws = 10
    current_draw = 0
    
    try:
        budget = int(input("로또 구매 금액을 입력하세요: "))
        if budget < 1000:
            print("로또 구매 금액은 최소 1,000원 이상이어야 합니다.")
            return

        winning_numbers = [int(num) for num in input("1등 번호 6개를 입력하세요 (1부터 45까지의 숫자): ").split()]
        
        if len(winning_numbers) != 6 or any(num < 1 or num > 45 for num in winning_numbers):
            print("올바른 1등 번호를 입력하세요.")
            return

        while current_draw < max_draws and budget >= 1000:
            user_numbers = generate_lotto_numbers()
            budget -= 1000
            current_draw += 1
            rank = check_lotto_rank(user_numbers, winning_numbers)
            print(f"로또 번호 {current_draw}: {user_numbers}, {rank} 등")

        print(f"로또 {current_draw}장을 구매했습니다. 남은 금액은 {budget}원 입니다.")
    except ValueError:
        print("올바른 숫자를 입력하세요.")

if __name__ == "__main__":
    main()
