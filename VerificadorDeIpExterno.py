# verifica ip externo
import json
from urllib.request import urlopen



def formato():
    api = urlopen('https://ipinfo.io/json')  # requisição
    dados = json.load(api) # carrega o dicionário json
    
    print("Informações sobre o ip")
    print(f"IP: {dados['ip']}")
    print(f"ORG: {dados['org']}")
    print(f"CIDADE: {dados['city']}")
    print(f"PAÍS: {dados['country']}")
    print(f"REGIÃO: {dados['region']}")


if __name__ == '__main__':
    formato()
