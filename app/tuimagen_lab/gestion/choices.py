import os
import pandas as pd

# Obtener la ruta del archivo CSV
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path_dientes = os.path.join(BASE_DIR, 'gestion', 'data', 'piezas-dientes.csv')
file_path_materiales = os.path.join(BASE_DIR, 'gestion', 'data', 'materiales-dientes.csv')

# Cargar los archivos CSV
piezas_df = pd.read_csv(file_path_dientes)
materiales_df = pd.read_csv(file_path_materiales)

# Convertir los valores en una lista de tuplas
PIEZAS = [(str(row['num_dientes']), str(row['num_dientes'])) for index, row in piezas_df.iterrows()]
MATERIALES = [(str(row['materiales']), str(row['materiales'])) for index, row in materiales_df.iterrows()]