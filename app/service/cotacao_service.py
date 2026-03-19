import requests

def add_moeda(name):

    url = f"https://open.er-api.com/v6/latest/{name}"

    response = requests.get(url)

    if response.status_code != 200:
        print("Erro ao acessar API")
        return False

    dados = response.json()

    if dados.get("result") == "success":
        return True
    else:
        return False


def serachCotacao(moeda):

    url = f"https://open.er-api.com/v6/latest/{moeda}"

    response = requests.get(url)

    if response.status_code != 200:
        print("Erro na API:", response.status_code)
        return None, None

    try:
        dados = response.json()
    except:
        print("Resposta da API não é JSON")
        print(response.text)
        return None, None

    if dados.get("result") != "success":
        print("Moeda não encontrada")
        return None, None

    BRL = dados["rates"]["BRL"]
    date = dados["time_last_update_utc"]

    return BRL, date