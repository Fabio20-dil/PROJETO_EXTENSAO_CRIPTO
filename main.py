# ==========================================
# PROJETO DE EXTENSÃO: INN SEGUROS
# Algoritmo de Cifra de Blocos Simétrica
# ==========================================


def expandir_chave(chave_string):
    chave = []

    for p in chave_string:
        chave.append(ord(p)) # Pega a chave e adiciona em uma lista. Mas adiciona, por meio da função ord(), o código Unicode da letra
    

    # GERANDO AS CHAVES
    t = 24
    subchave_1 = 0
    for b in chave:
        bits = b << t
        subchave_1 = subchave_1 + bits
        t -= 8

    # GERANDO A DERIVAÇÃO DAS CHAVES
    subchave_2 = ((subchave_1 << 8) | (subchave_1 >> (32-8))) & 0xFFFFFFFF  
    subchavexor1 = subchave_1 ^ subchave_2                                  
    subchave_3 = ((subchave_2 << 8) | (subchave_2 >> (32-8))) & 0xFFFFFFFF  
    subchavexor2 = subchave_2 ^ subchave_3                                  
    subchavexor3 = subchavexor1 ^ subchavexor2                             

    return [subchave_1,subchavexor1,subchavexor3]

def cifrar_bloco(bloco_32bits,subchaves):

    sk1,sk2,sk3 = subchaves

    #RODADA 1
    bloco_32bits = bloco_32bits ^ sk1 #APLICANDO XOR NA CHAVE 
    casas = sk1 % 32 # CALCULA O NUMERO DE CASAS QUE SERÃO MOVIDAS
    bloco_32bits = ((bloco_32bits << casas) | (bloco_32bits >> (32-casas))) & 0xFFFFFFFF #REALIZA A ROTAÇÃO

    #RODADA 2
    bloco_32bits = bloco_32bits ^ sk2
    casas = sk2 % 32
    bloco_32bits = ((bloco_32bits << casas) | (bloco_32bits >> (32-casas))) & 0xFFFFFFFF

    #RODADA 3
    bloco_32bits = bloco_32bits ^sk3
    casas = sk3 % 32
    bloco_32bits = ((bloco_32bits << casas) | (bloco_32bits >> (32-casas))) & 0xFFFFFFFF

    return bloco_32bits

def decifrar_bloco(bloco_cifrado32bits,subchaves):
    sk1,sk2,sk3 = subchaves
    bloco_32bits = bloco_cifrado32bits
    
    #RODADA 3
    casas = sk3 % 32 # CALCULA AS CHAVES
    bloco_32bits = ((bloco_32bits >> casas) | (bloco_32bits << (32-casas))) & 0xFFFFFFFF #DESFAZ A ROTAÇÃO
    bloco_32bits = bloco_32bits ^sk3 # DESFAZ O XOR

    #RODADA 2
    casas = sk2 % 32
    bloco_32bits = ((bloco_32bits >> casas) | (bloco_32bits << (32-casas))) & 0xFFFFFFFF
    bloco_32bits = bloco_32bits ^sk2

    #RODADA 1
    casas = sk1 % 32
    bloco_32bits = ((bloco_32bits >> casas) | (bloco_32bits << (32-casas))) & 0xFFFFFFFF
    bloco_32bits = bloco_32bits ^sk1 

    return bloco_32bits

    


if __name__ == "__main__":
    print("--- Sistema de criptografia INN Seguro ativo ---")
    expandir_chave("CASA")






