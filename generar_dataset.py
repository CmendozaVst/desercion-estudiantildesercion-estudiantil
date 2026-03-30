"""
=============================================================
 GENERADOR DE DATASET SINTÉTICO - DESERCIÓN ESTUDIANTIL
 Universidad de la Costa | Data Mining
 Actividad I: Aprendizaje Supervisado vs No Supervisado
=============================================================

Requisitos:
    pip install pandas numpy

Uso:
    python generar_dataset.py
    → Genera: dataset_desercion.csv
"""

import pandas as pd
import numpy as np

# Semilla para reproducibilidad
np.random.seed(42)
N = 600  # Número de registros (supera el mínimo de 500)

# =============================================================
# 1. VARIABLES DEMOGRÁFICAS
# =============================================================
edad = np.random.randint(16, 30, N).astype(float)

genero = np.random.choice(
    ['Masculino', 'Femenino', 'Otro'],
    N, p=[0.48, 0.49, 0.03]
)

ciudad_origen = np.random.choice(
    ['Barranquilla', 'Bogotá', 'Medellín', 'Cartagena', 'Santa Marta',
     'Montería', 'Sincelejo', 'Valledupar', 'Bucaramanga', 'Cali'],
    N, p=[0.25, 0.18, 0.12, 0.10, 0.08, 0.07, 0.07, 0.05, 0.04, 0.04]
)

# =============================================================
# 2. VARIABLES ACADÉMICAS
# =============================================================
promedio_colegio    = np.round(np.random.normal(3.5, 0.6, N).clip(1.0, 5.0), 2)
puntaje_admision    = np.round(np.random.normal(55, 12, N).clip(0, 100), 1)
promedio_semestre1  = np.round(np.random.normal(3.2, 0.8, N).clip(0.0, 5.0), 2)

# =============================================================
# 3. VARIABLES FINANCIERAS
# =============================================================
nivel_socioeconomico = np.random.choice(
    [1, 2, 3, 4, 5, 6],
    N, p=[0.15, 0.25, 0.28, 0.18, 0.09, 0.05]
)
beca              = np.random.choice(['Si', 'No'], N, p=[0.30, 0.70])
credito_educativo = np.random.choice(['Si', 'No'], N, p=[0.35, 0.65])

# =============================================================
# 4. VARIABLE OBJETIVO: DESERCIÓN (Si / No)
#    Se calcula con una probabilidad que refleja factores de riesgo
#    reales: bajo rendimiento, estrato bajo, sin apoyo financiero.
# =============================================================
prob_desercion = (
    0.30
    - 0.08 * (promedio_semestre1 - 3.2)
    - 0.05 * (promedio_colegio - 3.5)
    - 0.06 * (puntaje_admision - 55) / 12
    + 0.07 * (nivel_socioeconomico <= 2).astype(float)
    - 0.06 * (beca == 'Si').astype(float)
    - 0.04 * (credito_educativo == 'Si').astype(float)
)
prob_desercion = prob_desercion.clip(0.05, 0.95)
desercion = np.where(np.random.rand(N) < prob_desercion, 'Si', 'No')

# =============================================================
# 5. CONSTRUIR DATAFRAME
# =============================================================
df = pd.DataFrame({
    'id_estudiante'      : range(1001, 1001 + N),
    'edad'               : edad,
    'genero'             : genero,
    'ciudad_origen'      : ciudad_origen,
    'promedio_colegio'   : promedio_colegio,
    'puntaje_admision'   : puntaje_admision,
    'promedio_semestre1' : promedio_semestre1,
    'nivel_socioeconomico': nivel_socioeconomico,
    'beca'               : beca,
    'credito_educativo'  : credito_educativo,
    'desercion'          : desercion
})

# =============================================================
# 6. INTRODUCIR VALORES NULOS (~5% por columna numérica)
# =============================================================
cols_nulos = [
    'edad', 'promedio_colegio', 'puntaje_admision',
    'promedio_semestre1', 'nivel_socioeconomico'
]
for col in cols_nulos:
    idx_nulos = np.random.choice(df.index, size=int(0.05 * N), replace=False)
    df.loc[idx_nulos, col] = np.nan

# =============================================================
# 7. INTRODUCIR OUTLIERS (~2%)
#    Outliers altos: valores que superan el rango válido de la escala
#    Outliers bajos: valores negativos o edades imposibles
# =============================================================

# Outliers ALTOS
idx_out_alto = np.random.choice(df.index, size=8, replace=False)
df.loc[idx_out_alto[:4], 'promedio_semestre1'] = np.round(
    np.random.uniform(5.5, 6.5, 4), 2   # Escala máxima es 5.0
)
df.loc[idx_out_alto[4:], 'puntaje_admision'] = np.round(
    np.random.uniform(105, 130, 4), 1   # Escala máxima es 100
)

# Outliers BAJOS
idx_out_bajo = np.random.choice(df.index, size=6, replace=False)
df.loc[idx_out_bajo[:3], 'promedio_semestre1'] = np.round(
    np.random.uniform(-1.5, -0.1, 3), 2  # Valores negativos
)
df.loc[idx_out_bajo[3:], 'edad'] = np.random.choice([5, 7, 9], 3)  # Edades imposibles

# =============================================================
# 8. GUARDAR CSV
# =============================================================
output_path = 'dataset_desercion.csv'
df.to_csv(output_path, index=False)

print("=" * 55)
print("  Dataset generado correctamente")
print("=" * 55)
print(f"  Archivo      : {output_path}")
print(f"  Registros    : {len(df)}")
print(f"  Columnas     : {len(df.columns)}")
print(f"  Deserción Si : {(df['desercion'] == 'Si').sum()}")
print(f"  Deserción No : {(df['desercion'] == 'No').sum()}")
print(f"\n  Valores nulos por columna:")
for col, cnt in df.isnull().sum().items():
    if cnt > 0:
        print(f"    {col:<25}: {cnt}")
print("=" * 55)
