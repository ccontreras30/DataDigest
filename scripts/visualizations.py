import pandas as pd
import matplotlib.pyplot as plt

def generate_plot():
    df = pd.read_csv("data/processed_data/summary.csv")
    top10 = df.sort_values(by='Value', ascending=False).head(10)
    plt.figure(figsize=(10,6))
    plt.barh(top10['Country Name'], top10['Value'], color='skyblue')
    plt.xlabel("Población")
    plt.title("Top 10 países por población (2020)")
    plt.tight_layout()
    plt.savefig("docs/top10_population.png")
    print("Gráfico generado.")

if __name__ == "__main__":
    generate_plot()

