# contar hasta 20
for n in range(1,21):
    print(n)

# lista de un millon
un_millon = [n for n in range(1,1_000_001)]
for n in un_millon:
    print(n)

print(f"min: {min(un_millon)}")
print(f"max: {max(un_millon)}")
print(f"{sum(un_millon)}")