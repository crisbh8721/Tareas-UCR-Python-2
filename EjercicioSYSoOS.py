#Ejercicio 1: Crear estructura de carpetas y archivos
#Objetivo: Automatizar la creación de carpetas y archivos temporales.

import os
base = "proyecto_demo"
subcarpetas = ["entrada","salida","temporal"]
if not os.path.exists(base):
    os.mkdir(base)
    print(f"Subcarpeta '{base}' creada.")

for sub in subcarpetas:
    ruta = os.path.join(base,sub)
    if not os.path.exists(ruta):
        os.mkdir(ruta)
        print(f"Subarpeta  '{sub}' creada")

#Crear archivos temporales
for i in range(3):
    ruta_archivo = os.path.join(base, "temporal", f"archivo{i}.tmp")
    with open(ruta_archivo, "w") as f:
        f.write("Este es un archivo temporal.\n")

#Ejercicio 2: Limpiar archivos temporales
#Objetivo: Usar os.listdir() y os.remove() para eliminar archivos .tmp

ruta_temporal = os.path.join("proyecto_demo", "temporal")

for archivo in os.listdir(ruta_temporal):
    if archivo.endswith(" .tmp"):
        ruta = os.path.join(ruta_temporal, archvo)
        os.remove(ruta)
        print(f"Elimiado: {archivo}")