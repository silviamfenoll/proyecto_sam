import sys 
from rich import print

sam_file = sys.argv[1] #define la variable

total_reads = 0
mapq_60 = 0

with open(sam_file, "r") as f: #with open cierra el archivo tras ejecutarse
    for line in f: 
        if line.startswith("@"):
            continue #salta estas líneas porque se corresponden con los headers
        else:
            total_reads += 1

            wline = line.rstrip() #quita los espacios a la derecha("r")
            lista = wline.split("\t") #separa por columnas con tabuladores
            mapq = int(lista[4]) #define mapq como los números enteros (int) de la columna 5

            if mapq == 60:
                mapq_60 += 1

percentage = (mapq_60 / total_reads) * 100

print(f"[bold blue]Total de lecturas alineadas:[/bold blue] {total_reads}")
print(f"[bold green]Lecturas con MAPQ = 60:[/bold green] {mapq_60}")
print(f"[bold yellow]Porcentaje:[/bold yellow] {percentage:.1f}%")


