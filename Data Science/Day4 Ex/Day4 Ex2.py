#Read Json file
#Download json file -> json file example [Country name , Population]
#Read iy using python
#Add item
#Input new thing and insert in json file
#After making Country
#Delete one Country
#Make a website that can add and delete
#and if it not there send message that is empty not found .


import json

# Specify the correct file path
file_path = r'C:\Users\PC\Downloads\Data Science\Day4 Ex\example.json'

# Open and read the JSON file
with open(file_path, 'r') as myjsonfile:
    jsondata = myjsonfile.read()
    
print(jsondata)





