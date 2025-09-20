from app import calcular_bissecao

def main():
    a = float(input('Digite o primeiro ponto do intervalo: '))
    b = float(input('Digite o segundo ponto do intervalo: '))
    precisao = float(input("Qual será o critério de parada em um número decimal: ").replace(',','.'))
    f_x = input('Qual vai ser sua função (Se quiser ver o guia de operadores digite guia): ').lower().strip()
    if f_x == 'guia':
        print('''
[+]  = Soma
[-]  = Subtração
[*]  = Multiplicação
[/]  = Divisão
[//] = Divisão Inteira
[%]  = Módulo (Resto da divisão)
[**] = Exponenciação
[()] = Ordem de Precedência
[x]  = Variavel de uso obrigatório
''')
        f_x = input('Agora digite a sua função baseado nesses operadores e sem o f(x) (Apenas a expressão): ')
    bissecao = calcular_bissecao(a, b, f_x, precisao)
    return bissecao

if __name__ == '__main__':
    print(main())
