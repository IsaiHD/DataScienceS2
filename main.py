import generador
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def limpieza(publicaciones_df,usuarios_df):
    publicaciones_df.replace("NULL", np.nan, inplace=True)
    usuarios_df.replace("NULL", np.nan, inplace=True)

    publicaciones_df.dropna(inplace=True)
    usuarios_df.dropna(inplace=True)

    publicaciones_df["Fecha"] = pd.to_datetime(publicaciones_df["Fecha"])
    
    usuarios_df['Genero'] = usuarios_df['Genero'].astype('category')

    return publicaciones_df,usuarios_df


def fucionarDataFrames(publicaciones_df,usuarios_df):
    fucion_dfs = publicaciones_df.merge(usuarios_df, left_on='ID_Publicacion', right_on='ID_Publicacion', how='inner')
    fucion_dfs.to_csv('fucion_dfs.csv', index=False)
    return fucion_dfs

def calcularPromediosPublicaciones(publicaciones_df):
    colLikes = publicaciones_df['Likes']
    colComentarios = publicaciones_df['Comentarios']
    colCompartidos = publicaciones_df['Compartidos']

    promedioLikes = colLikes.mean()
    promedioComentarios = colComentarios.mean()
    promedioCompartidos = colCompartidos.mean()

    return promedioLikes,promedioComentarios,promedioCompartidos

def calcularEngagement(fucion_dfs):
    fucion_dfs['Engagement'] = fucion_dfs['Likes'] + fucion_dfs['Comentarios'] + fucion_dfs['Compartidos']

    engagement_promedio = fucion_dfs.groupby(['Genero', pd.cut(fucion_dfs['Edad'], [18, 25, 35, 45, float('inf')])]) \
                                    ['Engagement'].mean()
    
    return engagement_promedio

def identificarMayorYMenorEngagement(fucion_dfs):

    mayor_engagement = fucion_dfs.sort_values(by='Engagement', ascending=False).head(5)

    menor_engagement = fucion_dfs.sort_values(by='Engagement', ascending=True).head(5)

    return mayor_engagement, menor_engagement

def visualizar_distribucion_engagement_por_ubicacion(fucion_dfs):
    # Crear el gráfico de barras
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Ubicacion', y='Engagement', data=fucion_dfs, estimator=np.mean, ci=None)
    plt.title('Distribución de Engagement por Ubicación Geográfica de los Usuarios')
    plt.xlabel('Ubicación')
    plt.ylabel('Engagement Promedio')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def main():
    publicaciones_df,usuarios_df = generador.publicaciones_df,generador.usuarios_df

    publicaciones_df,usuarios_df = limpieza(publicaciones_df,usuarios_df)

    publicaciones_df.to_csv('publicaciones.csv', index=False)
    usuarios_df.to_csv('usuarios.csv', index=False)

    fucionarDataFrames(publicaciones_df,usuarios_df)
    
    fusion_dfs = fucionarDataFrames(publicaciones_df,usuarios_df)  # Guardar el resultado en una variable    
    promedioLikes, promedioComentarios, promedioCompartidos = calcularPromediosPublicaciones(publicaciones_df)
    print("\nPromedios de Publicaciones:\n")
    print("Promedio de likes: ",promedioLikes)
    print("Promedio de comentarios: ",promedioComentarios)
    print("Promedio de compartidos: ",promedioCompartidos)

    print("\n\n")
    engagement_promedio = calcularEngagement(fusion_dfs)

    engagement_promedio.to_csv('engagement_promedio.csv')

    mayor_engagement, menor_engagement = identificarMayorYMenorEngagement(fusion_dfs)    
    print("\nEngagement Promedio por Género y Rango de Edad:\n")
    print(engagement_promedio)

    print("\nPublicaciones con mayor engagement:")
    print(mayor_engagement)

    print("\nPublicaciones con menor engagement:")
    print(menor_engagement)

    visualizar_distribucion_engagement_por_ubicacion(fusion_dfs)



    
    # Si quieres ver los datos de los archivos csv descomenta las siguientes lineas, como no lo pide
    # en la pauta, no es necesario mostrarlos
    #print("\nDATA FRAME PUBLICACIONES.\n\n")
    #print(publicaciones_df)
    
    #print("\n\nDATA FRAME USUARIOS.\n\n\n")
    #print(usuarios_df) 


if __name__ == "__main__":
    main()