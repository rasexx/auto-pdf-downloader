# Auto PDF Downloader

![imagen](image.png)

# Auto PDF Downloader

## Documentación Técnica

### Autor

**Jose Ramon Garcia Del Risco**

### Título del Proyecto

**Auto PDF Downloader**

### Fecha

**Octubre 2023**

---

### Descripción del Proyecto

Este proyecto está diseñado para automatizar el proceso de búsqueda de documentos PDF en Google, descargarlos y verificar que contengan texto seleccionable. La herramienta es particularmente útil para investigadores que necesitan recopilar una gran cantidad de documentos de manera rápida y eficiente. Al automatizar el proceso de búsqueda y descarga, la herramienta ahorra tiempo y asegura que los documentos recopilados estén en un formato utilizable.

La aplicación cuenta con una interfaz gráfica de usuario (GUI) que permite a los usuarios monitorear el progreso del proceso de búsqueda y descarga en tiempo real. La GUI proporciona retroalimentación visual sobre el estado de cada consulta de búsqueda y el progreso de descarga de cada archivo PDF.

### Objetivos y Alcance

Los principales objetivos de este proyecto son:
- **Automatizar Búsquedas en Google**: La herramienta realiza búsquedas automatizadas en Google basadas en consultas de búsqueda proporcionadas por el usuario.
- **Descargar PDFs**: Descarga los archivos PDF encontrados en los resultados de búsqueda.
- **Verificar el Contenido de los PDFs**: La herramienta verifica que los PDFs descargados contengan texto seleccionable, asegurando que no sean solo imágenes escaneadas.
- **GUI Amigable para el Usuario**: Se proporciona una interfaz gráfica de usuario para permitir a los usuarios iniciar fácilmente el proceso de búsqueda y descarga y monitorear su progreso.

El alcance de este proyecto incluye:
- **Web Scraping**: Usar la biblioteca `requests` para realizar web scraping.
- **Análisis de HTML**: Utilizar `BeautifulSoup` para analizar el contenido HTML y extraer información relevante.
- **Descarga de Archivos**: Descargar archivos usando solicitudes HTTP.
- **Verificación de PDFs**: Usar `PyPDF2` para verificar el contenido de los PDFs descargados.
- **Desarrollo de GUI**: Crear una interfaz amigable para el usuario usando `tkinter`.

### Módulos y Componentes

- **integrated_search_and_download_gui.py**: Este es el script principal que integra la GUI con las funcionalidades de búsqueda y descarga. Maneja las entradas del usuario, realiza búsquedas en Google, descarga PDFs y verifica su contenido.
- **requirements.txt**: Este archivo lista todas las dependencias requeridas para el proyecto, asegurando que todas las bibliotecas necesarias estén instaladas.
- **README.md**: Proporciona una descripción general del proyecto, incluyendo instrucciones de instalación y guías de uso.
- **LICENSE**: Contiene la información de licencia del proyecto, especificando los términos bajo los cuales el proyecto puede ser usado y distribuido.
- **.gitignore**: Especifica archivos y directorios que deben ser ignorados por Git, evitando que sean incluidos en el control de versiones.

### Organización de Archivos y Directorios

- **/src**: Este directorio contiene el script principal y el directorio para almacenar los resultados de búsqueda.
  - **integrated_search_and_download_gui.py**: El script principal que maneja las funcionalidades centrales del proyecto.
  - **search_results**: Un directorio donde se almacenan los PDFs descargados. Cada consulta de búsqueda resulta en un subdirectorio que contiene los PDFs correspondientes.
- **/docs**: Este directorio contiene archivos de documentación.
  - **README.md**: Proporciona una descripción general del proyecto y guías de uso.
  - **LICENSE**: Contiene la información de licencia del proyecto.
  - **TECHNICAL_DOCUMENTATION.md**: Este archivo, que proporciona documentación técnica detallada del proyecto.
- **requirements.txt**: Lista todas las dependencias requeridas para el proyecto, asegurando que todas las bibliotecas necesarias estén instaladas.
- **.gitignore**: Especifica archivos y directorios que deben ser ignorados por Git, evitando que sean incluidos en el control de versiones.

