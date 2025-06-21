from pathlib import Path

file = Path('./pi_millon_digits.txt')

#1
contents = file.read_text().replace('\n', '').replace(' ', '')
print(contents)

#2
contents_2 = file.read_text()
lines = contents_2.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)