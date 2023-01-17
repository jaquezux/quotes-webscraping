# Web Scraping - Quotes to Scrape

## Passo a passo do setup:

1) Já tendo o Python instalado, precisei instalar o BeautifulSoup através do VSCode, rodando o código abaixo no Terminal:

```python
> pip install beautifulsoup4
```

2) No arquivo main.py, digitei as primeiras linhas de código, que são as importações das bibliotecas necessárias para o scraping:

```python
from bs4 import BeautifulSoup
import requests
```

3) O site utilizado foi o https://quotes.toscrape.com, que é específico para essa atividade. Fiz a identificação dos elementos que preciso extrair. Nesse caso, é a citação + nome do autor.

![webscraping_quotestoscrape](https://user-images.githubusercontent.com/97712990/212784820-cef02f1b-fe19-4f11-9117-b98d7f221498.jpg)


Para isso, cliquei em cima do elemento com o botão direito do mouse e selecionei a opção “Inspecionar”, que me levou ao código HTML da página.

- A citação está dentro de um ```<span>```, com a classe ```“text”```.
- O autor está dentro de um ```<small>```, com a classe ```“author”```.


## Escrevendo o código:
```python
1. page_to_scrape = requests.get("https://quotes.toscrape.com")
2. soup = BeautifulSoup(page_to_scrape.text, "html.parser")
3. quotes = soup.findAll("span", class_="text")                    
4. authors = soup.findAll("small", class_="author")
```
1. A variável **page_to_scrape** vai fazer o request (```requests.get```) do site.
2. A variável **soup** está pedindo para o BeautifulSoup fazer a análise do HTML (```"html.parser"```) que está sendo extraído na variável page_to_scrape (```page_to_scrape.text```).
3. A variável **quotes** está usando o método ```findAll```, que usa os argumentos tag do html e classe. A citação encontra-se na tag (```"span"```) e classe (```class_="text"```).
4. A variável **authors** está usando o método ```findAll```, que usa os argumentos tag do html e classe. O autor encontra-se na tag (```"small"```) e a classe (```class_="author"```).


## Imprimindo o resultado:
```python
for quote, author in zip(quotes[2], authors[2]):
    print(quote.text + " - " + author.text)
```
###### Estou pedindo para que, para cada citação e autor dentro da lista de citações e autores disponíveis no site, o Python deve imprimir a citação + “ - “ + o nome do autor.

#### Exemplo de saída:
“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.” - Albert Einstein
