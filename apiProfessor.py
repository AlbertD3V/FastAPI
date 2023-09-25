from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Aluno(BaseModel):
    nome: str
    idade: int

class Idade(BaseModel):
    idade: int

app = FastAPI()

alunos = {0: {'nome': 'Jorge', 'idade': 20},
          1: {'nome': 'Maria', 'idade': 22},
          2: {'nome': 'Pedro', 'idade': 33},
          3: {'nome': 'Júlia', 'idade': 16}}

@app.get('/aluno/')
async def listar_alunos(idade_min: int = -1, idade_max: int = 999):
    return {id: aluno for id, aluno in alunos.items() 
            if aluno['idade'] >= idade_min 
            and aluno['idade'] <= idade_max}

@app.get('/aluno/{id}')
async def consultar_aluno(id: int):
    if id in alunos:
        return alunos[id]
    else:
        raise HTTPException(404)

@app.post('/aluno/')
async def cadastrar_aluno(aluno: Aluno):
    id = max(alunos.keys(), default=-1) + 1
    alunos[id] = aluno.dict()
    alunos[id]['id'] = id
    return alunos[id]

@app.put('/aluno/{id}')
async def alterar_aluno(id: int, aluno: Aluno):
    if id in alunos:
        alunos[id] = aluno.dict()
        return alunos[id]
    else:
        raise HTTPException(404)

@app.delete('/aluno/{id}')
async def remover_aluno(id: int):
    if id in alunos:
        return alunos.pop(id)
    else:
        raise HTTPException(404)

@app.patch('/aluno/{id}')
async def alterar_idade_aluno(id: int, idade: Idade):
    if id in alunos:
        alunos[id]['idade'] = idade.idade
        return alunos[id]
    else:
        raise HTTPException(404)
