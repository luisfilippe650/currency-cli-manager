import argparse
from app.config import cotacao_config

parser = argparse.ArgumentParser()

# comando principal
subparser = parser.add_subparsers(dest="comando")

# -------------------------
# CRUD MOEDA
# -------------------------
parser_moeda = subparser.add_parser("moeda")

moeda_sub = parser_moeda.add_subparsers(dest="acao")

# adicionar moeda
parser_addmoeda = moeda_sub.add_parser("add")
parser_addmoeda.add_argument("--nome", required=True)

# listar moeda
parser_listmoeda = moeda_sub.add_parser("list")

# deletar moeda
parser_deletemoeda = moeda_sub.add_parser("delete")
parser_deletemoeda.add_argument("--id", required=True)

# -------------------------
# COTAÇÃO
# -------------------------
parser_cotacao = subparser.add_parser("cotacao")
parser_cotacao.add_argument("--nome", required=True)

# -------------------------
# HISTÓRICO
# -------------------------
parser_historico = subparser.add_parser("historico")

historico_sub = parser_historico.add_subparsers(dest="acao")

parser_listarhistorico = historico_sub.add_parser("list")

parser_deletehistorico = historico_sub.add_parser("delete")

# -------------------------
# EXECUÇÃO
# -------------------------

args = parser.parse_args()

if args.comando == "moeda":

    if args.acao == "add":
        print(cotacao_config.add_coin(args.nome))

    elif args.acao == "list":
        print(cotacao_config.list_coins())

    elif args.acao == "delete":
        print(cotacao_config.delete_coin(args.id))

elif args.comando == "cotacao":
    print(cotacao_config.get_cotacao(args.nome))

elif args.comando == "historico":

    if args.acao == "list":
        print(cotacao_config.list_history())

    elif args.acao == "delete":
        print(cotacao_config.delete_history())