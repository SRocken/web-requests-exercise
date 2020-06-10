# get_data.py

print("REQUESTING SOME DATA FROM THE INTERNET...")

# Get request for product's "name"
#{
# "aisle": "spices seasonings",
# "department": "pantry",
# "id": 2,
# "name": "All-Seasons Salt",
# "price": 4.99
#}
# Right answer is All-Seasons Salt

import requests
import json
import statistics

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
response = requests.get(request_url)
my_dict = json.loads(response.text)
print(my_dict["name"])

#Loop of requests

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
products = requests.get(request_url)
my_list = json.loads(products.text)
for p in my_list:
    print(p["id"], " ", p["name"])


#Gradebook
request_url3 = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
grades = requests.get(request_url3)
list_grades = json.loads(grades.text)
students = list_grades["students"]

grades = []
for i in students:
    i["finalGrade"] = float(i["finalGrade"])
    grades.append(i["finalGrade"])
avg = statistics.mean(grades)
mingrades = min(grades)
maxgrades = max(grades)

print("Average Grade: ", avg)
print("Lowest Grade: ",mingrades)
print("Highest Grade: ", maxgrades)
