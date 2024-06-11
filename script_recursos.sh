#!/bin/bash

# Verifica que el usuario haya ingresado el parámetro N
if [ -z "$1" ]; then
    echo "Por favor, proporcione el intervalo de tiempo en segundos (N) como parámetro."
    exit 1
fi

INTERVAL=$1

# Crea el archivo CSV y añade los encabezados
echo "Tiempo,CPU(%),Memoria(%)" > recursos.csv

# Bucle para capturar las estadísticas cada N segundos
while true; do
    TIMESTAMP=$(date "+%H:%M:%S")
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
    MEM_USAGE=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
    echo "$TIMESTAMP,$CPU_USAGE,$MEM_USAGE" >> recursos.csv
    sleep $INTERVAL
done