### Dependencias

Este proyecto depende de varias bibliotecas de Python para realizar sus tareas. Las dependencias están listadas en el archivo `requirements.txt` e incluyen:

- **beautifulsoup4==4.12.3**: Una biblioteca para analizar documentos HTML y XML. Se usa para extraer datos de páginas web.
- **certifi==2024.8.30**: Proporciona el CA Bundle de Mozilla en Python. Se usa para asegurar conexiones seguras.
- **charset-normalizer==3.4.0**: Una biblioteca para detectar y normalizar codificaciones de caracteres.
- **idna==3.10**: Implementa el estándar de Nombres de Dominio Internacionalizados en Aplicaciones (IDNA).
- **PyPDF2==3.0.1**: Una biblioteca para trabajar con archivos PDF. Se usa para verificar que los PDFs descargados contengan texto seleccionable.
- **requests==2.32.3**: Una biblioteca HTTP simple para Python. Se usa para realizar web scraping y descargar archivos.
- **soupsieve==2.6**: Una biblioteca de selectores CSS diseñada para ser usada con BeautifulSoup.
- **urllib3==2.2.3**: Un cliente HTTP potente y fácil de usar para Python.

### Requisitos del Sistema

Para ejecutar este proyecto, necesitas tener el siguiente software instalado en tu sistema:

- **Python 3.6 o superior**: El proyecto está escrito en Python, por lo que necesitas tener Python instalado para ejecutar los scripts.
- **pip**: El gestor de paquetes de Python, usado para instalar las dependencias requeridas.

### Instrucciones de Instalación

Sigue estos pasos para configurar el proyecto en tu máquina local.

#### Instalación Manual

1. **Clonar el Repositorio**:
   Primero, clona el repositorio desde GitHub a tu máquina local usando el siguiente comando:
   ```bash
   git clone https://github.com/rasexx/automatic-google-search.git
   cd automatic-google-search
   ```

