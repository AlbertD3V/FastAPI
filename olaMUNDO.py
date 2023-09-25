from  fastapi import FastAPI


app =FastAPI()

@app.get('/')
async def root():
    return {'mensagem': 'Olá Mundo'}

@app.get('/test')
async def test():
    return {'test':'testado =D'}