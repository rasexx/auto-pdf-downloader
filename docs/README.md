# Automatic Google Search and PDF Download

![imagen](image.png)

Este proyecto realiza búsquedas automáticas en Google, descarga los PDFs encontrados y verifica que contengan texto seleccionable. Es una herramienta útil para la recopilación de información para investigaciones.

## Descripción

El script realiza búsquedas predefinidas en Google, simulando un navegador web para evitar bloqueos. Para cada búsqueda, obtiene los enlaces de los PDFs en los resultados, los descarga y verifica que contengan texto seleccionable. Solo se conservan los PDFs que cumplen con este criterio.

## Características principales

- Búsqueda automática en Google
- Descarga de PDFs
- Verificación de texto seleccionable en PDFs
- Interfaz gráfica para monitorear el progreso
- Registro de actividades y errores

## Requisitos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/rasexx/automatic-google-search.git
cd automatic-google-search
```

2. (Opcional) Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

1. Navega al directorio del proyecto:

```bash
cd src
```

2. Ejecuta el script principal:

```bash
python integrated_search_and_download_gui.py
```

3. Utiliza la interfaz gráfica para iniciar el proceso y monitorear el progreso.

## Personalización

Puedes modificar las búsquedas editando el archivo `search_queries_input.txt` en el directorio `src`.

## Advertencia

El uso de scripts para realizar búsquedas automáticas en Google puede violar los términos de servicio de Google. Usa este script de manera responsable y considera añadir pausas entre las búsquedas para evitar ser bloqueado.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de hacer un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

---

# Automatic Google Search and PDF Download

This project performs automatic Google searches, downloads the found PDFs, and verifies that they contain selectable text. It is a useful tool for gathering information for research.

## Description

The script performs predefined searches on Google, simulating a web browser to avoid blocks. For each search, it obtains the links of the PDFs in the results, downloads them, and verifies that they contain selectable text. Only PDFs that meet this criterion are kept.

## Main Features

- Automatic Google search
- PDF download
- Verification of selectable text in PDFs
- Graphical interface to monitor progress
- Activity and error logging

## Requirements

- Python 3.6 or higher
- pip (Python package manager)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/rasexx/automatic-google-search.git
cd automatic-google-search
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Navigate to the project directory:

```bash
cd src
```

2. Run the main script:

```bash
python integrated_search_and_download_gui.py
```

3. Use the graphical interface to start the process and monitor progress.

## Customization

You can modify the searches by editing the `search_queries_input.txt` file in the `src` directory.

## Warning

Using scripts to perform automatic searches on Google may violate Google's terms of service. Use this script responsibly and consider adding pauses between searches to avoid being blocked.

## Contributions

Contributions are welcome. Please open an issue to discuss major changes before making a pull request.

## License

This project is under the MIT License. See the LICENSE file for more details.
