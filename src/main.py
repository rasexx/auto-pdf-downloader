import requests
from bs4 import BeautifulSoup
import time
import random

def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('div', class_='yuRUbf')
    
    top_3_links = []
    for result in search_results[:3]:
        link = result.find('a')['href']
        top_3_links.append(link)
    
    return top_3_links

def main():
    searches = [
        'example of a search',
        'example of a search 2',
        'example of a search 3',
        'you can use infinite searches by adding more queries to the list'
    ]

    with open('search_results.txt', 'w', encoding='utf-8') as f:
        for i, search in enumerate(searches, 1):
            print(f"Realizando búsqueda {i} de {len(searches)}: {search}")
            results = google_search(search)
            
            f.write(f"Resultados para: {search}\n")
            for j, link in enumerate(results, 1):
                f.write(f"{j}. {link}\n")
            f.write("\n")
            
            # Pausa aleatoria entre búsquedas para evitar ser bloqueado
            time.sleep(random.uniform(5, 10))

    print("Búsquedas completadas. Los resultados se han guardado en 'search_results.txt'")

if __name__ == "__main__":
    main()