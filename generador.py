import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()

# Constants
NUM_PUBLICACIONES = 500    
NUM_USUARIOS = 150

# Generate publicaciones 
publicaciones_data = {
    "ID_Publicacion": range(1, NUM_PUBLICACIONES + 1),
    "Fecha": [fake.date_between(start_date='-1y',end_date='today') for _ in range(NUM_PUBLICACIONES)],
    "Contenido": [fake.sentence(nb_words=4) for _ in range(NUM_PUBLICACIONES)],
    "Likes": [random.randint(0, 500) for _ in range(NUM_PUBLICACIONES)],
    "Comentarios": [random.randint(0, 100) for _ in range(NUM_PUBLICACIONES)],
    "Compartidos": [random.randint(0, 50) if random.random() > 0.08 else "NULL" for _ in range(NUM_PUBLICACIONES)]
}

# Convertir en dataframe :v
publicaciones_df = pd.DataFrame(publicaciones_data)

# Generate usuarios 
usuarios_data = {
    "ID_Usuario": range(1, NUM_USUARIOS + 1),
    "Edad": [random.randint(18, 70) for _ in range(NUM_USUARIOS)],
    "Genero": [random.choice(['Masculino', 'Femenino']) if random.random() > 0.05 else "NULL" for _ in range(NUM_USUARIOS)],
    "Ubicacion": [fake.city() for _ in range(NUM_USUARIOS)],
    "ID_Publicacion": [random.randint(1, NUM_PUBLICACIONES) for _ in range(NUM_USUARIOS)]
}

# Convertir en data frame :v
usuarios_df = pd.DataFrame(usuarios_data)

# Guardar el archivo csv :v
publicaciones_df.to_csv('publicaciones.csv', index=False)
usuarios_df.to_csv('usuarios.csv', index=False)

