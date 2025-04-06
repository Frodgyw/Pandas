import pandas as pd
import openpyxl


df = pd.read_csv('1.csv')
print(df)

dict_s = {"City": ["Симферополь", "Ялта", "Балаклава", "Евпатория", "Судак", "Феодосия", "Гурзуф", "Алушта"],
          "IndexCity": [126780, 539806, 162563, 162345, 174316, 161876, 161233, 165444]}
df = pd.DataFrame(dict_s)
print(df)

df.to_csv('1.csv', encoding='utf-8-sig')
df.to_excel('1.xls', sheet_name='2', engine='openpyxl', index=False)


