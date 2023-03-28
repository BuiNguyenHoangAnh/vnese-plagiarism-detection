
import pandas as pd 

df=pd.read_csv("Book1.csv",sep=",")
i=0

for index in range(len(df)):
   #   with open(df["valueID"][index] +  '.txt', 'w', encoding='utf-8') as output:
   with open('doc' + str(i) +  '.txt', 'w', encoding = 'utf-8') as output:
      output.write(df['content'][index])
      i+=1