def transformar_funcao(var, func: str):
    var = str(var)
    func = func.replace('x', var)
    return func

def calcular_funcao_str(x: float, f_x: str):
    def calcular_str_como_expressao(x= x, f_x= f_x):
        f_x = eval(f_x)
        return f_x
    
    f_x = calcular_str_como_expressao()
    return f_x

def calcular_bissecao(a: float,
                      b: float,
                      FX: str,
                      criterio_parada: float):
    """Calcula a bisseção da função baseado no intervalo do ponto a ao ponto b
    A multiplicação dos 2 tem de resultar em um número negativo

    Args:
        a (float): Ponto a
        b (float): Ponto b
        criterio_parada (float): Criterio de parada para comparação da imagem da media
    """
    ax = str(a) # transformando o x em a
    bx = str(b)
    str_f_a = transformar_funcao(ax, FX) # str(fx) # criando uma função para transformar x em a
    str_f_b = transformar_funcao(bx, FX)
    imagem_a = calcular_funcao_str(ax, str_f_a) # float(f_a)
    imagem_b = calcular_funcao_str(bx, str_f_b) # float(f_b)

    if imagem_a * imagem_b > 0:
        return "Não é possível calcular a raiz dessa função, pelo método da bisseção."
    else:
        media_xk = (a + b) / 2 # media de A e B
        str_f_xk = transformar_funcao(media_xk, FX)
        
        imagem_media_xk = calcular_funcao_str(media_xk, str_f_xk)

        while imagem_media_xk < criterio_parada:
            media_xk = (a + b) / 2
            str_f_xk = transformar_funcao(media_xk, FX)
            imagem_media_xk = calcular_funcao_str(media_xk, str_f_xk)

            if imagem_a * imagem_media_xk < 0: # então: os sinais são diferentes
                b = media_xk # logo b <- xk
            elif imagem_b * imagem_media_xk < 0: # então: os sinais são diferentes
                a = media_xk
            print(f"[{a}, {b}]")
        return media_xk
