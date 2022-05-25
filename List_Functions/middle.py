# Função middle que recebe uma lista e retorna uma 
# nova lista com todos os elementos originais, exceto o primeiro e o último elementos
def middle(t:list)->list:
    lista_res = []
    for e in range(1,len(t)-1):
        lista_res.append(t[e])
    return lista_res

t = [1,2,5,7,3,4]
t_res = middle(t)
print(t_res)