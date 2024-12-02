import tkinter as tk
from tkinter import ttk
import threading
import requests
from bs4 import BeautifulSoup
import time
import random
import os
from urllib.parse import urlparse, unquote
import re
import PyPDF2
import logging

def sanitize_filename(filename):
    return re.sub(r'[\/*?:"<>|]', "", filename)

def google_search(query):
    url = f"https://www.google.com/search?q={query}+filetype:pdf"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('div', class_='yuRUbf')

        pdf_links = []
        for result in search_results:
            link = result.find('a')['href']
            if link.lower().endswith('.pdf'):
                pdf_links.append(link)

        return pdf_links[:3]  # Retorna hasta 3 enlaces PDF
    except requests.RequestException as e:
        logging.error(f"Error en la búsqueda de Google: {e}")
        return []

def download_pdf(url, folder, progress_callback):
    try:
        response = requests.get(url, stream=True, allow_redirects=True)
        response.raise_for_status()

        # Manejar redirecciones manualmente si es necesario
        if 'Location' in response.headers:
            url = response.headers['Location']
            response = requests.get(url, stream=True)
            response.raise_for_status()

        content_disposition = response.headers.get('content-disposition')
        if content_disposition:
            filename = re.findall("filename=(.+)", content_disposition)[0].strip('"')
        else:
            parsed_url = urlparse(unquote(url))
            filename = os.path.basename(parsed_url.path)
        if not filename.lower().endswith('.pdf'):
            filename += '.pdf'

        filename = sanitize_filename(filename)
        filepath = os.path.join(folder, filename)

        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 KB
        downloaded = 0

        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(chunk_size=block_size):
                size = file.write(chunk)
                downloaded += size
                percent = int(100 * downloaded / total_size) if total_size > 0 else 0
                progress_callback(percent)

        return filepath
    except requests.RequestException as e:
        logging.error(f"Error al descargar {url}: {e}")
        return None

def has_selectable_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            if len(reader.pages) > 0:
                text = reader.pages[0].extract_text()
                return len(text.strip()) > 0
    except Exception as e:
        logging.error(f"Error al procesar el PDF {pdf_path}: {e}")
    return False

class SearchDownloadGUI:
    def __init__(self, master):
        self.master = master
        master.title("Búsqueda y Descarga Automática de PDFs")
        master.geometry("800x600")

        self.overall_progress = tk.DoubleVar()
        self.current_progress = tk.DoubleVar()
        self.status_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        ttk.Button(main_frame, text="Iniciar Proceso", command=self.start_process).grid(column=0, row=0, sticky=tk.W, pady=5)

        ttk.Label(main_frame, text="Progreso General:").grid(column=0, row=1, sticky=tk.W, pady=5)
        self.overall_progress_bar = ttk.Progressbar(main_frame, length=700, variable=self.overall_progress, maximum=100)
        self.overall_progress_bar.grid(column=0, row=2, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(main_frame, text="Progreso Actual:").grid(column=0, row=3, sticky=tk.W, pady=5)
        self.current_progress_bar = ttk.Progressbar(main_frame, length=700, variable=self.current_progress, maximum=100)
        self.current_progress_bar.grid(column=0, row=4, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(main_frame, textvariable=self.status_var).grid(column=0, row=5, sticky=tk.W, pady=5)

        main_frame.columnconfigure(0, weight=1)

    def start_process(self):
        self.overall_progress.set(0)
        self.current_progress.set(0)
        self.status_var.set("Iniciando proceso...")
        threading.Thread(target=self.run_search_and_download, daemon=True).start()

    def run_search_and_download(self):
        logging.basicConfig(filename='search_download_log.txt', level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')

        script_dir = os.path.dirname(os.path.abspath(__file__))
        input_file = os.path.join(script_dir, 'search_queries_input.txt')
        with open(input_file, 'r', encoding='utf-8') as f:
            searches = [line.strip() for line in f if line.strip()]

        results_folder = "search_results"
        os.makedirs(results_folder, exist_ok=True)

        total_searches = len(searches)
        for i, search in enumerate(searches, 1):
            self.status_var.set(f"Buscando: {search}")
            logging.info(f"Búsqueda: {search}")
            results = google_search(search)

            pdf_found = False
            for j, link in enumerate(results, 1):
                self.status_var.set(f"Descargando PDF {j} de {len(results)} para '{search}'")
                self.current_progress.set(0)
                filepath = download_pdf(link, results_folder, self.update_current_progress)

                if filepath and has_selectable_text(filepath):
                    logging.info(f"PDF con texto seleccionable descargado: {filepath}")
                    pdf_found = True
                    break  # Mantener solo el primer PDF con texto seleccionable
                elif filepath:
                    os.remove(filepath)
                    logging.info(f"PDF sin texto seleccionable eliminado: {filepath}")

            if not pdf_found:
                logging.warning(f"No se encontró un PDF válido para la búsqueda: {search}")
            self.overall_progress.set((i / total_searches) * 100)
            time.sleep(random.uniform(2, 5))

        self.status_var.set("Proceso completado.")
        logging.info("Proceso de búsqueda y descarga finalizado.")

    def update_current_progress(self, value):
        self.current_progress.set(value)
        self.master.update_idletasks()

def main():
    root = tk.Tk()
    app = SearchDownloadGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

