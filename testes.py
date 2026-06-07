def tratar_padding(dados_texto):
    #IDENTIFICANDO SE A ENTRADA É MULTIPLO DE 4(32 BITS), E CASO NÃO, IDENTIFICANDO QUANTO FALTA

    tam_bloco = 4
    sobra = len(dados_texto) % tam_bloco
    quantos_faltam  = 0 if sobra == 0  else tam_bloco - sobra

    #PREENCHENDO OS BYTES RESTANTES
    txt = chr(quantos_faltam) 
    padding = txt * quantos_faltam
    texto_final = dados_texto
    texto_final = dados_texto + padding
    print(len(texto_final))

    return texto_final
   
def remover_padding(texto_final):
    print(len(texto_final))


TEXTO = tratar_padding('CARROE')