2. **Crear y Activar un Entorno Virtual (Opcional)**:
   Se recomienda crear un entorno virtual para gestionar las dependencias del proyecto. Ejecuta los siguientes comandos para crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```

3. **Instalar las Dependencias**:
   Instala las dependencias requeridas listadas en el archivo `requirements.txt` usando pip:
   ```bash
   pip install -r requirements.txt
   ```

### Configuración Inicial del Entorno

1. **Navegar al Directorio del Proyecto**:
   Cambia al directorio `src` donde se encuentra el script principal:
   ```bash
   cd src
   ```

2. **Crear el Archivo de Consultas de Búsqueda**:
   Crea un archivo llamado `search_queries_input.txt` en el directorio `src`. Agrega tus consultas de búsqueda a este archivo, una por línea. Cada línea debe contener una consulta de búsqueda separada que el script usará para realizar búsquedas en Google.

### Archivos de Configuración y Variables de Entorno

- **requirements.txt**: Este archivo lista todas las dependencias requeridas para el proyecto. Asegura que todas las bibliotecas necesarias estén instaladas.
- **search_queries_input.txt**: Este archivo contiene las consultas de búsqueda que serán usadas por el script. Cada línea en el archivo representa una consulta de búsqueda separada.

### Configuración de Servicios Externos

No se configuran servicios externos para este proyecto. El script realiza web scraping usando la biblioteca `requests` y analiza HTML usando `BeautifulSoup`. Todas las operaciones se realizan localmente en tu máquina, y no se requieren APIs o servicios externos.

### Guía de Uso

Esta sección proporciona instrucciones detalladas sobre cómo usar la aplicación Auto PDF Downloader.

#### Ejemplos Prácticos

1. **Iniciar la Aplicación**:
   - Para iniciar la aplicación, navega al directorio `src` y ejecuta el script principal:
     ```bash
     python integrated_search_and_download_gui.py
     ```
   - Se abrirá la interfaz gráfica de usuario (GUI), permitiéndote iniciar el proceso de búsqueda y descarga.

2. **Agregar Consultas de Búsqueda**:
   - Abre el archivo `search_queries_input.txt` ubicado en el directorio `src`.
   - Agrega tus consultas de búsqueda al archivo, una por línea. Cada línea debe contener una consulta de búsqueda separada.
   - Guarda el archivo y regresa a la GUI para iniciar el proceso de búsqueda.

#### Interfaz de Usuario

La interfaz de usuario está diseñada para ser intuitiva y amigable. Incluye los siguientes componentes:

- **Ventana Principal**: La ventana principal proporciona opciones para iniciar el proceso de búsqueda y descarga.
- **Barras de Progreso**: Se muestran dos barras de progreso para indicar el progreso general y el progreso de la consulta de búsqueda actual.
- **Estado y Registros**: Un área de texto muestra el estado actual y los registros, proporcionando retroalimentación en tiempo real sobre el proceso de búsqueda y descarga.

### Guía de Contribución

Damos la bienvenida a las contribuciones al proyecto Auto PDF Downloader. Sigue estos pasos para contribuir:

1. **Hacer un Fork del Repositorio**:
   - Haz un fork del repositorio en GitHub para crear tu propia copia.

2. **Crear una Nueva Rama**:
   - Crea una nueva rama para tu característica o corrección de errores:
     ```bash
     git checkout -b nombre-de-la-caracteristica
     ```

3. **Realizar tus Cambios**:
   - Realiza tus cambios y haz commit con mensajes descriptivos:
     ```bash
     git commit -m "Descripción de los cambios"
     ```

4. **Subir tus Cambios**:
   - Sube tus cambios a tu fork:
     ```bash
     git push origin nombre-de-la-caracteristica
     ```

5. **Crear un Pull Request**:
   - Crea un pull request al repositorio principal, describiendo tus cambios y por qué deberían ser fusionados.

### Actualización y Solución de Problemas

Esta sección proporciona instrucciones para actualizar las dependencias y solucionar problemas comunes.

- **Actualizar Dependencias**:
  - Para actualizar las dependencias, ejecuta el siguiente comando:
    ```bash
    pip install --upgrade -r requirements.txt
    ```

- **Problemas Comunes**:
  - **Versión Incorrecta de Python**: Asegúrate de tener la versión correcta de Python instalada (Python 3.6 o superior).
  - **Problemas de Red**: Verifica tu conexión a internet si las descargas fallan.
  - **Consultas de Búsqueda Inválidas**: Verifica el formato del archivo `search_queries_input.txt`. Cada línea debe contener una consulta de búsqueda válida.

### Mejores Prácticas de Mantenimiento

Para asegurar que el proyecto se mantenga en buen estado, sigue estas mejores prácticas de mantenimiento:

- **Actualizar Regularmente las Dependencias**: Mantén las dependencias actualizadas para beneficiarte de las últimas características y correcciones de seguridad.
- **Monitorear los Registros**: Revisa regularmente los registros para detectar errores y solucionarlos rápidamente.
- **Actualizar la Documentación**: Mantén la documentación actualizada con cualquier cambio en el proyecto.

### Documentación de APIs y Bibliotecas

Consulta la siguiente documentación para las bibliotecas usadas en este proyecto:

- **requests**: [Documentación de Requests](https://docs.python-requests.org/en/latest/)
- **BeautifulSoup**: [Documentación de BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- **PyPDF2**: [Documentación de PyPDF2](https://pypdf2.readthedocs.io/en/latest/)

### Recursos Adicionales

Para más información y recursos, consulta los siguientes enlaces:

- [Documentación Oficial de Python](https://docs.python.org/3/)
- [Guías de GitHub](https://guides.github.com/)

---

# Auto PDF Downloader

![imagen](image.png)

# Auto PDF Downloader

## Technical Documentation

### Author

**Jose Ramon Garcia Del Risco**

### Project Title

**Auto PDF Downloader**

### Date

**October 2023**

---

### Project Overview

This project is designed to automate the process of searching for PDF documents on Google, downloading them, and verifying that they contain selectable text. The tool is particularly useful for researchers who need to gather a large number of documents quickly and efficiently. By automating the search and download process, the tool saves time and ensures that the documents collected are in a usable format.

The application features a graphical user interface (GUI) that allows users to monitor the progress of the search and download process in real-time. The GUI provides visual feedback on the status of each search query and the download progress of each PDF file.

### Objectives and Scope

The main objectives of this project are:
- **Automate Google Searches**: The tool performs automated searches on Google based on user-provided search queries.
- **Download PDFs**: It downloads the PDF files found in the search results.
- **Verify PDF Content**: The tool checks that the downloaded PDFs contain selectable text, ensuring they are not just scanned images.
- **User-Friendly GUI**: A graphical user interface is provided to allow users to easily start the search and download process and monitor its progress.

The scope of this project includes:
- **Web Scraping**: Using the `requests` library to perform web scraping.
- **HTML Parsing**: Utilizing `BeautifulSoup` to parse HTML content and extract relevant information.
- **File Downloading**: Downloading files using HTTP requests.
- **PDF Verification**: Using `PyPDF2` to verify the content of the downloaded PDFs.
- **GUI Development**: Creating a user-friendly interface using `tkinter`.

### Modules and Components

- **integrated_search_and_download_gui.py**: This is the main script that integrates the GUI with the search and download functionalities. It handles user inputs, performs Google searches, downloads PDFs, and verifies their content.
- **requirements.txt**: This file lists all the dependencies required for the project, ensuring that all necessary libraries are installed.
- **README.md**: Provides an overview of the project, including installation instructions and usage guidelines.
- **LICENSE**: Contains the licensing information for the project, specifying the terms under which the project can be used and distributed.
- **.gitignore**: Specifies files and directories that should be ignored by Git, preventing them from being included in version control.

### File and Directory Organization

- **/src**: This directory contains the main script and the directory for storing search results.
  - **integrated_search_and_download_gui.py**: The main script that handles the core functionalities of the project.
  - **search_results**: A directory where the downloaded PDFs are stored. Each search query results in a subdirectory containing the corresponding PDFs.
- **/docs**: This directory contains documentation files.
  - **README.md**: Provides an overview of the project and usage instructions.
  - **LICENSE**: Contains the licensing information for the project.
  - **TECHNICAL_DOCUMENTATION.md**: This file, which provides detailed technical documentation for the project.
- **requirements.txt**: Lists all the dependencies required for the project, ensuring that all necessary libraries are installed.
- **.gitignore**: Specifies files and directories to be ignored by Git, preventing them from being included in version control.

### Dependencies

This project relies on several Python libraries to perform its tasks. The dependencies are listed in the `requirements.txt` file and include:

- **beautifulsoup4==4.12.3**: A library for parsing HTML and XML documents. It is used to extract data from web pages.
- **certifi==2024.8.30**: Provides Mozilla's CA Bundle in Python. It is used to ensure secure connections.
- **charset-normalizer==3.4.0**: A library for detecting and normalizing character encodings.
- **idna==3.10**: Implements the Internationalized Domain Names in Applications (IDNA) standard.
- **PyPDF2==3.0.1**: A library for working with PDF files. It is used to verify that the downloaded PDFs contain selectable text.
- **requests==2.32.3**: A simple HTTP library for Python. It is used to perform web scraping and download files.
- **soupsieve==2.6**: A CSS selector library designed to be used with BeautifulSoup.
- **urllib3==2.2.3**: A powerful, user-friendly HTTP client for Python.

### System Requirements

To run this project, you need to have the following software installed on your system:

- **Python 3.6 or higher**: The project is written in Python, so you need Python installed to run the scripts.
- **pip**: The Python package manager, used to install the required dependencies.

### Installation Instructions

Follow these steps to set up the project on your local machine.

#### Manual Installation

1. **Clone the Repository**:
   First, clone the repository from GitHub to your local machine using the following command:
   ```bash
   git clone https://github.com/rasexx/automatic-google-search.git
   cd automatic-google-search
   ```

2. **Create and Activate a Virtual Environment (Optional)**:
   It is recommended to create a virtual environment to manage the project dependencies. Run the following commands to create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the Dependencies**:
   Install the required dependencies listed in the `requirements.txt` file using pip:
   ```bash
   pip install -r requirements.txt
   ```

### Initial Environment Setup

1. **Navigate to the Project Directory**:
   Change to the `src` directory where the main script is located:
   ```bash
   cd src
   ```

2. **Create the Search Queries File**:
   Create a file named `search_queries_input.txt` in the `src` directory. Add your search queries to this file, one per line. Each line should contain a separate search query that the script will use to perform Google searches.

### Configuration Files and Environment Variables

- **requirements.txt**: This file lists all the dependencies required for the project. It ensures that all necessary libraries are installed.
- **search_queries_input.txt**: This file contains the search queries to be used by the script. Each line in the file represents a separate search query.

### External Services Configuration

No external services are configured for this project. The script performs web scraping using the `requests` library and parses HTML using `BeautifulSoup`. All operations are performed locally on your machine, and no external APIs or services are required.

### Usage Guide

This section provides detailed instructions on how to use the Auto PDF Downloader application.

#### Practical Examples

1. **Starting the Application**:
   - To start the application, navigate to the `src` directory and run the main script:
     ```bash
     python integrated_search_and_download_gui.py
     ```
   - The graphical user interface (GUI) will open, allowing you to start the search and download process.

2. **Adding Search Queries**:
   - Open the `search_queries_input.txt` file located in the `src` directory.
   - Add your search queries to the file, one per line. Each line should contain a separate search query.
   - Save the file and return to the GUI to start the search process.

#### User Interface

The user interface is designed to be intuitive and user-friendly. It includes the following components:

- **Main Window**: The main window provides options to start the search and download process.
- **Progress Bars**: Two progress bars are displayed to show the overall progress and the progress of the current search query.
- **Status and Logs**: A text area displays the current status and logs, providing real-time feedback on the search and download process.

### Contribution Guide

We welcome contributions to the Auto PDF Downloader project. Follow these steps to contribute:

1. **Fork the Repository**:
   - Fork the repository on GitHub to create your own copy.

2. **Create a New Branch**:
   - Create a new branch for your feature or bugfix:
     ```bash
     git checkout -b feature-name
     ```

3. **Make Your Changes**:
   - Make your changes and commit them with descriptive messages:
     ```bash
     git commit -m "Description of the changes"
     ```

4. **Push Your Changes**:
   - Push your changes to your fork:
     ```bash
     git push origin feature-name
     ```

5. **Create a Pull Request**:
   - Create a pull request to the main repository, describing your changes and why they should be merged.

### Update and Troubleshooting

This section provides instructions for updating dependencies and troubleshooting common issues.

- **Updating Dependencies**:
  - To update the dependencies, run the following command:
    ```bash
    pip install --upgrade -r requirements.txt
    ```

- **Common Issues**:
  - **Incorrect Python Version**: Ensure you have the correct Python version installed (Python 3.6 or higher).
  - **Network Issues**: Check your internet connection if downloads fail.
  - **Invalid Search Queries**: Verify the format of the `search_queries_input.txt` file. Each line should contain a valid search query.

### Maintenance Best Practices

To ensure the project remains in good condition, follow these maintenance best practices:

- **Regularly Update Dependencies**: Keep the dependencies up to date to benefit from the latest features and security fixes.
- **Monitor Logs**: Regularly check the logs for errors and address them promptly.
- **Update Documentation**: Keep the documentation up to date with any changes to the project.

### API and Library Documentation

Refer to the following documentation for the libraries used in this project:

- **requests**: [Requests Documentation](https://docs.python-requests.org/en/latest/)
- **BeautifulSoup**: [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- **PyPDF2**: [PyPDF2 Documentation](https://pypdf2.readthedocs.io/en/latest/)

### Additional Resources

For further information and resources, refer to the following links:

- [Python Official Documentation](https://docs.python.org/3/)
- [GitHub Guides](https://guides.github.com/)
