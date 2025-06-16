# slices
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(numbers[2:10])
print(numbers[-2:])
print(numbers[:-2])

for n in numbers[-5:]:
    print(n)


#4-10
print(f"Primeros 3 elementos: {numbers[:3]}")
print(f"Ultimos 3 elementos: {numbers[-3:]}")
print(numbers)
print(f"3 elementos del medio: {numbers[len(numbers)//2 - 1 : len(numbers)//2 + 2]}")