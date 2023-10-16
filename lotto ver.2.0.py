import random

def generate_lotto_numbers():
    return sorted(random.sample(range(1, 46), 6))

def generate_winning_numbers():
    return sorted(random.sample(range(1, 46), 6))

def check_lotto_rank(user_numbers, winning_numbers):
    matched_numbers = set(user_numbers) & set(winning_numbers)
    
    rank_dict = {
        6: "1등",
        5: "3등",
        4: "4등",
        3: "5등",
    }
    
    rank = rank_dict.get(len(matched_numbers), "꽝")
    return rank, len(matched_numbers)

def main():
    max_draws = 10
    current_draw = 0
    
    try:
        budget = int(input("로또 구매 금액을 입력하세요: "))
        if budget < 1000:
            print("로또 구매 금액은 최소 1,000원 이상이어야 합니다.")
            return

        winning_numbers = generate_winning_numbers()
        print(f"1등 번호: {winning_numbers}")
        
        while current_draw < max_draws and budget >= 1000:
            user_numbers = generate_lotto_numbers()
            budget -= 1000
            current_draw += 1
            rank, matched_numbers_count = check_lotto_rank(user_numbers, winning_numbers)
            print(f"로또 번호 {current_draw}: {user_numbers}, {rank}, 당첨 개수: {matched_numbers_count}")

        print(f"로또 {current_draw}장을 구매했습니다. 남은 금액은 {budget}원 입니다.")
    except ValueError:
        print("올바른 숫자를 입력하세요.")

if __name__ == "__main__":
    main()
