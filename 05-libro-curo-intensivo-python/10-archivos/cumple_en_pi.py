from pathlib import Path

file = Path('pi_millon_digits.txt')

pi_string = file.read_text().replace('\n', '').replace(' ', '')

cumple = input("Ingrese su cumpleaños en formato ddmmyyyy: ")

print(pi_string)
if cumple in pi_string:
    print("Si esta tu cumple en el primer millon de decimales de pi")
else:
    print("No esta en el primer millon de decimales de pi")
