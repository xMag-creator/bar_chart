from sys import exit


try:
    import pandas as pd
    print("pandas module loaded")
except:
    print("No such module like pandas")
    exit(0)

source_data = "dane_opady_temperatura.ods"
print(f"source data {source_data}")

df = pd.read_excel(source_data, engine="odf")

print("----[ Info about source data ]------")
print(df)
print("-----------------------------")

df["Autor"] = "Adam Jurkiewicz"
print("----[ Info about source data ]------")
print(df)

df.to_excel("ane_opady_temperatura_nowy.ods", engine="odf")
df.to_excel("ane_opady_temperatura_nowy.xlsx", engine="openpyxl")
