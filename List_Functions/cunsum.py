# Função cumsum que recebe uma lista de números e retorna a soma cumulativa;
# isto é, uma nova lista onde o i-ésimo elemento é a soma dos primeiros i+1 elementos da lista original.

def cunsum(t:list)->list:
    i = 0
    res = 0
    lista_cunsum = []
    for e in t:
        res = res + t[i] 
        i += 1
        lista_cunsum.append(res)
    return lista_cunsum
        
t = [1,2,3]
lista_cunsum = cunsum(t)
print(lista_cunsum)
