import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Parse the JSON string into a Python dictionary
data = json.loads(sampleJson)

# Access the nested "salary" key
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

# Add a "birth_date" key at the same level as the "name" key
data["company"]["employee"]["birth_date"] = "1990-01-01"

# Convert the dictionary back to JSON string
updatedJson = json.dumps(data, indent=4)

# Save the dictionary as JSON to a file
with open("xp.json", "w") as file:
    file.write(updatedJson)


# with open("xp.json"", "w") as file_obj:
#     sampleJson = json.load(file_obj)

