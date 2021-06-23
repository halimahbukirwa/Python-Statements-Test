# Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

lst = [num for num in range(1,51) if num % 3 == 0]

print(lst)
