vet = [0] * 10

for i in range (10):
    vet[i] = int(input(f"Digite o {i+1}º número: "))
repetidos = []

for i in range(10):
    for j in range(i+1, 10):
        if vet[i] == vet[j] and vet[i] not in repetidos:
            repetidos.append(vet[i])

            if len(repetidos) > 0:
                 print('Os seguintes números se repetem: ')

    for num in repetidos:
        print(f"O número {num} se repete nas posições:", end=" ")
        for i in range(10):
            if vet[i] == num:
                print(i, end=" ")
        print()
else:
        print("Não há números repetidos no vetor.")