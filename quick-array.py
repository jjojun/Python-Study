def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 중간 값을 피벗으로 선택
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# 정렬할 리스트 생성
my_list = [3, 6, 8, 10, 1, 2, 1]

# 퀵 정렬 수행
sorted_list = quick_sort(my_list)

# 결과 출력
print(sorted_list)
