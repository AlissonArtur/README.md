import requests

url = 'http://localhost:5000/api/saque'

try:
    
    response = requests.get(url)
    

    if response.status_code == 200:
        calculo = response.json()['valor']








print('{:^30}'.format('BANCO MORADAAI'))


valor = response.json()['valor']

total = valor
céd = 100
totcéd = 0

while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        print(f'total de {totcéd} cédulas de R${céd}')
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 2
        elif céd == 2:
            céd =1
        totcéd = 0
        if total == 0:
            break

resultado = eval(totcéd)