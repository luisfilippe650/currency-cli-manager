from app.crud import cotacao_crud
from app.crud import historic_crud
from app.service import cotacao_service


# adicionar moeda no banco de dados
def add_coin(name):
    value = cotacao_service.add_moeda(name)

    if value is False:
        return "currency does not exist"

    return cotacao_crud.add_coin(name)


# listar todas as moedas adicionadas no banco de dados
def list_coins():
    return cotacao_crud.list_coins()


# puxar a moeda cadastrada do banco de dados, listar cotação e salvar no histórico
def get_exchange_rate(currency):
    # conferir se existe no banco de dados essa moeda
    result = cotacao_crud.find_coin(currency)

    if result is None:
        return "currency not found in database"

    # como o SELECT retorna uma tupla, pegamos o valor da moeda
    base_currency = result[0]

    # puxar valor na API
    exchange_rate = cotacao_service.search_exchange_rate(base_currency)

    if exchange_rate is None:
        return "error fetching exchange rate"

    # salvar no histórico
    historic_crud.save_value(base_currency, "BRL", exchange_rate)

    return f"currency: {base_currency}\nvalue in BRL: {exchange_rate}"


# deletar moeda adicionada
def delete_coin(id):
    return cotacao_crud.delete_coin(id)


# listar histórico de moedas
def list_history():
    return historic_crud.list_history()


# deletar o histórico
def delete_history():
    return historic_crud.delete_history()