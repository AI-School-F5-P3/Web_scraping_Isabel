#Importación de librerías
import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv

#Variable con la dirección del sitio a hacer scraping
URL = "https://quotes.toscrape.com/"
url_base = "https://quotes.toscrape.com"


# Función para obtener el contenido HTML
def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

# Obtener el objeto BeautifulSoup para la URL principal
soup = get_soup(URL)

#Imprimir con formato
print(soup.prettify()) 

# Función para obtener la información de la página "about" del autor
def get_author_about(url):
    author_soup = get_soup(url)
    about = author_soup.find('div', class_='author-details')
    born_date = about.find('span', class_='author-born-date').get_text()
    born_location = about.find('span', class_='author-born-location').get_text()
    description = about.find('div', class_='author-description').get_text(strip=True)
    return born_date, born_location, description

# Lista para almacenar las citas
quotes_data = []

# Scraping de todas las páginas de citas
page_url = URL
while page_url:
    # Actualizar el contenido de soup para la página actual
    soup = get_soup(page_url)
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = ", ".join([tag.get_text() for tag in quote.find_all('a', class_='tag')])

        # Obtener el enlace a la página "about" del autor
        author_url = url_base + quote.find('a')['href']
        born_date, born_location, description = get_author_about(author_url)

        # Añadir los datos a la lista
        quotes_data.append([text, author, tags, born_date, born_location, description])

    # Verificar si hay una página siguiente
    next_button = soup.find('li', class_='next')
    if next_button:
        page_url = url_base + next_button.find('a')['href']
    else:
        page_url = None

quotes_df = pd.DataFrame(quotes_data,columns=['text','author','tags','born_date','born_location','description'])
    

# Inspeccionar el dataframe
first_10 = quotes_df.head(10)

print(first_10)

# Guardar los datos en un archivo CSV
with open('quotes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Text', 'Author', 'Tags', 'Born Date', 'Born Location', 'Description'])
    writer.writerows(quotes_data)

print("Scraping completed and data saved to quotes.csv.")