# %%
from urllib.request import urlopen
from bs4 import BeautifulSoup


# Consultando o site da feito para o curso - Alura Motors
url = 'https://alura-site-scraping.herokuapp.com/hello-world.php'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

print(soup.find('h1', id = 'hello-world').get_text())
print(soup.find('p').get_text())

print(soup.find('h1', {'class': 'sub-header'}).get_text())


# %%
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError


# Consultando a plataforma da Alura
url = 'https://www.alura.com.br'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

try:
    req = Request(url, headers = headers)
    response = urlopen(req)
    print(response.read())

except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)


# %%
from urllib.request import urlopen


def process_html_response(input: bytes) -> str:
    input = input.decode('utf-8')

    return ' '.join(input.split()).replace('> <', '><')


# Consultando o site da feito para o curso - Alura Motors
url = 'https://alura-site-scraping.herokuapp.com/index.php'

response = urlopen(url)
html = response.read()


# Tratando os dados obtidos
html = process_html_response(html)

print(html)


from bs4 import BeautifulSoup

# Criando um objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Mostrando na tela de uma forma bonita, identada
print(soup.prettify())

# Buscando um elemento de forma sequencial, percorrendo a DOM
print(soup.html.head.title)

# Busca o texto dentro da tag
print(soup.title.get_text())
print(soup.h5.getText())

print(soup.img)

# Acessando os atributos de uma tag - esse método retorna um dicionário
print(soup.img.attrs)

# Buscando as chaves do dicionário do método acima
print(soup.img.attrs.keys())

# Buscando os valores
print(soup.img.attrs.values())

# Acessando valores em forma de dicionário
print(soup.img['class'])
print(soup.img.get('src'))