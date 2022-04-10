import csv
import pandas as pd


data_xlsx = pd.read_excel('data.xlsx')
data = pd.DataFrame(data_xlsx).to_dict(orient='records')
print(data)

with open('data_csv.csv', 'w') as fd:
    fieldnames = ['name', 'type', 'owner']
    wr = csv.DictWriter(fd, fieldnames=fieldnames)
    wr.writeheader()
    wr.writerows(data)
