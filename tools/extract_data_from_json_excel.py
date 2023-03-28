import pandas as pd
df_json = pd.read_json('vie.json')
df_json.to_excel('Book1.xlsx')