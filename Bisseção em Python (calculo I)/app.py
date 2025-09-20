from time import sleep

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
    iteracao = 1

    if imagem_a * imagem_b > 0:
        return "Não é possível calcular a raiz dessa função, pelo método da bisseção."
    else:
        media_xk = (a + b) / 2 # media de A e B
        str_f_xk = transformar_funcao(media_xk, FX)
        
        imagem_media_xk = calcular_funcao_str(media_xk, str_f_xk)

        sleep(0.7)
        
        print(f"""
\033[32ma = {a:.8f}\033[m, \033[33mb = {b:.8f}\033[m

\033[1;34mIteração {iteracao}:\033[m intervalo [\033[32m{a}\033[m, \033[33m{b}\033[m]],
\033[35mmedia = {media_xk}\033[m, \033[36mf(media) = {imagem_media_xk}\033[m
Atualizamos o \033[37m{"a" if a == media_xk else "b"} <- {media_xk}\033[m
""")
        imagem_media_xk = imagem_media_xk * -1 if imagem_media_xk < 0 else imagem_media_xk

        while imagem_media_xk > criterio_parada:
            iteracao += 1
            media_xk = (a + b) / 2
            str_f_xk = transformar_funcao(media_xk, FX)
            imagem_media_xk = calcular_funcao_str(media_xk, str_f_xk)

            if imagem_a * imagem_media_xk < 0: # então: os sinais são diferentes
                b = media_xk # logo b <- xk
            elif imagem_b * imagem_media_xk < 0: # então: os sinais são diferentes
                a = media_xk
            sleep(0.4)
            print(f"""
\033[1;34mIteração {iteracao}:\033[m intervalo [\033[32m{a}\033[m, \033[33m{b}\033[m]],
\033[35mmedia = {media_xk}\033[m, \033[36mf(media) = {imagem_media_xk}\033[m
Atualizamos o \033[37m{"a" if a == media_xk else "b"} <- {media_xk}\033[m
""")
            imagem_media_xk = imagem_media_xk * -1 if imagem_media_xk < 0 else imagem_media_xk
        return media_xk

calcular_bissecao(1,2,"x**3-x-2",0.00001)