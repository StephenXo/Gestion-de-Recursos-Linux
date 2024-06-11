import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV limpio
df = pd.read_csv('recursos.csv',sep=',')

# Convertir la columna de tiempo a formato datetime
df['Tiempo'] = pd.to_datetime(df['Tiempo'], format='%H:%M:%S')

# Configurar la columna de tiempo como el índice
df.set_index('Tiempo', inplace=True)

# Graficar el uso de CPU y Memoria
plt.figure(figsize=(14, 7))

# Graficar uso de CPU
plt.subplot(2, 1, 1)
plt.plot(df.index, df['CPU(%)'], marker='o', linestyle='-', color='r')
plt.title('Uso de CPU (%)')
plt.xlabel('Tiempo')
plt.ylabel('CPU (%)')
plt.grid(True)

# Graficar uso de Memoria
plt.subplot(2, 1, 2)
plt.plot(df.index, df['Memoria(%)'], marker='o', linestyle='-', color='b')
plt.title('Uso de Memoria (%)')
plt.xlabel('Tiempo')
plt.ylabel('Memoria (%)')
plt.grid(True)

# Mostrar las gráficas
plt.tight_layout()
plt.show()

