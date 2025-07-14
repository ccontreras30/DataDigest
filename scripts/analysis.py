import pandas as pd

def analyze_data():
    df = pd.read_csv("data/raw_data/population.csv")
    df_filtered = df[df['Year'] == 2020]
    df_summary = df_filtered.groupby('Country Name')['Value'].sum().reset_index()
    df_summary.to_csv("data/processed_data/summary.csv", index=False)
    print("Análisis completado.")

if __name__ == "__main__":
    analyze_data()

