from classes import *



# def create_ong(token):
#     ong = ONG('salve os bichos')
#     projeto = Projeto('salve','todos animais','rafael','andamento')
#     ong.adicionar_projeto(projeto)
#     print(api_create(ong.to_json(),token))

def view_projetos(projetos:list[Projeto]):
    for index,p in zip(range(len(projetos)),projetos):
        print(f'[{index}]: {p.nome}')
    

def view_ongs(ongs:list[ONG]):    
    for index, ong in zip(range(len(ongs)),ongs):
        print(f'{index} : Nome: {ong.nome}')
        for p in ong.getProjetos():
            print(f'  Projeto ----> {p.nome}')
        print('\n')
    
    