# Dadas duas listas, converta-as em um dicionário de tal forma que os itens da primeira lista sejam chaves e os 
# itens da segunda lista sejam valores do dicionário, na mesma ordem.
keys = ['Ten','Twenty','Thirty']
values = [10,20,30]
dic = dict(zip(keys,values))
print(dic)