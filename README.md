# Análisis Exploratorio de Datos de Vehículos

Este proyecto realiza un análisis exploratorio de datos (EDA) sobre un conjunto de datos de anuncios de venta de coches. La aplicación web está construida con **Streamlit** y desplegada en **Render**.

## Funcionalidades
- **Visualización de histogramas**: Permite explorar la distribución de variables numéricas, como el odómetro.
- **Gráficos de dispersión**: Facilita el análisis de relaciones entre variables, como el precio vs. el año del vehículo.
- **Interactividad**: Los gráficos son interactivos, lo que permite a los usuarios explorar los datos de manera dinámica.

## Cómo usar la aplicación
1. Accede a la aplicación desplegada en Render: [Enlace a la aplicación](http://34.213.214.55:8501).
2. Explora los datos utilizando los botones para generar histogramas y gráficos de dispersión.

## Estructura del proyecto
- **`vehicles_us.csv`**: Conjunto de datos de anuncios de vehículos.
- **`app.py`**: Archivo principal de la aplicación Streamlit.
- **`notebooks/EDA.ipynb`**: Notebook de Jupyter con el análisis exploratorio de datos.
- **`requirements.txt`**: Lista de dependencias necesarias para ejecutar el proyecto.
- **`.gitignore`**: Archivo que excluye archivos innecesarios del control de versiones.

## Instalación y ejecución local
Si deseas ejecutar la aplicación en tu máquina local, sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/javierIqm/vehicles-analysis.git

2. Navega al directio del proyecto  
    cd vehicles-analysis

3. Crea y activa un entorno virtual:
    * python -m venv vehicles_env
    * Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
    * \vehicles_env\Scripts\activate

4. Instalas las dependencias     
    * pip install -r requirements.txt

5. Ejecuta la aplicación:
    streamlit run app.py


## Enlace a la aplicación en Render
Puedes acceder a la aplicación web desplegada en Render a través del siguiente enlace:
[https://vehicles-analysis-1ynd.onrender.com](https://vehicles-analysis-1ynd.onrender.com)
