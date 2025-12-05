#1---
temperatura = float(input('Digite a temperatura em Celsius (Ex.: 23.7): '))
if temperatura < 15:
    print("Temperatura Baixa - Ligar Aquecedor")
elif temperatura >= 15 and temperatura >= 30:
    print("Temperatura Ideal - Sistema em Espera")
elif temperatura > 30:
    print("Temperatura Alta - Ligar Exaustores")
else:
    print('Temperatura não aceita.')

#2---
correntes = [0.5, 1.2, 0.8, 1.5, 0.6, 1.1, 0.9, 1.3]
soma = 0
for valor in correntes:
    soma += valor 

media = soma/len(correntes)
print(f'\nMédia das correntes: {media:.2f} A')

contador = 0 
for valor in correntes:
    if valor > 1.0:
        contador += 1

print(f'Leituras acima de 1.0 A: {contador}')

#3===
while True:
    try:
        numero = int(input('\nDigite um número inteiro positivo: '))
        if numero > 0:
            break
        else:
            print('erro: você deve digitar um número positivo!')
    except ValueError :
        print('Erro: você deve digitar um número inteiro!')

print(f'Tabuada do número {numero}:')
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")

#4---
M = [
    [2,5,1],
    [3,4,2],
    [1,6,3]
]
soma_total = 0
for linha in M:
    for elemento in linha:
        soma_total += elemento

print(f'Soma total dos elementos:{soma_total}')

#5---
notas = []
while True:
    print('\n||| MENU |||')
    print('1-Incerir nova nota')
    print('2-Ver notas lançadas')
    print('3-Calcular mádia final')
    print('0-Sair')
    op = int(input('Escolha uma opção: '))

    if op == 1:
        nota = float(input('Digite a nova nota: '))
        notas.append(nota)
        print('Noata adicionada com sucesso!')
    
    elif op == 2:
        if len(notas) == 0:
            print('Nenhuma nota foi lançada ainda.')
        else:
            print(f'Notas lançadas: {notas}')
    
    elif op == 3:
        if len(notas) == 0:
            print('não há notas para calcular a média.')
        else:
            med = sum(notas) / len(notas)
            print(f'Média final: {med:.2f}')
    
    elif op == 0:
        print('Programa encerrado.')
        break
    
    else:
        print('Opção inválida! Digite uma opção exitente(Ex.:1,2,3,0).')