import csv
from pathlib import Path

def ler_csv() -> None:
    arquivo_csv = open('editoras.csv')
    csv_reader = csv.reader(arquivo_csv, delimiter=',')
    for linha in csv_reader:
        print(linha)
    arquivo_csv.close()


if __name__ == '__main__':
    ler_csv()
