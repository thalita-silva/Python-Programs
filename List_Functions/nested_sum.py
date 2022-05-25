# Função chamada nested_sum que recebe uma lista de listas de 
# números inteiros e adiciona os elementos de todas as listas aninhadas.
def nested_sum(t:list)->int:
    soma = 0
    for e in t:
        for j in e:
            soma += j
    return soma
t = [[1,2],[3],[4,5,6]]
res = nested_sum(t)
print(res)