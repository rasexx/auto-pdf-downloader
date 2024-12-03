# Importación de módulos necesarios
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

# Función para sanitizar nombres de archivos
def sanitize_filename(filename):
    return re.sub(r'[\/*?:"<>|]', "", filename)

# Función para realizar búsquedas en Google
def google_search(query):
    # Construcción de la URL de búsqueda
    url = f"https://www.google.com/search?q={query}+filetype:pdf"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        # Realizar la solicitud HTTP
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Analizar el contenido HTML de la respuesta
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('div', class_='yuRUbf')

        # Extraer enlaces a PDFs
        pdf_links = []
        for result in search_results:
            link = result.find('a')['href']
            if link.lower().endswith('.pdf'):
                pdf_links.append(link)

        return pdf_links[:3]  # Retorna hasta 3 enlaces PDF
    except requests.RequestException as e:
        logging.error(f"Error en la búsqueda de Google: {e}")
        return []

# Función para descargar un PDF
def download_pdf(url, folder, progress_callback):
    try:
        # Realizar la solicitud HTTP para descargar el PDF
        response = requests.get(url, stream=True, allow_redirects=True)
        response.raise_for_status()

        # Manejar redirecciones manualmente si es necesario
        if 'Location' in response.headers:
            url = response.headers['Location']
            response = requests.get(url, stream=True)
            response.raise_for_status()

        # Obtener el nombre del archivo del encabezado de la respuesta
        content_disposition = response.headers.get('content-disposition')
        if content_disposition:
            filename = re.findall("filename=(.+)", content_disposition)[0].strip('"')
        else:
            parsed_url = urlparse(unquote(url))
            filename = os.path.basename(parsed_url.path)
        if not filename.lower().endswith('.pdf'):
            filename += '.pdf'

        # Sanitizar el nombre del archivo
        filename = sanitize_filename(filename)
        filepath = os.path.join(folder, filename)

        # Descargar el archivo en bloques
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

# Función para verificar si un PDF tiene texto seleccionable
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

# Clase para la interfaz gráfica de búsqueda y descarga
class SearchDownloadGUI:
    def __init__(self, master):
        self.master = master
        master.title("Búsqueda y Descarga Automática de PDFs")
        master.geometry("800x600")

        # Configuración del modo oscuro
        self.master.configure(bg='#2e2e2e')
        # Variables para el progreso y el estado
        self.overall_progress = tk.DoubleVar()
        self.current_progress = tk.DoubleVar()
        self.status_var = tk.StringVar()

        # Crear los widgets de la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Crear el marco principal
        main_frame = ttk.Frame(self.master, padding="10", style='Dark.TFrame')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # Título y descripción
        ttk.Label(main_frame, text="Búsqueda y Descarga Automática de PDFs", font=("Helvetica", 16, "bold"), foreground='white', background='#2e2e2e').grid(column=0, row=0, sticky=tk.W, pady=10)
        ttk.Label(main_frame, text="Esta aplicación busca y descarga PDFs automáticamente desde Google.", font=("Helvetica", 10), foreground='white', background='#2e2e2e').grid(column=0, row=1, sticky=tk.W, pady=5)
        # Botón para iniciar el proceso
        ttk.Button(main_frame, text="Iniciar Proceso", command=self.start_process, style='Dark.TButton').grid(column=0, row=2, sticky=tk.W, pady=10)

        # Barra de progreso general
        ttk.Label(main_frame, text="Progreso General:", foreground='white', background='#2e2e2e').grid(column=0, row=3, sticky=tk.W, pady=5)
        self.overall_progress_bar = ttk.Progressbar(main_frame, length=700, variable=self.overall_progress, maximum=100, style='Dark.Horizontal.TProgressbar')
        self.overall_progress_bar.grid(column=0, row=4, sticky=(tk.W, tk.E), pady=5)

        # Barra de progreso actual
        ttk.Label(main_frame, text="Progreso Actual:", foreground='white', background='#2e2e2e').grid(column=0, row=5, sticky=tk.W, pady=5)
        self.current_progress_bar = ttk.Progressbar(main_frame, length=700, variable=self.current_progress, maximum=100, style='Dark.Horizontal.TProgressbar')
        self.current_progress_bar.grid(column=0, row=6, sticky=(tk.W, tk.E), pady=5)

        # Área de texto para mostrar el estado actual
        self.status_text = tk.Text(main_frame, height=10, wrap='word', bg='#3e3e3e', fg='white', font=("Helvetica", 10, "bold"))
        self.status_text.grid(column=0, row=7, sticky=(tk.W, tk.E), pady=10)
        self.status_text.insert(tk.END, "Estado de la aplicación...\n")
        self.status_text.config(state=tk.DISABLED)

        # Configurar estilos personalizados
        style = ttk.Style()
        style.configure('Dark.TFrame', background='#2e2e2e')
        style.configure('Dark.TButton', background='#4e4e4e', foreground='white')
        style.configure('Dark.Horizontal.TProgressbar', troughcolor='#4e4e4e', background='#00ff00')
        main_frame.columnconfigure(0, weight=1)

    # Método para iniciar el proceso de búsqueda y descarga
    def start_process(self):
        self.overall_progress.set(0)
        self.current_progress.set(0)
        self.update_status("Iniciando proceso...")
        self.show_loading_animation()
        threading.Thread(target=self.run_search_and_download, daemon=True).start()

    # Método para mostrar la animación de carga
    def show_loading_animation(self):
        # Aquí puedes cargar un GIF animado o un icono de carga
        # Por simplicidad, se muestra un texto de carga
        self.loading_label = ttk.Label(self.master, text="Cargando...", font=("Helvetica", 12, "bold"), foreground='white', background='#2e2e2e')
        self.loading_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.master.update_idletasks()

    # Método para ocultar la animación de carga
    def hide_loading_animation(self):
        if hasattr(self, 'loading_label'):
            self.loading_label.destroy()
    # Método para actualizar el estado en el área de texto
    def update_status(self, message):
        self.status_text.config(state=tk.NORMAL)
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.config(state=tk.DISABLED)
        self.status_text.see(tk.END)

    # Método para ejecutar la búsqueda y descarga
    def run_search_and_download(self):
        # Configuración del registro de actividades
        logging.basicConfig(filename='search_download_log.txt', level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')

        # Leer las búsquedas desde el archivo de entrada
        script_dir = os.path.dirname(os.path.abspath(__file__))
        input_file = os.path.join(script_dir, 'search_queries_input.txt')
        with open(input_file, 'r', encoding='utf-8') as f:
            searches = [line.strip() for line in f if line.strip()]

        # Crear el directorio para los resultados
        results_folder = "search_results"
        os.makedirs(results_folder, exist_ok=True)

        # Realizar las búsquedas y descargas
        total_searches = len(searches)
        for i, search in enumerate(searches, 1):
            self.update_status(f"Buscando: {search}")
            logging.info(f"Búsqueda: {search}")
            results = google_search(search)

            pdf_found = False
            for j, link in enumerate(results, 1):
                self.update_status(f"Descargando PDF {j} de {len(results)} para '{search}'")
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

        self.update_status("Proceso completado.")
        logging.info("Proceso de búsqueda y descarga finalizado.")
        self.hide_loading_animation()

    # Método para actualizar el progreso actual
    def update_current_progress(self, value):
        self.current_progress.set(value)
        self.master.update_idletasks()

# Función principal para iniciar la aplicación
def main():
    root = tk.Tk()
    app = SearchDownloadGUI(root)
    root.mainloop()

# Ejecutar la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()

