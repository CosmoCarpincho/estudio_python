# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

def solution(number):
    r = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            r += i
    return r

print(solution(4))
print(solution(5))
print(solution(9))
        
def solution2(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

print(solution2(4))
print(solution2(5))
print(solution2(9))