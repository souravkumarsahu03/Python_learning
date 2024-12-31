# Access the nested key "marks" from the following nested data 


import json
student_data = """{ "student":{
        "grade":{
            "name" : "Sourav",
                "marks": 87
                }   
}"""

data = json.loads(student_data)
print(data["student"]["grade"]["marks"])