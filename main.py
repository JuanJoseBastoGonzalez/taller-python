import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
try:
    df = pd.read_csv("colegio.csv")
except FileNotFoundError:
    print("Error: El archivo 'colegio.csv' no fue encontrado")
    exit()

# Calculate central tendency and dispersion statistics
try:
    media_nota = df["Nota Final"].mean()
    mediana_nota = df["Nota Final"].median()
    moda_nota = df["Nota Final"].mode()[0]
    varianza_nota = df["Nota Final"].var()
    desviacion_nota = df["Nota Final"].std()

    # Display statistical results
    print("\nEstadísticas de las Notas:")
    print(f"Media: {media_nota:.2f}")
    print(f"Mediana: {mediana_nota:.2f}")
    print(f"Moda: {moda_nota:.2f}")
    print(f"Varianza: {varianza_nota:.2f}")
    print(f"Desviación Estándar: {desviacion_nota:.2f}")

    # Create visualizations
    # 1. Bar plot - Grades by student
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Nombre", y="Nota Final", data=df, palette="viridis")
    plt.xticks(rotation=45, ha='right')
    plt.title("Notas Finales por Estudiante")
    plt.tight_layout()
    plt.show()

    # 2. Line plot - Absences by grade
    plt.figure(figsize=(10, 5))
    faltas_por_grado = df.groupby("Grado")["Faltas"].sum().reset_index()
    plt.plot(faltas_por_grado["Grado"], faltas_por_grado["Faltas"], 
             marker='o', linestyle='-', color='blue', linewidth=2)
    plt.title("Faltas por Grado")
    plt.xlabel("Grado")
    plt.ylabel("Total Faltas")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # 3. Pie chart - Approval status
    plt.figure(figsize=(8, 8))
    estado_count = df["Estado"].value_counts()
    colors = ["#4CAF50", "#FF5733"]
    plt.pie(estado_count, labels=estado_count.index, autopct='%1.1f%%', 
            colors=colors, shadow=True, startangle=90)
    plt.title("Distribución de Aprobados y Desaprobados")
    plt.axis('equal')
    plt.show()

    # 4. Histogram - Final grades distribution
    plt.figure(figsize=(10, 6))
    plt.hist(df["Nota Final"], bins=15, color='skyblue', 
             edgecolor='black', alpha=0.7)
    plt.title("Distribución de Notas Finales")
    plt.xlabel("Notas")
    plt.ylabel("Frecuencia")
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

except KeyError as e:
    print(f"Error: La columna {e} no existe en el archivo CSV")
except Exception as e:
    print(f"Error inesperado: {e}")