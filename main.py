# %%
from cgitb import text
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

# %%
def process_html_response(input: bytes) -> str:
    input = input.decode('utf-8')

    return ' '.join(input.split()).replace('> <', '><')

# %%
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
soup.prettify()

# Buscando um elemento de forma sequencial, percorrendo a DOM
soup.html.head.title

# Busca o texto dentro da tag
soup.title.get_text()
soup.h5.getText()

soup.img

# Acessando os atributos de uma tag - esse método retorna um dicionário
soup.img.attrs

# Buscando as chaves do dicionário do método acima
soup.img.attrs.keys()

# Buscando os valores
soup.img.attrs.values()

# Acessando valores em forma de dicionário
soup.img['class']
soup.img.get('src')


# %%
# Pesquisando com o BeautifulSoup

soup.find('img')

soup.findAll('img')

soup.findAll('img', limit=1)

# A forma de pesquisar abaixo é igual ao findAll, sem limit
soup('img')

soup.findAll(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

soup.findAll('p', {'class':'txt-value'})

soup.findAll('p', text='Belo Horizonte - MG')

soup.findAll('img', alt='Foto')

for item in soup.findAll('img', alt='Foto'):
    print(item.get('src'))

# Tomar cuidado com a palavra 'class'
soup.find_all('p', class_='txt-value')

# Encontrando todos os textos dentro das tags
soup.find_all(text = True)


# %%
# Outros métodos de pesquisa

html_teste = """
    <html>
        <body>
            <div id="container-a">
                <h1>Título A</h1>
                <h2 class="ref-a">Sub título A</h2>
                <p>Texto de conteúdo A</p>
            </div>
            <div id="container-b">
                <h1>Título B</h1>
                <h2 class="ref-b">Sub título B</h2>
                <p>Texto de conteúdo B</p>
            </div>
        </body>
    </html>
"""

# Tratando o conteúdo html
html_teste = process_html_response(html_teste)

# Criando um objeto BeautifulSoup
soup = BeautifulSoup(html_teste, 'html.parser')

soup.find('h2')

# Parents
soup.find('h2').find_parent('div')
soup.find('h2').find_parents()
soup.findAll('h2')

for item in soup.findAll('h2'):
    print(item.find_parent('div'))

# Siblings
soup.find('h2').findNextSibling()
soup.find('h2').findPreviousSibling()
soup.find('p').findPreviousSiblings()

# Next and Previous
soup.find('h2').find_next()
soup.find('h2').find_previous()
soup.find('h2').find_all_next()


# %%
# WebScraping do site Alura Motors

from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

response = urlopen('https://alura-site-scraping.herokuapp.com/index.php')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

crads = []
card = {}

# OBTENDO OS DADOS DO PRIMEIRO CARD

anuncio = soup.find('div', {'class': 'well card'})

# Obtendo o valor do veiculo
anuncio.find('div', {'class':'value-card'})
anuncio.find('p', {'class':'txt-value'}).get_text()

card['value'] = anuncio.find('p', {'class':'txt-value'}).get_text()

# %%
# Obtendo informações sobre o veículo anunciado
anuncio.find('div', {'class':'body-card'}).find_all('p')

infos = anuncio.find('div', {'class':'body-card'}).find_all('p')

for info in infos:
    card[info.get('class')[0].split('-')[-1]] =  info.get_text()

# %%
# Obtendo os acessorios
anuncio.find('div', {'class':'body-card'}).ul.find_all('li')

items = anuncio.find('div', {'class':'body-card'}).ul.find_all('li')

items.pop()

acessorios = []

for item in items:
    acessorios.append(item.get_text().replace('► ', ''))

card['items'] = acessorios

# %%
# Criando um dataframe com os dados extraidos
import pandas as pd

# O .T no final da linha faz a transposição do dataframe
dataset = pd.DataFrame().from_dict(card, orient='index').T

dataset.to_csv('./data/dataset.csv', sep=';', index=False, encoding='utf-8-sig')

# %%
# Obtendo a foto o anuncio
from urllib.request import urlretrieve

image = anuncio.find('div', {'class':'image-card'}).img

image.get('src')

urlretrieve(image.get('src'), './img/' + image.get('src').split('/')[-1])