import requests


print('''
=====================================
---------- IFNORME SEU CEP ----------
=====================================
''')
cep = int(input("Informe seu CEP: "))



response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
dicio = response.json()
print(f'Bairro:{dicio["bairro"]}')
print(f'Cidade:{dicio["localidade"]}')
print(f'Estado:{dicio["uf"]}')
print('-'*30)

latitude = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={dicio["localidade"]},{dicio["uf"]},BR&limit=1&appid=7fb1faec61a93f327bf29097dcd13d48')
lati = latitude.json()[0]
print(f'Latitude: {lati["lat"]}')
print(f'Longitude: {lati["lon"]}')
print('-'*30)

tempo = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat=-12.9822499&lon=-38.4812772&lang=pt_br&units=metric&appid=7fb1faec61a93f327bf29097dcd13d48')
temp = tempo.json()
print(f'Humidade: {temp["main"]["humidity"]}')
print(f'Temperatura max: {temp["main"]["temp"]}')
print(f'Sensação térmica: {temp["main"]["feels_like"]}')
print('-'*30)

