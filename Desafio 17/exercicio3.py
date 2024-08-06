# 3. Faça um programa no qual o usuário precisa cadastrar as informações de um produto: código, nome, quantidade e preço. 
# No final o programa deve mostrar as informações cadastradas e exibir o valor total da compra. ]

print("-- Cadastro de Produtos --")
codigo = input("Digite o código do produto: ")
nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))
preco = float(input("Digite o preço unitário do produto: "))

valor_total = quantidade * preco

print("\nInformações do Produto:")
print(f"Código: {codigo}")
print(f"Nome: {nome}")
print(f"Quantidade: {quantidade}")
print(f"Preço unitário: R$ {preco:.2f}")
print(f"Valor total da compra: R$ {valor_total:.2f}")
