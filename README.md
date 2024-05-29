# Proyecto de Predicción de Precios de Viviendas en California

Este proyecto es una solución a un problema planteado por Kaggle, desarrollado como parte del curso  de "Topicos Avanzados en Software" De la universidad de Cartagena.

Puedes revisar el análisis exploratorio de los Datos en: [Google Colab](https://colab.research.google.com/drive/154LH2L0mE58gyZHrKbv-rr0B4JkgaN4B?usp=sharing)

También puedes ver una demostración del código en: [demo en Streamlit](https://antojose93-house-price-california-main-xygz1i.streamlit.app/)

Para ver el problema completo visita:[Kaggle](https://www.kaggle.com/datasets/shibumohapatra/house-price/data)

## Descripción

La Oficina del Censo de los Estados Unidos ha publicado los Datos del Censo de California, que constan de 10 tipos de métricas como la población, ingreso medio, precio medio de la vivienda, entre otros, para cada grupo de manzanas en California. El conjunto de datos también sirve como entrada para la delineación del proyecto e intenta especificar los requisitos funcionales y no funcionales para el mismo.

**Objetivo del Problema**: El proyecto tiene como objetivo construir un modelo de precios de viviendas para predecir los valores medios de las casas en California utilizando el conjunto de datos proporcionado. Este modelo debería aprender de los datos y ser capaz de predecir el precio medio de la vivienda en cualquier distrito, dado el resto de las métricas.

Los grupos de manzanas o distritos son las unidades geográficas más pequeñas para las cuales la Oficina del Censo de los Estados Unidos publica datos de muestra (un grupo de manzanas típicamente tiene una población de 600 a 3,000 personas). Hay 20,640 distritos en el conjunto de datos del proyecto.



**Tareas de Análisis**:
1. Construir un modelo de precios de viviendas para predecir los valores medios de las casas en California utilizando el conjunto de datos proporcionado.
2. Entrenar el modelo para aprender de los datos y predecir el precio mediano de la vivienda en cualquier distrito, dado el resto de las métricas.
3. Predecir precios de viviendas basados en el ingreso medio y graficar el diagrama de regresión para ello.

Para ejecutarlo en producción, clona este repositorio, luego ejecuta `pip install -r requirements.txt` y para iniciar, ejecuta `streamlit run main.py`.

## Dependencias

El proyecto depende de las siguientes librerías:
- pandas
- scikit-learn
- seaborn
- numpy
- streamlit

Puedes instalar estas dependencias ejecutando `pip install -r requirements.txt`.

## Uso

Para utilizar el proyecto, sigue estos pasos:
1. Clona este repositorio.
2. Instala las dependencias ejecutando `pip install -r requirements.txt`.
3. Ejecuta el proyecto utilizando Streamlit ejecutando `streamlit run main.py`.



- Antonio Hurtado - Desarrollador


<p align="left"> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a> <a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="40" height="40"/> </a> </p>
