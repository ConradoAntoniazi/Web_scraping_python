import requests
from bs4 import BeautifulSoup as bs
from datetime import date

# retorna um objeto BeautifulSoup contendo a estura da página endereçada por 'url'
def get_html(url):
    # Envia uma solicitação HTTP GET para a página do perfil
    response = requests.get(url)

    # Quebra o código caso não consiga acessar a página
    if response.status_code != 200:
        print("Não foi possivel acessar a página!")
        exit(1)

    #CASO TENHA CHEGADO ATÉ AQUI, FOI POSSÍVEL ABRIR A PÁGINA

    # Parseia o conteúdo HTML da página (organiza o código da página HTML para ficar mais fácil de ser trabalhada)
    html = bs(response.text, 'html.parser')
    return html

# retorna a url da página contendo o cardápio do ru
def faz_url_ru():
    # Solicita a data para busca do cardápio correspondente àquele dia
    data = date.today()

    # URL do site do cardápio do dia informado
    return f"https://ru.ufes.br/cardapio/{data}"

# retorna o cardápio em si ou None, se não for encontrado
def acha_texto_cardapio(html):
    #caixa (div) que contém o cardápio do RU daquele dia
    cardapio_html = html.find("div", class_="view-content")

    if not cardapio_html:
        print("Problema na extração do cardápio da UFES.")
        exit(1)
    
    cardapio_text = cardapio_html.get_text().strip()

    if not ("Almoço" in cardapio_text):
        return None

    return cardapio_text


# retorna o cardápio do dia
def retorna_cardapio_ru():
    url = faz_url_ru()

    html = get_html(url)

    cardapio_ru = acha_texto_cardapio(html)

    return cardapio_ru