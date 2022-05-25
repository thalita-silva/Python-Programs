#Função chamada chop que toma uma lista alterando-a para remover o primeiro e o último elementos, e retorna None
def chop(t:list)->None:
    del t[0]
    t.pop()

t = [1,2,3,4]
chop(t)
print(t)