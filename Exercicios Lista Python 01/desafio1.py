list_notas = []
for i in range(2):
    nota = float(input(f'Digite a {i+1}ª nota do aluno: '))
    list_notas.append(nota)

media = sum(list_notas) / 2

print(f'Média: {media:.2f}')
print('Resultado: Aprovado') if media >= 7 else print('Resultado: Reprovado')
