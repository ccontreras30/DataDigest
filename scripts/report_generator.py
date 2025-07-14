import pandas as pd

def generate_report():
    df = pd.read_csv("data/processed_data/summary.csv")
    top5 = df.sort_values(by='Value', ascending=False).head(5)
    with open("output/reports/report.md", "w") as f:
        f.write("# Informe de Población Mundial 2020\n\n")
        f.write("## Top 5 países por población:\n\n")
        for _, row in top5.iterrows():
            f.write(f"- {row['Country Name']}: {int(row['Value']):,} habitantes\n")
    print("Informe generado.")

if __name__ == "__main__":
    generate_report()

