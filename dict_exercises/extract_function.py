# Função chamada extract que recebe um dicionário e uma lista 
# como parâmetro. A função deve retornar um novo dicionário que extraia os 
# elementos do dicionário original usando os elementos da lista como chaves a extrair.
def extract(lista_extrair:list,dict_extrair:dict)->dict:
    list_values = []
    list_values.append(dict_extrair.get("name"))
    list_values.append(dict_extrair.get("salary"))
    novo_dict = dict(zip(lista_extrair,list_values))
    return novo_dict
sample_dict = {"name":"Kelly","age":25,"salary":8000,"city":"New York"}
keys = ["name","salary"]
print(extract(keys,sample_dict))