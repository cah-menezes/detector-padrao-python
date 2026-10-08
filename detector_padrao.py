"""Detector de Padrão
Recebe um texto, varre procurando CPF (000.000.000-00) e e-mail (nome@dominio.com), e reporta o que encontrou."""

from re import search

#Termos que serão buscados
dados = {
    "CPF":  {"receita": r"\d{3}\.\d{3}\.\d{3}-\d{2}", "descrição": "CPF - dado pessoal sensível (LGPD)"},
    "E-mail": {"receita": r"[a-z]+@[a-z]+\.[a-z]+", "descrição": "Email..."}
}

#Funções
def buscar(texto):
    #escaneia o texto a procura dos dados sensiveis
    encontradas = []
    for tipo in dados:
        padrao = dados[tipo]["receita"]
        busca = search(padrao, texto)
        encontradas.append((tipo, busca))
    return encontradas

def resultado(encontradas):
    for tipo in encontradas:
        if tipo[1] is not None:
            print(f"Os dados sensíveis: {tipo[0]}: {tipo[1].group()}, foram encontrados no seu texto.")
        else:
            print("Nenhum dado sensível encontrado.")

#Programa principal
if __name__ == "__main__":
    texto = input("Cole o texto para análise: ")
    buscar_no_texto = buscar(texto)
    resultado(buscar_no_texto)
