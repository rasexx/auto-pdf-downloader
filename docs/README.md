# Automatic Google Search

Este proyecto realiza búsquedas automáticas en Google y recopila los enlaces de los primeros 3 resultados para cada búsqueda. Es una herramienta útil para ayudar en la recopilación de información para investigaciones.

## Descripción

El script realiza búsquedas predefinidas en Google, simulando un navegador web para evitar bloqueos. Para cada búsqueda, obtiene los enlaces de los tres primeros resultados y los guarda en un archivo de texto. Esto puede ser especialmente útil para recopilar rápidamente recursos sobre temas específicos.

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
    python main.py
```

3. El script realizará las búsquedas predefinidas y guardará los resultados en un archivo llamado `search_results.txt` en el directorio raíz del proyecto.

## Personalización

Puedes modificar las búsquedas editando la lista `searches` en el archivo `src/main.py`.

### Puedes consultar la [Guia Oficial de Google](https://support.google.com/websearch/answer/35890) para realizar busquedas avanzadas

## Advertencia

El uso de scripts para realizar búsquedas automáticas en Google puede violar los términos de servicio de Google. Usa este script de manera responsable y considera añadir pausas entre las búsquedas para evitar ser bloqueado.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de hacer un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

# Automatic Google Search

This project performs automatic Google searches and collects the links of the first 3 results for each search. It is a useful tool to assist in gathering information for research.

## Description

The script performs predefined Google searches, simulating a web browser to avoid crashes. For each search, it fetches the links of the first three results and saves them to a text file. This can be especially useful for quickly gathering resources on specific topics.

## Requirements

- Python 3.6 or higher
- pip (Python package manager)

## Installation

1. Clone this repository:

```bash
    git clone https://github.com/rasexx/automatic-google-search.git
    cd automatic-google-search
```

(Optional) Create and activate a virtual environment:

```bash
    python -m venv venv
    source venv/bin/activate # On Windows use: venv/scripts/activate
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
    python main.py
```

3. The script will perform the predefined searches and save the results in a file named ``search_results.txt`` in the root directory of the project.

## Customization

You can modify the searches by editing the `searches` list in the `src/main.py` file.

### You can consult the [Official Google Guide](https://support.google.com/websearch/answer/35890) to perform advanced searches.

## Warning

Using scripts to perform automatic Google searches may violate Google's terms of service. Use this script responsibly and consider adding pauses between searches to avoid being blocked.

## Contributions

Contributions are welcome. Please open an issue to discuss major changes before making a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.