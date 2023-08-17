# sum to get the square of each element in a list using loop
nambari = (3, 5, 8, 1, 9, 12, 34, 22)

sum = 0

for num in nambari:
    sum = sum + num ** 2
    print("The square is", sum)
