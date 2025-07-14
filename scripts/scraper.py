import requests
import pandas as pd

def fetch_data():
    url = "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"
    df = pd.read_csv(url)
    df.to_csv("data/raw_data/population.csv", index=False)
    print("Datos descargados correctamente.")

if __name__ == "__main__":
    fetch_data()

