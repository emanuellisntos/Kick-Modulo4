# 5. Faça um programa que gere as tabuadas do 1 até o 10.

for i in range(1, 11):  # Loop para os números de 1 a 10
    print(f"Tabuada do {i}:")
    for j in range(1, 11):  # Loop para multiplicar de 1 a 10
        print(f"{i} x {j} = {i * j}")
    print()  # Linha em branco para separar as tabuadas
