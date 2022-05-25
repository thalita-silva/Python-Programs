# Função chamada is_sorted que toma uma lista como parâmetro e retorna True, se a lista estiver classificada em ordem ascendente,  
# e False se não for o caso
def is_sorted(t:list)->bool:
    if sorted(t) == t:
        return True
    else:
        return False
print(is_sorted([2,2,3]))
print(is_sorted(['b','a']))
