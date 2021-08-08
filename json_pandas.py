# *******************************Json Read using pandas library*********************************************

# /////json-------------java Script Object notation
# ////importing libraries
import json
import pandas as pd

# /////if we read the json file with in the project than we use these steps as following
# ////we don't comments is the json file
json_data='{"A":1,"B":2,"C":3}'
# /////we load the json data we use this command
x=json.loads(json_data)
# ////to acces the json file we use print function
# print(x['A'])

# ----------------if we want to acces the json file out of the directry than we use this method

# /////importing the file using python
with open('data_json.json') as f:
    f1=f.read()
    f2=json.loads(f1)
    print(f2['personal'])

