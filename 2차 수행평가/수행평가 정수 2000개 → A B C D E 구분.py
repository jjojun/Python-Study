grades = ['A' if num >= 91 else 'B' if num >= 81 else 'C' if num >= 71 else 'D' if num >= 61 else 'E' for num in range(1, 2001)]

with open('grades.txt', 'w') as file:
    file.write(''.join(grades))
