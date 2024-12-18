

### **README.md**

```markdown
# Proyecto de Estadísticas y Visualización con Seaborn y Matplotlib 🐍📊

Este proyecto tiene como objetivo calcular variables estadísticas y generar visualizaciones de un conjunto de datos temático de colegio utilizando **Python**, **Pandas**, **Seaborn** y **Matplotlib**.

---

## 📋 **Requisitos**

1. **Python 3.8 o superior**
2. **Librerías necesarias**:
   - Pandas
   - Matplotlib
   - Seaborn

---

## ⚙️ **Instalación**

### 1. Instalar Python
Asegúrate de tener Python instalado. Descárgalo desde [python.org](https://www.python.org/).

### 2. Instalar librerías requeridas
Ejecuta los siguientes comandos en tu terminal:

```bash
pip install pandas matplotlib seaborn
```

Si usas **Anaconda**, puedes instalar las librerías con:

```bash
conda install pandas matplotlib seaborn
```

---

## 🗂 **Cargar el Dataset**

El archivo **"datos.csv"** contiene información sobre estudiantes:

- **Nombre**: Nombre del estudiante  
- **Grado**: Nivel del estudiante (ej. 7°, 8°, 9°)  
- **Nota Final**: Calificación promedio  
- **Faltas**: Número de inasistencias  
- **Estado**: Aprobado o Desaprobado  

Formato del dataset:

```csv
Nombre,Grado,Nota Final,Faltas,Estado
Juan Pérez,9°,85,2,Aprobado
María González,10°,92,0,Aprobado
Pedro Sánchez,8°,67,5,Desaprobado
```

---

## 📊 **Cálculos Estadísticos**

El programa calcula las siguientes variables estadísticas:

### 1. Tendencia Central:
   - **Media**  
   - **Mediana**  
   - **Moda**

### 2. Dispersión:
   - **Varianza**  
   - **Desviación Estándar**

---

## 📈 **Visualizaciones Generadas**

El programa utiliza **Seaborn** y **Matplotlib** para generar:

- 📊 **Gráfico de Barras**: Comparar notas o faltas por estudiante  
- 📉 **Gráfico de Líneas**: Mostrar tendencias en notas  
- 🥧 **Gráfico de Pastel**: Distribución del estado (Aprobado/Desaprobado)  
- 📈 **Histograma**: Distribución de notas finales  

---

## 🚀 **Uso del Proyecto**

1. Clona el repositorio:

   ```bash
   git clone https://github.com/JuanJoseBastoGonzalez/taller-python
   cd proyecto-estadisticas
   ```

2. Asegúrate de tener **Seaborn** y **Pandas** instalados.

3. Ejecuta el script:

   ```bash
   python main.py
   ```

---

## 🔍 **Ejemplo de Código**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('datos.csv')

# Calcular estadísticas
media = df['Nota Final'].mean()
mediana = df['Nota Final'].median()
moda = df['Nota Final'].mode()[0]

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(x='Nombre', y='Nota Final', data=df, palette='viridis')
plt.xticks(rotation=45)
plt.title("Notas Finales por Estudiante")
plt.show()
```

---

## 📧 **Contacto**

Si tienes preguntas o sugerencias, no dudes en contactarme:

- **Nombre**: Juan José  
- **Email**: juanjosebasto79@example.com  
- **LinkedIn**: [Mi Perfil](https://www.linkedin.com/in/juan-jose-basto-gonzalez-49945023a/)  

---

### 🛠 **Tecnologías Utilizadas**
- Python
- Pandas
- Matplotlib
- Seaborn
