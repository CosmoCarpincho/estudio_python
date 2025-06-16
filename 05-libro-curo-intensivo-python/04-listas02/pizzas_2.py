pizzas = ["mozzarela", "anchoas", "napolitana"]

pizzas_amigo = pizzas[:]

pizzas.append("cuatro quesos")

pizzas_amigo.append("con champiñones")

print("Pizzas que me gustan:")
for p in pizzas:
    print(p)

print("\nPizzas que le gustan a mi amigo:")
for p in pizzas_amigo:
    print(p)