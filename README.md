# Proyecto de Web Scraping para XYZ Corp

## Descripción del Proyecto 📄

XYZ Corp busca una frase que represente sus valores y misión. Para ello, se desarrolló un programa en Python que realiza web scraping en [Quotes to Scrape](https://quotes.toscrape.com/). El objetivo es extraer todas las frases, junto con el autor, los tags asociados y la página "about" de cada autor. Los datos obtenidos se formatearon y almacenaron adecuadamente.

### Objetivos del Proyecto 🎯

- **Acceso a la web**: Extraer datos de una web preparada para el scraping.
- **Extracción de información relevante**: Obtener frases, autores, tags y páginas "about".
- **Formateo de datos**: Asegurar que los datos estén limpios y organizados.
- **Almacenamiento en base de datos**: Guardar la información extraída en un formato estructurado (CSV).

## Solución Implementada 🛠️

Para desarrollar la solución, se basó en dos ayudas principales, integrándolas y complementándolas para cumplir con los requisitos del proyecto.

### Código Base Utilizado

**Primera Ayuda**: Se utilizó el siguiente código proporcionado para el scraping de libros, adaptándolo a la nueva tarea:

```python
# Instalación de dependencias
"""
!pip install requests
!pip install BeautifulSoup4
!pip install pandas
"""

# Importación de librerías
import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv

# Variable con la dirección del sitio a hacer scraping
url = "https://books.toscrape.com/"

# Realizar la petición con request y guardamos el contenido de la pagina
books_to_scrape = requests.get(url)

# Parsear la información, mediante una instancia de beautiful soup
soup = BeautifulSoup(books_to_scrape.text, 'lxml')
# Confirmar el tipo de dato de la "sopa" creada
type(soup)

# Imprimir con formato
print(soup.prettify())

# Apuntar a los artículos para extraerlos
articulos = soup.find_all('article', attrs={'class':'product_pod'})
articulos

# Lista temporal para guardar los libros
libros = []

# Iterar los articulos y obtener las variables
for articulo in articulos:
    titulo_libro = articulo.h3.a.get('title')
    imagen_libro = articulo.img.get('src')
    precio_libro_raw = articulo.find('p', attrs={'class':'price_color'}).get_text()[1:]
    precio_libro = precio_libro_raw[1:]
    divisa = precio_libro_raw[0]
    temp_row = [titulo_libro, imagen_libro, precio_libro, divisa]
    libros.append(temp_row)
    print(temp_row)

quotes_df = pd.DataFrame(libros, columns=['titulo_libro', 'imagen_libro', 'precio_libro', 'divisa'])

# Inspeccionar el dataframe
first_10 = quotes_df.head(10)

print(first_10)
```


### Desarrollo del Scraper de Frases

**Segunda Ayuda**: Se utilizó el código desarrollado con la asistencia de ChatGPT, adaptándolo para extraer frases, autores, tags y páginas "about" de Quotes to Scrape.

### Tecnologías Utilizadas 💻

- **Git/GitHub**: Control de versiones y colaboración en el proyecto.
- **Trello**: Gestión y seguimiento de las tareas.
- **BeautifulSoup** y Requests: Web scraping.
- **Pandas y CSV**: Manejo y almacenamiento de datos.
- **OpenOffice**: Visualización de los datos extraídos.



## Conclusión 🏁
Este proyecto alcanzó el nivel esencial, cumpliendo con los requisitos básicos de extracción y almacenamiento de datos. Las herramientas y técnicas utilizadas permitieron desarrollar un programa funcional que satisface las necesidades de XYZ Corp. Se documentó todo el proceso y el código está disponible en el repositorio de GitHub para su revisión.

Para más detalles, consulta el código fuente y la documentación en el repositorio GitHub.
