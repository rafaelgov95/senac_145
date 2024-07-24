from classes import ONG,Projeto
from api_client import api_read



def createOng(token):
    ong = ONG(input("Nome: "))
    projeto = Projeto('salve','todos animais','rafael','andamento')
    ong.adicionar_projeto(projeto)
    print(api_create(ong.to_json(),token))

def getOngs():  
    ongs=[]  
    ongs_json=api_read()
    for index, data in zip(range(len(ongs_json)),ongs_json):
        ong = ONG(_id=data['_id'],nome=data['nome'])
        print(f'{index} : Nome: {data['nome']}')
        for p in data['projetos']:
            projeto = Projeto(p['_id'],p['nome'],p['descricao'],
                              p['responsavel'],p['status'])
            ong.adicionar_projeto(projeto)
            print(f'  Projeto ----> {p['nome']}')
        ongs.append(ong)
        print('\n')
    return ongs