from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

class Produto(BaseModel):
    codigo: int
    nome: str
    descricao :str
    preco:float
    restricao:str
class Preco(BaseModel):
    preco:float

app = FastAPI()
item = {0: {'codigo': 0, 'nome': 'Batata Frita','descricao': 'Batata Frita', 'preco': 10.90, 'restricao': 'vegano'},
        1: {'codigo': 1, 'nome': 'X-Burguer', 'descricao': 'Hambúrguer com Queijo', 'preco': 15.90, 'restricao': 'padrao'},
        2: {'codigo': 2, 'nome': 'X-salada', 'descricao': 'salada mista', 'preco': 35.90, 'restricao': 'vegetariano'},
        3: {'codigo': 3, 'nome': 'X-Bacon', 'descricao': 'Hambúrguer com Bacon', 'preco': 17.90, 'restricao': 'padrao'},
        4: {'codigo': 4, 'nome': 'Big Couve', 'descricao': 'Crepe de Couve com queijo de soja', 'preco': 45.90, 'restricao': 'vegano'}}

@app.get('/item/')
async def item():
    return item

@app.get('/item/{id}')
async def item(id: int):
    if id in item:
        return item[id]
    else:
        raise HTTPException(404)

@app.post('/item/')
async def criar_item(item: Produto,cod,nm,desc,preco,restr):
    item.codigo = cod
    item.nome = nm
    item.descricao = desc
    item.preco = preco
    item.restricao = restr
    codigo = item.keys(cod,nm,desc,preco,restr)
    #item[codigo] = item.dict()
    #item[codigo]['codigo'] = codigo
    return item[codigo]
''''
@app.put('/item/{id}')
async def alterar_item(id: int, item: Produto):
    if id in item:
        alunos[id] = aluno.dict()
        return alunos[id]
    else:
        raise HTTPException(404)'''