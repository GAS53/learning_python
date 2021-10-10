src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

digit_greater = [src[x] for x in range(1, len(src)) if src[x] > src[x - 1]]

print(digit_greater)  # test
