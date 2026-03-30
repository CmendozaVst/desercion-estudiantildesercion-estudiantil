# 📊 Dataset Sintético — Deserción Estudiantil

**Universidad de la Costa | Data Mining**  
**Actividad I: Aprendizaje Supervisado vs No Supervisado**

---

## 📁 Contenido del repositorio

| Archivo | Descripción |
|---|---|
| `dataset_desercion.csv` | Dataset sintético con 600 registros |
| `generar_dataset.py` | Código Python para reproducir el dataset |
| `README.md` | Documentación del dataset |

---

## 🎯 Descripción del problema

La Universidad está interesada en predecir, de manera temprana, qué estudiantes tienen mayor riesgo de abandonar sus estudios durante el primer año académico, con el fin de implementar estrategias de apoyo y retención.

El dataset simula información histórica de estudiantes de pregrado con variables demográficas, académicas y financieras.

---

## 📋 Descripción de las variables

| Variable | Tipo | Rango / Valores | Descripción |
|---|---|---|---|
| `id_estudiante` | Entero | 1001 – 1600 | Identificador único del estudiante |
| `edad` | Numérico continuo | 16 – 30 años | Edad al momento de ingresar |
| `genero` | Categórico | Masculino, Femenino, Otro | Género del estudiante |
| `ciudad_origen` | Categórico | 10 ciudades colombianas | Ciudad de procedencia |
| `promedio_colegio` | Numérico continuo | 1.0 – 5.0 | Promedio académico en bachillerato |
| `puntaje_admision` | Numérico continuo | 0 – 100 | Resultado de prueba de admisión |
| `promedio_semestre1` | Numérico continuo | 0.0 – 5.0 | Promedio académico del primer semestre |
| `nivel_socioeconomico` | Entero | 1 – 6 (estrato) | Estrato socioeconómico del estudiante |
| `beca` | Categórico | Si / No | Indica si el estudiante recibe beca |
| `credito_educativo` | Categórico | Si / No | Indica si tiene crédito o préstamo educativo |
| `desercion` | Categórico | **Si / No** | **Variable objetivo** — indica si el estudiante desertó |

---

## 🔢 Estadísticas generales

- **Total de registros:** 600
- **Variables:** 11 (10 predictoras + 1 objetivo)
- **Distribución de la variable objetivo:**
  - Desertó (Si): ≈ 189 estudiantes (31.5 %)
  - No desertó (No): ≈ 411 estudiantes (68.5 %)

---

## ❌ Valores nulos

Se introdujeron valores nulos de manera aleatoria en aproximadamente el **5 % de los registros** de las siguientes columnas numéricas, simulando datos incompletos o no reportados:

| Columna | Cantidad de nulos aprox. |
|---|---|
| `edad` | 30 |
| `promedio_colegio` | 30 |
| `puntaje_admision` | 29 |
| `promedio_semestre1` | 29 |
| `nivel_socioeconomico` | 30 |

**Método:** Para cada columna se seleccionaron índices aleatorios usando `numpy.random.choice` y se reemplazaron con `NaN`.

---

## ⚠️ Outliers (valores atípicos)

Se introdujeron deliberadamente valores atípicos en aproximadamente el **2 % de los registros** para simular errores de captura o casos extremos:

### Outliers altos (valores por encima del rango válido)

| Columna | Rango normal | Valores outlier | Cantidad |
|---|---|---|---|
| `promedio_semestre1` | 0.0 – 5.0 | 5.5 – 6.5 | 4 registros |
| `puntaje_admision` | 0 – 100 | 105 – 130 | 4 registros |

### Outliers bajos (valores por debajo del rango válido)

| Columna | Rango normal | Valores outlier | Cantidad |
|---|---|---|---|
| `promedio_semestre1` | 0.0 – 5.0 | -1.5 – -0.1 | 3 registros |
| `edad` | 16 – 30 | 5, 7, 9 | 3 registros |

**Método:** Se seleccionaron índices aleatorios y se asignaron valores fuera del rango esperado usando `numpy.random.uniform` y `numpy.random.choice`.

---

## 🤖 Modelo de Machine Learning propuesto

Para este problema se propone un modelo de **aprendizaje supervisado de clasificación binaria**, dado que:

- La variable objetivo (`desercion`) tiene dos categorías definidas: Si / No.
- Se cuenta con datos históricos etiquetados.
- El objetivo es predecir la clase de nuevos estudiantes.

**Modelo seleccionado:** Árbol de Decisión (Decision Tree) o Regresión Logística como línea base.

**Justificación:**
- Fácil interpretabilidad (el árbol muestra qué variables influyen más).
- Funciona bien con variables mixtas (numéricas y categóricas).
- Permite identificar factores de riesgo concretos para tomar decisiones de intervención.

---

## ▶️ Cómo reproducir el dataset

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu_usuario/desercion-estudiantil.git
cd desercion-estudiantil

# 2. Instalar dependencias
pip install pandas numpy

# 3. Ejecutar el generador
python generar_dataset.py

# → Se generará: dataset_desercion.csv
```

---

## 👥 Integrantes del grupo

| Nombre | 
|---|
| _(Agrega tu nombre aquí)_ |
| _(Agrega tu nombre aquí)_ |
| _(Agrega tu nombre aquí)_ |

---

## 📚 Referencias

- Pedregosa et al. (2011). *Scikit-learn: Machine Learning in Python*. JMLR 12.
- Tinto, V. (1987). *Leaving College: Rethinking the Causes and Cures of Student Attrition*. University of Chicago Press.
- McKinney, W. (2010). *Data Structures for Statistical Computing in Python*. SciPy.
