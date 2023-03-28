# Importing dependencies 
import pandas as pd 

# Reading xlsx into pandas dataframe
df=pd.read_csv("articles1.csv",sep=",", encoding = 'latin-1')
df.to_json('data.json')
# # Encoding/decoding a Dataframe using 'columns' formatted JSON
# jsonfile = df.to_json(orient='columns')

# # Print out the result
# print('Excel Sheet to JSON:\n', jsonfile)

# # Make the string into a list to be able to input in to a JSON-file
# json_dict = json.loads(jsonfile)

# # write from and file to write to
# with open('data.json', 'w') as json_file:
#     json.dump(json_dict, json_file)