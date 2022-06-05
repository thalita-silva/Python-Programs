# Função que recebe um inteiro k e retorna um novo dicionário 
# cujas chaves são os valores de 1 a k, e os valores sejam o valor da chave ao quadrado.
def novo_dict(k:int)->dict:
    keys = []
    values = []
    for e in range(k):
        keys.append(e+1)
        values.append((e+1) ** 2)
    return dict(zip(keys,values))
    
print(novo_dict(15))