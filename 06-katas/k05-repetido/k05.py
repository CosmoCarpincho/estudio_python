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

print(sum([1,2,3]))
print(sum(x for x in range(4))) # 0 1 2 3

# https://www.codewars.com/kata/54ff3102c1bad923760001f3/python

def get_count(sentence: str) -> int:
    n = 0
    for l in sentence.lower():
        if l in ['a', 'e', 'i', 'o', 'u']:
            n += 1
    return n

print(get_count('aeiou'))


l = 'a'
if l in 'aeiou':
    print('si')
else:
    print('no')

def get_count2(sentence: str) -> int:
    return sum(1 for let in sentence if let in "aeiouAEIOU")

def get_count3(s):
    return sum(c in 'aeiou' for c in s)


# https://www.codewars.com/kata/565b9d6f8139573819000056/python

def decode(message: str):
    a = 'abcdefghijklmnopqrstuvwxyz'
    r = list(reversed(a))
    d = ''

    dic = {}
    for i in range(len(a)):
            dic[a[i]] = r[i]
    
    for m in message.lower():
        if m == ' ':
            d += ' '
        else:
            d += dic[m]
    return d

print(decode('sr'))

def decode2(message):
    a = 'abcdefghijklmnopqrstuvwxyz'
    return message.translate(str.maketrans(a, a[::-1]))

print(decode2('sr'))


